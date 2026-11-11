#!/usr/bin/env python3
"""S5: 完整 pfb 多步管道臂 — 分解 → 逐节点[搜索→逻辑校验→外部核验] loop → 封闭推理。

设计 (2026-11-08 成璐指令): "pfb本来就应该完整跑，直接在无泄漏状态跑" +
"分解的时候也查-逻辑-外信息逐个校验" + "全查-校验-再查这样loop循环，
最后验证好事实之后的分解和封闭推理才是有效的"。

与现有臂的区别:
  S0/A3/A4/S3 = 单轮 one-shot (S3 的"交叉核验"是 prompt 指令, 模型自说自话)
  S5          = 真·多步管道: harness 层真实执行检索 (research_hook/ego-browser),
                每个关键事实节点独立发起 LLM 调用做逻辑校验+外部核验,
                未通过校验的节点回炉重查 (≤K 轮), 全部收敛后才做封闭推理。
                这是生产 stage 外包模式的 pfb 化: 文件接口改成 JSON 记录,
                每步留痕可审计。

无泄漏: 各阶段 prompt 只喂题面+上一阶段产物, judge/gold 不进任何生成 prompt;
最终打分用 s8b_pilot.judge (gold 要点覆盖), 与 S0-A4 同一口径可比。

管道 (per rep):
  P1 decompose : 拆出 ≤N 个关键事实/前提节点 (编号 N1..NK), 每个附支撑它的结论
  P2 search    : 对每个节点调 research_hook(节点查询词) → 来源包 (arXiv API via ego-browser)
  P3 verify    : 每节点一次 LLM 调用: 逻辑自洽检查 + 对照来源核验 → status ∈ {verified, degraded, failed}
                 failed → 重查 (换查询词, ≤K 轮); 仍失败 → [待核验] 降级
  P4 synthesize: 基于已验证事实集做封闭推理, 输出最终答案 (未验证节点显式标注)
  J  judge     : gold 要点覆盖打分 (与 S0-A4 同口径)

Usage:
    python3 s5_pipeline.py --qs nat,soc --reps 2 --out runs-s5 --dry-run
    python3 s5_pipeline.py --qs nat --reps 1 --out runs-s5   # 冒烟
    python3 s5_pipeline.py --qs nat,soc --reps 500 --out runs-prod-s5  # 量产 (接在主 run 后)
"""
import argparse, json, math, os, random, re, sys, time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ablation_harness import call_llm, LLM_MODEL
from s8b_pilot import build_prompt, judge, QUESTIONS
from judge_v2_depth import score_run
from research_hook import research_hook, ResearchHookUnavailable

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_NODES = 60  # safety valve only — real stopping rule is the objective function, not this cap
# BUDGET_RETRIEVAL removed 2026-11-08 (user: no cap on search). _budget_used is now a pure counter for diagnostics.
# breadth-vs-depth trade-off weight in the decomposition objective:
#   S_alpha(T) = sum_n [ n*ln(k_n) + alpha * k_n*ln(n) ]
# alpha=0 -> pure depth-mining; alpha=1 -> symmetric depth/breadth; default 0.5
ALPHA_BREADTH = 0.5
_budget_used = {"n": 0}

def _budget_reset():
    _budget_used["n"] = 0

def _budget_take():
    """Count retrieval calls (diagnostic only); NEVER blocks — user directive 2026-11-08: no budget cap on search/ego-browser."""
    _budget_used["n"] += 1
    return True
MAX_ROUNDS = 2     # 每节点最大重查轮数 (含首轮)
SEARCH_PER_NODE = 4  # 每节点注入的来源上限

# ── 阶段 prompt ────────────────────────────────────────────────────────
P1_DECOMPOSE = (
    "你是严谨的研究员。下面是一道待解问题。你的任务不是回答问题本身，而是把它逐层拆解成"
    "回答所依赖的完整决策树。\n\n"
    "【节点来源标记 source（每个节点必填）】\n"
    "- given: 题目文本中直接给出的数值或条件；\n"
    "- knowledge: 你已掌握且属于常识/稳定事实的内容（学科定义、经典公式、架构参数等），不需要联网查证即可确认；\n"
    "- search: 完全不知道、必须检索才能确认的事实（实时数据、最新规格、具体参数等）。\n"
    "原则：能用 given/knowledge 覆盖的不要标 search——只有真正查不到的才需要检索。knowledge 节点的 claim 里要写出具体数值或公式，"
    "并在 evidence 栏注明「模型先验知识，属常识级事实」。若该数值有时效性风险，claim 末尾加「[时效待核]」。\n"
    "不确定具体数字时不要犹豫、也不要降级成定性描述：用符号变量替代（例如 ρ, L, u），"
    "把公式完整写出来——一个带变量的可计算表达式比一句定性判断有价值得多。变量在最终答案里保留为参数即可，不需要解出具体数值。\n\n"
    "【分解目标函数（显式优化准则）】\n"
    "你的分解树得分 = Σₙ [ n·ln(kₙ) + {alpha}·kₙ·ln(n) ]，其中 kₙ 是第 n 层的节点数（L1=直接因子层，L2=定义展开层，L3=可计算项层…），n 是层深。\n"
    "第一项奖励深度（同样的节点放在更深层贡献更大），第二项奖励广度（每层正交维度覆盖得越全贡献越大）。{alpha}=0 时纯挖深，{alpha}=1 时深挖与广搜完全对称——本题使用 {alpha}={alpha}，即两种挖掘收益并重。\n"
    "边际收益规律（精确）：向第 n 层新增 1 个节点，得分增量 = ln((kₙ+1)/kₙ) + {alpha}·ln(n)，且该节点若继续展开还会带来更深层的间接增量。注意三层含义——(a) 同一层内：kₙ 越大，再加一个兄弟节点的边际越小（对数递减），所以无差别横向铺量有饱和点，但每个真正正交的新维度都仍值得加；(b) 跨层：同样的 1 个节点放在第 n+1 层比放在第 n 层贡献更大（两项都随 n 增长），而且解锁它自己的子树；(c) 广度项保证「漏掉一个顶层正交维度」是有代价的——宁可先保证 L1/L2 覆盖完整，再往深处挖。因此——\n"
    "- 展开一个有 2-3 个正交因子的定义式节点（如 成本→「采购价、电费摊销、故障损耗」）比多铺一个浅层兄弟节点值钱得多；\n"
    "- 停止条件：当「再展开一层能带来的信息增量」低于「该层检索/核验的预算成本」时停，不要为了凑深度硬拆无信息量的子项。\n"
    "【检索策略】外部检索不限次数（source=search 的节点都会真实联网核验，given/knowledge 不触发检索）。最大化上述得分：把每个真正需要外部数据的 search 节点都查到位——宁可多查，不可漏查。给定/知识类节点直接写具体数值或符号变量公式，不要浪费在它们身上。\n"
    "预算不足时的取舍顺序：先保证所有 L1 正交维度都有节点（覆盖度），再把剩余预算按「展开增益/预算成本」从高到低分配给最深的未展开定义式节点。\n\n"
    "【逐层展开规则】\n"
    "1. 先识别顶层决策公式或目标函数（如成本公式、约束条件、评分标准），这是第 1 层；\n"
    "2. 对第 1 层的每个因子/参数，展开为第 2 层子节点——具体到需要查什么数字、什么公式、什么经验值；\n"
    "3. 对第 2 层中涉及复合量或可分解量的节点，继续展开为第 3 层（如 TCO → 摊销+电费+故障损耗；"
    "吞吐量 → prefill 算力瓶颈 + decode 带宽瓶颈）；\n"
    "4. 如果某节点的取值会影响其他节点的判断（交互效应），单独列出 SHARED 节点说明耦合关系；\n"
    "5. 不要停在'这个因素很重要'——必须拆到可以直接检索验证的具体事实（一个数字、一个公式、一个阈值）；\n"
    "6. 复合概念展开：当问题中出现由多个正交维度构成的复合词（即该词的取值取决于两个或以上独立因子的组合），"
    "必须将其展开为各构成因子作为同级子节点，不得将复合词作为单一叶子节点保留。"
    "判断标准：如果你能用「X = f(A, B)」的形式写出该概念的定义式，则 A 和 B 必须是独立分支；\n"
    "7. 定义式必须展开到可计算项：如果某节点的 claim 是一个定义式（X = A + B + C），"
    "则每个组成项必须有对应的 L3 子节点给出其计算公式（未知数值可用符号变量表示）或具体数值来源。"
    "停在'X 包含 A、B、C'而不拆出 A/B/C 各自的计算方式 = 未完成分解。\n"
    "8. 子问全覆盖：问题文本中显式列出的每个子问（如 (a)(b)(c)）必须在 L1 层有至少一个节点直接支撑它。如果某个子问要求区分多种口径/度量（例如同时问『按字节』和『按请求』），则必须为每种口径各建一个独立节点，不得合并为一个节点。\n\n"
    "9. 定量承诺：每个节点的 claim 必须携带具体数值、公式或可计算的表达式——不允许纯定性表述（如『显著』『有限』『较高』）。\n"
"若某事实确实只有定性结论，claim 末尾标 [待核验] 并给出最接近的量化形式（变量/参数化公式）。\n"
"原因：P4 综合时只能把 fact table 里的具体数字写进答案；定性节点 = 答案里少一个数字 = 覆盖率掉一个点。\n\n"
    "分布参数必须实例化：涉及幂律/Zipf/Pareto 等分布时，不能只写『长尾分布』——必须给出具体参数值或假设区间（如 α∈[0.8, 1.2]、β=0.9±0.1），\n"
    "并算出至少一个可检验的推论（如 top 10% 对象贡献 ≥85% 请求量）。没有参数值的分布描述 = 不可计算 = P4 无法代入。\n\n"
    
    "【展开深度与停止条件（由目标函数决定，不设固定节点数上限）】\n"
    "不要预设节点总数。判断标准只有一个：对树上每个非叶子候选位置问——「再往下展开一层，能否产生新的具体数值、公式或可检索事实？」能 → 必须展开；不能（只剩定性描述或同义复述）→ 停。\n"
    "停止条件（三个方向都要判）：向下——若某节点已是最小可计算单元（单个不可再分的数值或公式），它的任何子节点都不增加信息量，停；横向同层——若某层 kₙ 已大到新增兄弟节点只是同义复述或边缘案例，边际 ln((kₙ+1)/kₙ) 趋近于零，停；横向跨层——若某个正交维度在浅层还没有节点（覆盖缺口），广度项会持续扣分，必须补上而不是只顾深挖。除此之外默认继续拆：深层节点直接贡献更大（∝n），且每个新节点都解锁自己的子树。\n"
    "禁止为了控制篇幅而提前收树；也禁止硬拆无信息量的子项凑深度（那会稀释 kₙ 的有效性且不增加答案内容）。\n"
    "【排除/筛选类结论的强制继续规则】任何「X 不可行 / X 被排除 / 本题无解」这类判定，只能作为树的中间层或某个分支的叶子，不能作为整棵树的终点。做出排除之后必须立即追问并展开：(a) 放宽哪个前提后 X 变为可行？(b) 放宽的代价是什么（量化到可计算的程度）？(c) 在放宽后的可行集里，原问题的目标函数如何重新排序？——这三问各自至少产生一个节点。原因：排除本身不回答问题，回答问题是「在什么条件下、以什么代价、选哪个」；只给排除不给后续 = 把最便宜的浅树当成了完整答案。\n\n"
    "【示例：什么是'每个分支都挖到最深'——只展示结构，不展示任何领域内容】\n"
    "例1（某子树，3层×2-3节点）：\n"
    "  N5: <某个可分解的复合概念> (L1)\n"
    "    N6: <组成部分A> = f(参数a, 参数b, 参数c) (L2)\n"
    "      N7: 实例X: f(a_X, b_X, c_X) ≈ v_X [已核验] (L3)\n"
    "      N8: 实例Y: f(a_Y, b_Y, c_Y) ≈ v_Y [已核验] (L3)\n"
    "    N9: <组成部分B> = g(参数d, 参数e) (L2)\n"
    "      N10: 实例X: d_x × e_x = w_x [推导] (L3)\n"
    "结构要点：N5 不是叶子——它下面有 ≥2 个 L2 分支，每个 L2 又展开到 L3 的具体数值。如果停在 N5 就收手，这棵树就废了。深度和广度都有收益：多一层 ∝ n 的贡献，多一个节点 ∝ ln(kₙ) 的贡献。\n\n"
    "例2（排除结论后继续分解）：\n"
    "  N12: <方案P>在约束C下不可行 (L1) ← 排除结论，不能停在这里\n"
    "    N13: 放宽哪个前提后 P 变为可行？(L2)\n"
    "      N14: 放宽代价 = h(新约束) ≈ 具体量 [待核验] (L3)\n"
    "      N15: 放宽后的质量/性能损失 ≈ d% [待核验] (L3)\n"
    "    N16: 放宽的代价是什么（量化）(L2)\n"
    "      N17: 哪些候选支持新约束，哪些不支持 (L3)\n"
    "    N18: 放宽后目标函数重新排序 → 新的最优解 (L2)\n"
    "结构要点：N12 是排除结论，但它下面挂了 3 个 L2 分支，每个都挖到了 L3。排除本身不回答问题，回答问题是「在什么条件下、以什么代价、选哪个」。\n\n"
    "注意：以上两个例子中的尖括号内容都是占位符，你需要根据实际问题填入自己的节点。例子只告诉你树应该长什么样（几层、每层几个节点、叶子长什么样），不告诉你应该拆什么。\n\n"
    "【格式要求】\n"
    "每个节点给：编号（N1, N2, ...）、一句话陈述（具体到可检索的事实）、层级标记（L1/L2/L3）、"
    "它支撑问题的哪个子问、来源标记 source（given|knowledge|search）、一条英文检索词（具体到该事实本身；source=given/knowledge 时可为空字符串）。\n"
    "只输出 JSON，格式：{{\"nodes\": [{{\"id\": \"N1\", \"claim\": \"...\", \"level\": \"L1\", \"source\": \"given|knowledge|search\", "
    "\"supports\": \"a\", \"search_query\": \"english query\"}}, ...]}}\n\n"
    "【问题】\n{question}\n"
)

P15A_DIMENSIONS = (
    "你是研究问题分解专家。下面是一道待解问题。"
    "你的唯一任务是：从问题文本本身出发，列出回答它必须覆盖的所有顶层维度。\n\n"
    "【规则】\n"
    "- 只看问题文本，不参考任何外部框架或常识性检查清单；\n"
    "- 每个维度用一句话描述（只陈述该维度是什么，不举具体例子）；\n"
    "- 维度之间必须正交——一个维度的信息不能由其他维度推出；\n"
    "- 通常 4-8 个维度，宁少勿多。\n\n"
    "【格式要求】只输出 JSON：{{\"dimensions\": [\"...\", ...]}}\n\n"
    "【问题】\n{question}\n"
)

P15B_GAP_FILL = (
    "你是研究覆盖度审查员。下面是一道问题、一组顶层维度、和一份已生成的事实节点列表。"
    "对照维度列表，找出哪些维度没有被节点充分覆盖，为缺失维度生成补充节点。\n\n"
    "【判断标准】\n"
    "- 某维度有 ≥2 个具体可检索的节点 → 视为已覆盖；\n"
    "- 某维度只有 0-1 个节点且停留在定性层面 → 视为缺失，需补 L2/L3 节点；\n"
    "- 补充节点必须具体到可检索的事实（一个数字、一个公式、一个阈值），带英文检索词。\n\n"
    "【规则】\n"
    "- 只补缺失维度，不重复已有节点；\n"
    "- 如果所有维度都已充分覆盖，new_nodes 输出空列表；\n"
    "- 补充节点数量通常 3-10 个。\n\n"
    "【格式要求】只输出 JSON：{{\"missing_dimensions\": [\"...\", ...], \"new_nodes\": "
    "[{{\"id\": \"NXX\", \"claim\": \"...\", \"level\": \"L2|L3\", "
    "\"supports\": \"...\", \"search_query\": \"english query\"}}, ...]}}\n\n"
    "【问题】\n{question}\n\n"
    "【顶层维度】\n{dimensions}\n\n"
    "【已有节点】\n{existing_nodes}\n"
)

P3_VERIFY = (
    "你是事实核验员。针对下面这个关键事实节点，执行两步检查：\n\n"
    "【第一步 — 逻辑校验】该陈述在逻辑上是否自洽？量纲/量级是否合理？"
    "是否存在内部矛盾或明显违背基本物理/经济直觉的地方？\n\n"
    "【第二步 — 外部核验】先判断参考来源与该事实是否相关（主题/领域是否匹配），再在相关性成立时判断是否有明确支持。"
    "支持强度：直接支持 / 间接支持 / 无关 / 矛盾。注意：若全部来源均与该事实主题无关，外部核验记为「无可用外部证据」——"
    "此时只能依据第一步逻辑校验判定，不得因来源不相关而判 failed，也不得把「来源无关」写成「来源支持」。\n\n"
    "【判定规则】\n"
        "- verified: 逻辑自洽，且满足以下任一条件：(a) 至少一个来源直接支持；(b) 该事实可从第一性原理/题面条件推出且无来源与之矛盾；(c) 两个或以上独立来源给出一致或兼容的数值/结论（即使没有单一来源'直接陈述'）；\n"
        "- degraded: 逻辑自洽但仅有一个间接来源、且无法排除其他可能性 → 保留但降级为定性表述；\n"
        "- failed: 仅当该陈述与参考来源明确矛盾，或存在硬逻辑错误（量纲错/内部矛盾）时才判 failed。\n"
        "注意：来源未覆盖 ≠ 错误。数学性质、统计规律这类可从第一性原理推出的事实，"
        "若逻辑校验通过且无来源与之矛盾，应判 verified 并在 evidence 里注明「逻辑推导成立，来源未直接覆盖」；"
        "不要仅因检索结果不相关就判 failed。"
    "【来源标记】\n该节点的 source 标记为 {source}。若 source 为 given 或 knowledge：核验重点变为「逻辑自洽 + 数值量级合理」，无需外部来源支持即可判 verified（evidence 注明「先验知识/题面给定，逻辑校验通过」）；若 source 为 search：按下方判定规则执行外部核验。\n\n"
    "【关键事实节点】\n{node_id}: {claim}\n\n"
    "【参考来源】\n{sources_block}\n\n"
    "只输出 JSON：{{\"status\": \"verified|degraded|failed\", \"logic_ok\": true/false,\n"
    "\"evidence\": \"一句话说明依据（引用来源编号）\", \"corrected_claim\": \"若 failed/degraded，给出修正后的表述；否则空字符串\"}}"
)

P4_SYNTHESIZE = (
    "你是严谨的研究员。下面是一道问题和一组已经过核验的事实节点表。"
    "请基于这些事实做封闭推理，给出最终答案。\n\n"
    "【分析层 — 对 fact table 中的数值/公式节点做后处理（不新增事实，只推导）】\n"
    "1. 参数敏感性：若某 verified 节点的关键参数处于定义式的分母/指数/阈值/乘数位置，写出 f(参数×0.9)、f(参数×1.1) 的表达式或数值区间——「若参数取 X，则 Y ∈ [a, b]」；\n"
    "2. 条件推断：题面隐含但未显式给出的前提（如稳态假设、边界条件），列出并说明其对结论的影响方向；\n"
    "3. 分布估计：当数据点不足以确定唯一值时，给出最可能的参数化形式和合理区间（用符号表示未知量）。\n"
    "以上分析结果写入正文对应段落，标签为 [推导]。若 fact table 中无相关数值/公式节点，跳过本节。\n\n"
    "要求：\n"
    "1. 事实表中使用规则：verified 节点可直接作定量依据；degraded 节点若 claim 本身含具体数值/公式且逻辑自洽，允许作定量依据（标签写 [推导]），仅当 claim 是纯定性表述时才限于定性引用；\n"
    "2. failed 或缺失的节点不得假设其值——显式写出「缺 X 导致 Y 无法定量」，给出区间而非点估计；\n"
    "3. 先给结论，再给因果链，不跳步；每个数字写出量纲和口径；\n"
    "4. 溯源标注（硬性格式要求）：正文中每个关键数字/事实，紧跟其后加一个方括号标签，只允许三种写法：[已核验]、[推导]、[凭记忆]。"
"例如：LRU 字节命中率约为 78% [推导]；典型 CDN 缓存容量约 10TB [凭记忆]。自检：数一下正文里带百分号/倍数/容量单位的数字共几个，"
"标签总数不得少于该数字个数的三分之一；标 [凭记忆] 的数值必须配降置信词（约/估计/通常）。禁止只在末尾摘要表写状态而不给正文数字打标签。\n"
    "5. 定量优先原则：fact table 里任何 verified/degraded 节点携带的具体数值（容量、比率、价格、复杂度、带宽），最终答案必须把它用进定量推导——代入公式、算出区间或点估计。"
"只有当该数值与问题无关、或节点 claim 本身是纯定性表述时，才允许只做定性引用。禁止把可用的具体数字降级成『有限』『显著』『大约』这类模糊描述——"
    "有数字就写数字，缺数字才写区间，这是硬约束。\n"
    "禁止用「无法给出定量点估计」「只能定性推断」「由于缺少参数」这类话把整段结论降级为定性——\n"
    "fact table 里 verified 节点已给了公式（如 H = Cache_Size/Total_Bytes × f(α,β)），你的工作是代入已知参数算出数值范围；\n"
    "对未知参数用符号表示并给合理假设区间（如 x_min ∈ [1KB, 10MB] → 命中率 ∈ [a%, b%]）。\n"
    "「无法定量」只允许出现在 fact table 里确实没有任何相关数值/公式节点时。有节点却说不定量 = 没做完工作。\n"
    "6. 口径分离 + 节点落地原则：fact table 中每个 verified/degraded 且含具体数值或公式的节点，其核心结论必须在正文中显式出现——不是「提到相关概念」，而是把该节点的具体数字/公式/判断写进推导链。\n"
"若存在多个口径不同的度量（按字节 vs 按请求、稳态 vs 瞬态、上界 vs 下界），必须逐口径分别给结论和推导。\n"
"自检（硬性）：(a) 数 fact table 里 verified+degraded 且带数字的节点共 N 个，正文中必须能定位到 ≥N 个对应的具体数字/公式；\n"
"(b) 数 fact table 里有几种不同口径，正文里每种口径是否都有独立句子给出结果。不满足则重写对应段落。\n"
    "7. 起始假设链原则：如果问题包含「从 X 出发」「基于 X」「以 X 为前提」等起始条件，答案第一段必须明确写出该起始假设及其推导链（X → 推导出什么约束 → 如何影响后续分析），不能跳过起点直接进分析层。\n"
    "例如：「从生物演化出发」→ 第一段写「生存压力（金钱/资源有限）→ 定向搜索行为 → 偏好噪声作为探索机制」，然后再展开具体分析。\n"
    "自检：数一下问题里的起始条件有几个，正文第一段是否每个都显式出现了。\n\n"
    "8. 最后单独一节「事实核验摘要」：列出你实际使用了哪些节点、各自状态、哪些结论因此受限。\n\n"
    "【问题】\n{question}\n\n"
    "【已核验事实节点表】\n{fact_table}\n"
)


def _perturb():
    return "".join(random.choice(["\u200b", "\u200c", " ", "\u200d"]) for _ in range(4))


def _extract_json(text):
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    s = m.group(0)
    # 从前往后找第一个能解析成功的 { ... } 区间。
    # 旧实现只试一次全量贪婪匹配：模型输出被 max_tokens 截断时 JSON 尾部残缺，
    # 整个 parse 失败 → decompose 返回 0 节点（v13 r5 事故）。
    # 这里退而求其次：截取到最后一个完整对象（以 "}" 结尾且前面是 "," 或 "[" 的边界），
    # 把残缺尾部的半截 node 丢弃，保住已完整的 nodes。
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        pass
    # 截断修复：找到最后一个完整闭合的对象边界，补上缺失的 "]}"
    for end in range(len(s), max(0, len(s) - 2000), -1):
        if s[end - 1] == "}":
            candidate = s[:end].rstrip().rstrip(",") + "\n  ]\n}"
            try:
                return json.loads(candidate)
            except json.JSONDecodeError:
                continue
    return None


def decompose(question, max_retries=3, unlimited=False):
    """P1: 拆出关键事实节点。返回 nodes 列表。JSON 解析失败时 retry（降温度）。

    v2 (2026-11-09): r5 事故根因不是 max_tokens 截断（usage out=2128 < 8000），
    是模型在 ~2100 token 处主动停笔、JSON 停在半截 node。旧实现 parse 失败直接
    放弃整份输出（丢掉已完整的 N1-N10）。现在：_extract_json 有截断兜底，
    只要解出 ≥1 个完整 node 就接受；全空才 retry（retry 用更低温度减少跑飞）。
    """
    last_raw = ""
    for attempt in range(max_retries + 1):
        temp = 0.7 if attempt == 0 else 0.3
        prompt = P1_DECOMPOSE.format(question=question, alpha=ALPHA_BREADTH) + _perturb()
        out, _ = call_llm(prompt, max_tokens=8000, temperature=temp, top_p=0.95)
        last_raw = out or ""
        d = _extract_json(last_raw) or {}
        nodes = d.get("nodes") or []
        nodes = [n for n in nodes if isinstance(n, dict) and n.get("claim")]
        if nodes:
            for i, n in enumerate(nodes[:MAX_NODES], 1):
                n.setdefault("id", f"N{i}")
                n.setdefault("source", "search")
            from collections import Counter as _C
            sc = _C(n.get("source", "?") for n in nodes)
            print(f"  [decompose] source mix: {dict(sc)}", flush=True)
            cap = len(nodes) if unlimited else MAX_NODES
            return nodes[:cap], last_raw
        print(f"  [decompose] attempt {attempt+1}: no nodes parsed, retrying...", flush=True)
    return [], last_raw


def gap_check(question, existing_nodes):
    """P1.5: 两轮覆盖度审查。A=独立列维度（不看已有节点），B=对照补缺。"""
    # P15A: 独立识别顶层维度（不受已有节点锚定）
    prompt_a = P15A_DIMENSIONS.format(question=question) + _perturb()
    try:
        out_a, _ = call_llm(prompt_a, max_tokens=2048, temperature=0.7, top_p=0.95)
        d_a = _extract_json(out_a or "") or {}
        dimensions = d_a.get("dimensions") or []
    except Exception as e:
        print(f"  [gap_check A] error: {e}", flush=True)
        return [], [], ""
    if not dimensions:
        print(f"  [gap_check A] no dimensions identified", flush=True)
        return [], [], out_a or ""
    print(f"  [gap_check A] {len(dimensions)} dimensions: {' | '.join(d[:30] for d in dimensions[:5])}...", flush=True)

    # P15B: 对照维度列表补缺失节点
    node_lines = "\n".join(
        f"{n['id']} [{n.get('level','?')}]: {n['claim']}" for n in existing_nodes)
    dim_lines = "\n".join(f"- {d}" for d in dimensions)
    prompt_b = P15B_GAP_FILL.format(
        question=question, dimensions=dim_lines, existing_nodes=node_lines) + _perturb()
    try:
        out_b, _ = call_llm(prompt_b, max_tokens=4096, temperature=0.7, top_p=0.95)
        d_b = _extract_json(out_b or "") or {}
        new_nodes = [n for n in (d_b.get("new_nodes") or [])
                     if isinstance(n, dict) and n.get("claim")]
        missing = d_b.get("missing_dimensions") or []
        return new_nodes, missing, out_b
    except Exception as e:
        print(f"  [gap_check B] error: {e}", flush=True)
        return [], [], ""


def search_node(node, qid="gpu"):
    """P2: 对该节点做真实联网检索 (arXiv API via ego-browser)。失败降级为空。
    given/knowledge 节点不触发检索（逻辑核验即可）；search 节点全部真实联网（无预算上限）。

    local_corpus 通道按题域启用：_LOCAL_CORPUS_DIRS 目前只有 D1-gpu-research 语料，
    对 nat/soc 题 grep 出的"命中"全是无关 GPU 文档，会污染 P3 核验（nat 100 reps
    evidence 里大量出现"参考来源[1]为GPU硬件规格...与该节点无关"）。
    2026-11-09: 非 gpu 题禁用该通道，其余通道不受影响。"""
    if node.get("source", "search") in ("given", "knowledge"):
        return [], None  # no retrieval needed — logic verification only
    _budget_take()  # counter only, never blocks
    q = node.get("search_query") or node["claim"]
    try:
        srcs = research_hook("s5-node", q, max_results=SEARCH_PER_NODE,
                             enable_local=(qid == "gpu"))
        return srcs, None
    except ResearchHookUnavailable as e:
        return [], str(e)
    except Exception as e:
        return [], str(e)


def sources_block(srcs):
    if not srcs:
        return "(本轮检索无可用来源 — 全部通道失败)"
    lines = []
    for i, s in enumerate(srcs, 1):
        lines.append(f"[{i}] {s.get('title','?')}\n    URL: {s.get('url','?')}\n    摘要: {s.get('snippet','')[:800]}")
    return "\n".join(lines)


def verify_node(node, srcs):
    """P3: 单节点逻辑+外部核验。返回 (status, evidence, corrected_claim)。"""
    prompt = P3_VERIFY.format(
        node_id=node["id"], claim=node["claim"],
        source=node.get("source", "search"),
        sources_block=sources_block(srcs)) + _perturb()
    out, _ = call_llm(prompt, max_tokens=1200, temperature=0.7, top_p=0.95)
    d = _extract_json(out or "") or {}
    status = d.get("status")
    if status not in ("verified", "degraded", "failed"):
        status = "degraded"  # 解析失败按保守档处理
    return status, d.get("evidence", ""), d.get("corrected_claim", ""), out


_LABELS = ("[已核验]", "[推导]", "[凭记忆]")


def _label_stats(ans):
    """正文溯源标注统计：标签数 / 关键数字数 / 覆盖率。"""
    n_labels = sum(ans.count(p) for p in _LABELS)
    import re as _re
    n_nums = len(_re.findall(r'\d+\.?\d*\s*(%|个百分点|百分点|倍|ms|MB|GB|TB)', ans))
    return {"n_labels": n_labels, "n_numeric_claims": n_nums,
            "label_coverage": round(n_labels / max(n_nums, 1), 2)}





P1H_INDEX = (
    "你是严谨的研究员。下面是一道待解问题，正在被逐层分解成一棵目录树（结构同项目标准："
    "每个父节点是一个文件夹，它的子节点清单就是该文件夹的 INDEX.md——只列条目和一句话说明，"
    "不抄内容；每层的 INDEX 只描述下一层有哪些条目）。\n\n"
    "【本轮任务】只对给定的这些父节点做分解：对每个父节点，列出它的全部正交子维度作为子节点"
    "（即写出这个父节点文件夹的 INDEX）。不要碰其他分支，不要重复已确认事实里的内容。\n\n"
    "【子节点规则】\n"
    "1. 每个子节点必须携带具体数值、公式或可计算表达式——不允许纯定性表述；确实只有定性结论的标 [待核验] 并给出最接近的量化形式。\n"
    "2. 复合概念展开：若某子维度能写成 X = f(A, B)，则 A、B 必须是独立兄弟节点，不得合并。\n"
    "3. 定义式必须展开到可计算项：父节点是 X = A + B + C 时，A/B/C 各自必须有子节点给出计算方式。\n"
    "4. 子问全覆盖：问题文本显式列出的每个子问必须在 L1 有节点支撑；要求区分口径时为每种口径各建一个节点。\n"
    "5. 排除/筛选类结论不能当终点：「X 不可行」之后必须继续展开（放宽哪个前提/代价多少/重新排序），三问各至少一个节点。\n"
    "6. 正交性：同一父节点下的兄弟节点之间不得互相包含或同义复述；宁缺毋滥，但真正正交的维度不得漏。\n"
    "7. 成本/TCO 类父节点必须按时间结构展开为独立兄弟：瞬时资本(CapEx: 购置价/折旧) / 运行(OpEx: 电费·冷却·维护, 带利用率假设) / "
    "可靠性(故障率·MTBF·MTTR·冗余方案·保修/RMA) / 不确定性(关键参数的取值区间与方差来源)。只给一个总价 = 该父节点分解不完整，必须继续拆。\n"
    "8. 微架构优先：硬件对比不得停在营销规格（显存大小/价格），必须下钻到决定推理性能的一手参数——内存带宽、HBM/GDDR 代际、SM/CUDA core 数、"
    "L2 cache 容量、制程与 TDP、互联拓扑(NVLink/PCIe 代数带宽)。这些是题目和 L1 骨架不会明说的，靠领域知识补全并标 source=knowledge。\n\n"
    "【何时停】对每个父节点问：再往下拆一层还能产生新的具体数值/公式/可检索事实吗？能 → 必须拆；"
    "不能（只剩同义复述或定性描述）→ 该父节点本轮不产生子节点。全部父节点都停 → 输出空 nodes。\n\n"
    "【节点来源标记 source（必填）】given=题面直接给出 / knowledge=常识级稳定事实（claim 里写具体数值或公式，evidence 注明「模型先验知识」，有时效风险加 [时效待核]）/ search=必须联网查证的事实。能用 given/knowledge 覆盖的不要标 search。\n\n"
    "【格式】每个节点：编号 N{start} 起连续、claim（一句话，具体到可检索）、level（比父节点深 1 层）、"
    "source、supports（支撑哪个子问）、search_query（英文检索词；given/knowledge 可为空）。"
    "只输出 JSON：{{\"nodes\": [{{\"id\": \"N{start}\", \"claim\": \"...\", \"level\": \"L2\", \"source\": \"knowledge\", \"supports\": \"b\", \"search_query\": \"\"}}, ...]}}\n\n"
    "【问题】\n{question}\n\n"
    "【已确认事实（前几轮的结果，作为给定条件使用，不要重复拆解）】\n{confirmed_block}\n\n"
    "【本轮要分解的父节点】\n{parents_block}"
)


def _sa_tree(nodes):
    """S_α 树形得分（与 P1 prompt 中同一公式，harness 侧实现）：
    S = Σₙ [ n·ln(kₙ) + α·kₙ·ln(n) ]，kₙ = 第 n 层节点数。
    同时返回每层 kₙ 供状态机日志用。"""
    from collections import Counter as _C
    lv = _C(int((n.get("level") or "L?").lstrip("L")) for n in nodes
            if str(n.get("level") or "").startswith("L") and str(n.get("level")).lstrip("L").isdigit())
    s = 0.0
    per_layer = {}
    for n, k in sorted(lv.items()):
        contrib = n * math.log(k) + ALPHA_BREADTH * k * math.log(n)
        s += contrib
        per_layer[n] = {"k": k, "contrib": round(contrib, 3)}
    return round(s, 4), per_layer


def decompose_explore(question, max_rounds=8, budget_nodes=40, per_layer_cap=6, qid="gpu"):
    """P1e: 探索式分解 — 状态机主循环（无限回退，目标函数驱动停止）。

    每轮：decompose(整题 + 已确认事实) → gap_check(补广度) → 对未核验的 search
    节点做一轮 P2/P3 核验 → verified/degraded 节点作为【已确认事实】注入下一轮。
    回退是无限的——没有固定轮数上限；停止判据全部来自边际收益/行为证据：
      R1 饱和：本轮新增节点 = 0（模型找不到新东西可拆 = 定义级粒度自然停）
      R2 预算：累计节点 ≥ budget_nodes —— **软约束，不停止**。
         触发"该做层级压缩"信号（把深层叶子折叠成中间层摘要），树继续长。
         general 超级工程拆到定义级粒度节点数可达千级，硬上限会砍掉合法深度。
      R3 停滞：连续 2 轮 S_α 无增长（拆出来的都是同义复述）
    **层内限流（per-layer cap）**：每层每轮最多吸收 per_layer_cap 个新节点，
    超出的留到下一轮——防止深层同层数量爆炸导致单轮 token 溢出 / 注意力稀释。
    被截断的层会在日志里标记 capped=True，下一轮继续消化。
    返回 (nodes_all, rounds_log)，rounds_log 含每轮的 S_α、新增节点、停止原因。
    """
    confirmed = []          # [(id, claim, status)] 注入下一轮的已确认事实
    nodes_all = []
    seen_ids = set()
    rounds_log = []
    prev_sa = None
    stagnant = 0            # 连续无增长计数
    stop = None             # 停止原因（R1/R3/R4），循环内设置
    rnd = 0
    while True:
        rnd += 1
        # 防御性硬上限（v16.3 bug #5 修复）：R2 改软约束后循环真的无限了，
        # gpu 域 R1 迟迟不触发导致单 rep 失控。max_rounds 管"别失控"，
        # budget_nodes/compress_flag 管"该压缩了"，两者语义正交。
        if max_rounds and rnd > max_rounds:
            stop = "R4-max-rounds"
            break
        q_ext = question
        if confirmed:
            block = "\n".join(f"- {i}: {c} [{s}]" for i, c, s in confirmed[-budget_nodes:])
            q_ext += ("\n\n【已确认事实（前几轮分解+核验的结果，直接作为 given/knowledge 使用，"
                      "不要重复拆解它们；你的任务是找出尚未覆盖的维度并继续向深层展开）】\n" + block)
        nodes, raw = decompose(q_ext)
        new_nodes = [n for n in nodes if n["id"] not in seen_ids]
        seen_ids.update(n["id"] for n in nodes)
        # 广度审查只对新增部分跑（已有节点在上一轮已被审过）；无新增则跳过，省两次调用
        if new_nodes:
            new_nodes2, missing, _ = gap_check(question, new_nodes)
            candidates = new_nodes + new_nodes2[:max(0, MAX_NODES - len(nodes_all))]
        else:
            candidates, missing = [], []
        # 层内限流：每层每轮最多吸收 per_layer_cap 个新节点，超出的留到下一轮。
        # 深层同层数量大时（如 L3 一次出 15 个），单轮全吃下会导致 token 溢出
        # 和注意力稀释；截断后下一轮模型看到已确认事实块会继续消化剩余维度。
        from collections import Counter as _C2
        layer_counts = _C2(int(str(n.get("level") or "L?").lstrip("L")) for n in nodes_all
                           if str(n.get("level") or "").startswith("L") and str(n.get("level")).lstrip("L").isdigit())
        added, capped_layers = [], set()
        for n in candidates:
            lv = int(str(n.get("level") or "L?").lstrip("L")) if str(n.get("level") or "").startswith("L") and str(n.get("level")).lstrip("L").isdigit() else 0
            if lv > 0 and layer_counts[lv] >= per_layer_cap:
                capped_layers.add(lv)
                continue
            added.append(n)
            layer_counts[lv] += 1
        nodes_all.extend(added)
        sa, per_layer = _sa_tree(nodes_all)
        # 一轮 P2/P3 核验：只查 source=search 且未核验过的节点
        to_verify = [n for n in nodes_all if n.get("source", "search") == "search"
                     and n["id"] not in {c[0] for c in confirmed}]
        verified_now = []
        for node in to_verify[:12]:   # 每轮最多核验 12 个，控制 wall time
            srcs, err = search_node(node, qid=qid)
            if err:
                status, evidence, corrected, _raw = ("degraded", f"检索失败: {err}", node["claim"], "")
            else:
                status, evidence, corrected, _raw = verify_node(node, srcs)
            verified_now.append((node["id"], corrected or node["claim"], status))
        confirmed.extend(verified_now)
        stop = None
        # R1 饱和：本轮无任何新增节点（模型找不到新东西可拆 = 定义级粒度自然停）。
        # 注意口径是"所有层合计"——某一层被限流截断不算饱和，剩余维度下一轮继续消化；
        # 只有整棵树都长不出新节点才是真饱和。
        if len(added) == 0:
            stop = "R1-saturation"
        else:
            # R3 停滞：连续 2 轮 S_α 无增长（新增节点都是同义复述）
            if prev_sa is not None and sa <= prev_sa + 1e-6:
                stagnant += 1
            else:
                stagnant = 0
            if stagnant >= 2:
                stop = "R3-stagnant"
        # R2 预算阀：软约束，不停止循环。超过 budget_nodes 后在日志里标记
        # compress_triggered=True（提示该做层级压缩：把深层叶子折叠成中间层摘要），
        # 树继续长——general 超级工程拆到定义级粒度节点数可达千级，硬上限会砍掉合法深度。
        compress_flag = len(nodes_all) >= budget_nodes
        prev_sa = sa
        rounds_log.append({"round": rnd, "n_new": len(added), "n_total": len(nodes_all),
                           "S_alpha": sa, "per_layer": per_layer,
                           "capped_layers": sorted(capped_layers),
                           "compress_triggered": compress_flag,
                           "n_verified_this_round": len(verified_now), "stop": stop})
        print(f"  [state-machine] r{rnd}: +{len(added)} nodes (total {len(nodes_all)}), "
              f"S_α={sa}, verified +{len(verified_now)}, stop={stop}", flush=True)
        if stop:
            break
    return nodes_all, rounds_log


def _run_p1p2p3(rec, tag, question, qid="gpu"):
    """P1 decompose + P2 search + P3 verify. Sets stages.p2p3_nodes, n_verified, n_nodes."""
    t0 = time.time()
    # P1
    nodes, p1_raw = decompose(question)
    rec["stages"]["p1_decompose"] = {"nodes": len(nodes), "levels": {str(k): int(v) for k, v in Counter(n.get("level") or "?" for n in nodes).items()}, "raw": p1_raw}
    print(f"  [{tag}] P1: {len(nodes)} nodes", flush=True)
    if not nodes:
        rec["error"] = "decompose returned no nodes"
        rec["n_nodes"], rec["n_verified"] = 0, 0
        rec["stages"]["p2p3_nodes"] = []
        return rec
    # P1.5: gap check — 覆盖度审查，补缺失维度
    new_nodes, missing_dims, p15_raw = gap_check(question, nodes)
    if new_nodes:
        start_id = len(nodes) + 1
        for i, n in enumerate(new_nodes):
            n.setdefault("id", f"N{start_id + i}")
        nodes.extend(new_nodes[:MAX_NODES - len(nodes)])
        print(f"  [{tag}] P1.5: +{len(new_nodes)} nodes (missing: {', '.join(missing_dims[:4])}) → total {len(nodes)}", flush=True)
    else:
        print(f"  [{tag}] P1.5: no gaps found", flush=True)
    rec["stages"]["p15_gap_check"] = {"added": len(new_nodes), "missing": missing_dims, "raw": p15_raw[:2000]}
    # P2+P3 per node (with re-search loop)
    facts = []
    for node in nodes:
        node_rec = {"id": node["id"], "claim": node["claim"],
                    "level": node.get("level", "?"),
                    "source": node.get("source", "search"),
                    "search_query": node.get("search_query", "")}
        rounds = []
        for rnd in range(1, MAX_ROUNDS + 1):
            srcs, err = search_node(node, qid=qid)
            if err:
                status, evidence, corrected, raw = ("degraded", f"检索失败: {err}；claim 保留待后续补查", node["claim"], "")
            else:
                status, evidence, corrected, raw = verify_node(node, srcs)
            rounds.append({"round": rnd, "n_sources": len(srcs), "search_err": err,
                           "status": status, "evidence": evidence})
            node_rec.update(status=status, evidence=evidence,
                            corrected_claim=corrected or node["claim"])
            if status != "failed":
                break
            # failed → 用核验员给出的修正表述重查 (corrected_claim 是核验员对错误的具体定位,
            # 比拼接关键词更接近事实本身; 空则退回原 claim)
            new_q = corrected.strip() or node["claim"]
            node["search_query"] = new_q[:150]
            print(f"  [{tag}] {node['id']} round {rnd} FAILED → re-search with corrected claim", flush=True)
        node_rec["rounds"] = rounds
        if node_rec["status"] == "failed":
            node_rec["status"] = "unverified"  # 重查耗尽 → 降级 [待核验]
        facts.append(node_rec)
    rec["stages"]["p2p3_nodes"] = facts
    n_v = sum(1 for f in facts if f["status"] == "verified")
    rec["n_nodes"], rec["n_verified"] = len(facts), n_v
    rec["budget_used"] = _budget_used["n"]
    print(f"  [{tag}] P2/P3 done: {n_v}/{len(facts)} verified", flush=True)


def run_one(qid, rep, dry_run=False, rec_override=None):
    tag = f"S5-{qid}-r{rep}"
    question = QUESTIONS[qid]
    rec = rec_override or {"tag": tag, "arm": "S5", "qid": qid, "rep": rep,
           "model": LLM_MODEL, "ts": datetime.now(timezone.utc).isoformat(),
           "stages": {}}
    if dry_run:
        print(f"[dry] {tag}: pipeline ready (P1 decompose → P2 search×N → P3 verify×N → P4 synthesize)")
        return rec
    t0 = time.time()
    if rec.get("_fact_table_override") is not None:
        facts = rec["_fact_table_override"]
        n_v = sum(1 for f in facts if f["status"] == "verified")
        rec["stages"]["p2p3_nodes"] = facts
        rec["n_nodes"], rec["n_verified"] = len(facts), n_v
        rec["budget_used"] = 0
        print(f"  [{tag}] using pre-built fact table ({len(facts)} nodes, {n_v} verified)", flush=True)
    else:
        _budget_reset()
        if rec.get("_use_hierarchy"):
            # v17: 层级目录臂 — 逐层 INDEX 分解（成璐 2026-11-09 设计），无限预算。
            # decompose_hierarchy 内部已边拆边核验，直接返回 fact table。
            from s5_hierarchy import decompose_hierarchy
            nodes_all, rounds_log, facts = decompose_hierarchy(question, qid=qid)
            rec["stages"]["p1h_hierarchy"] = rounds_log
            n_v = sum(1 for f in facts if f["status"] == "verified")
            rec["n_nodes"], rec["n_verified"] = len(facts), n_v
            rec["stages"]["p2p3_nodes"] = facts
            rec["budget_used"] = 0
            print(f"  [{tag}] hierarchy P1H+P2/P3 done: {n_v}/{len(facts)} verified", flush=True)
        elif rec.get("_use_state_machine"):
            # v16: 状态机臂 — P1e 探索式分解（多轮回退 + 已确认事实注入）
            nodes_all, rounds_log = decompose_explore(question, qid=qid)
            rec["stages"]["p1e_state_machine"] = rounds_log
            facts = []
            for node in nodes_all:
                node_rec = {"id": node["id"], "claim": node["claim"],
                            "level": node.get("level", "?"),
                            "source": node.get("source", "search"),
                            "search_query": node.get("search_query", "")}
                if node.get("source") in ("given", "knowledge"):
                    node_rec.update(status="verified", evidence="模型先验/题面给定，未触发检索",
                                    corrected_claim=node["claim"])
                    facts.append(node_rec)
                    continue
                srcs, err = search_node(node, qid=qid)
                if err:
                    status, evidence, corrected, raw = ("degraded", f"检索失败: {err}", node["claim"], "")
                else:
                    status, evidence, corrected, raw = verify_node(node, srcs)
                node_rec.update(status=status, evidence=evidence,
                                corrected_claim=corrected or node["claim"])
                facts.append(node_rec)
            n_v = sum(1 for f in facts if f["status"] == "verified")
            rec["n_nodes"], rec["n_verified"] = len(facts), n_v
            rec["stages"]["p2p3_nodes"] = facts
            rec["budget_used"] = _budget_used["n"]
            print(f"  [{tag}] state-machine P2/P3 done: {n_v}/{len(facts)} verified", flush=True)
        else:
            _run_p1p2p3(rec, tag, question, qid=qid)
            facts = rec["stages"]["p2p3_nodes"]
            n_v = rec["n_verified"]
    # P0: 目录树落盘 — 成璐的项目标准：每个父节点一个文件夹，其子节点清单就是该文件夹的 INDEX.md
    if rec.get("_use_hierarchy"):
        try:
            import os as _os, json as _js
            base = _os.path.join(rec.get("out_path", ".") or ".", "tree", rec.get("tag", "?"))
            # id -> node; parent 关系靠 level 前缀无法恢复，这里用 supports/顺序近似：按 level 分层写
            from collections import defaultdict as _dd
            by_lv = _dd(list)
            for f in facts:
                by_lv[f.get("level", "?")].append(f)
            _os.makedirs(base, exist_ok=True)
            with open(_os.path.join(base, "INDEX.md"), "w") as fi:
                fi.write(f"# {rec.get('tag','?')} 目录树\n\n")
                for lv in sorted(by_lv, key=lambda x: str(x).lstrip("L")):
                    seg = by_lv[lv]
                    fi.write(f"## {lv}（{len(seg)} 条）\n")
                    for f in seg:
                        st = {"verified": "✅", "degraded": "⚠️", "failed": "❌"}.get(f["status"], "?")
                        fi.write(f"- [{f['id']}]{st} {f['corrected_claim']}\n")
            print(f"  [{rec.get('tag')}] tree written to {base}/INDEX.md ({len(facts)} entries)", flush=True)
        except Exception as e:
            print(f"  [{rec.get('tag')}] tree write failed: {e}", flush=True)
    # P4
    table = "\n".join(
        f"{f['id']}: {f['corrected_claim']}  [status={f['status']}; evidence: {f['evidence'][:120]}]"
        for f in facts)
    prompt = P4_SYNTHESIZE.format(question=question, fact_table=table) + _perturb()
    # v17 无限预算：fact table 巨大时单次 8000 token 输出不够，按层分段合成再合并
    if rec.get("_use_hierarchy") and len(facts) > 200:
        from collections import defaultdict as _dd
        by_lv = _dd(list)
        for f in facts:
            by_lv[f.get("level", "?")].append(f)
        parts = []
        for lv in sorted(by_lv, key=lambda x: str(x).lstrip("L")):
            seg = "\n".join(
                f"{f['id']} ({lv}): {f['corrected_claim']}  [status={f['status']}; evidence: {f['evidence'][:80]}]"
                for f in by_lv[lv])
            p = (f"你是研究员。基于下面第 {lv} 层的已核验事实，回答原问题中该层涉及的部分。"
                 f"只写结论+数值/公式，每条标来源条目 id，不要重复其他层的内容。\n\n"
                 f"【问题】\n{question}\n\n【第 {lv} 层事实】\n{seg}") + _perturb()
            out_l, _ = call_llm(p, max_tokens=4000, temperature=0.7, top_p=0.95)
            parts.append(f"=== 第 {lv} 层 ===\n{out_l or '(空)'}")
        merge_p = (f"你是研究员。下面是同一道问题按目录树分层得到的各层结论摘要。"
                   f"请把它们合并成一份完整最终答案：覆盖问题全部子问，保留所有具体数值/公式/排序，"
                   f"消除层间重复，最后给一个明确的推荐结论。\n\n【问题】\n{question}\n\n"
                   + "\n\n".join(parts)) + _perturb()
        answer, usage = call_llm(merge_p, max_tokens=8000, temperature=0.7, top_p=0.95)
        print(f"  [{rec.get('tag')}] hierarchy segmented synthesis: {len(facts)} facts, {len(parts)} layers", flush=True)
    else:
        answer, usage = call_llm(prompt, max_tokens=8000, temperature=0.7, top_p=0.95)
    rec["answer"] = answer or ""
    rec["label_stats"] = _label_stats(answer or "")
    rec["usage"] = usage
    rec["wall_s"] = round(time.time() - t0, 1)
    rec["n_verified"] = n_v
    rec["n_nodes"] = len(facts)
    # Judge (binary coverage, same rubric as S0-A4 — comparable across arms)
    j = judge(qid, answer)
    rec["judge"] = j
    cov = round(j.get("coverage") or 0, 3)
    # Depth-continuous score (judge_v2_depth, k·ln(k+1) weighting) — finer resolution
    try:
        dv = score_run(qid, answer)
        rec["depth_score"] = dv.get("overall")
    except Exception as e:
        rec["depth_score"] = None
        print(f"  [{tag}] depth-score failed: {e}", flush=True)
    print(f"  [{tag}] P4+J: cov={cov} depth={rec['depth_score']} labels={rec['label_stats']['n_labels']}/{rec['label_stats']['n_numeric_claims']} nums unverified={j.get('unverified_count')} wall={rec['wall_s']}s", flush=True)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qs", default="nat,soc")
    ap.add_argument("--reps", type=int, default=2)
    ap.add_argument("--out", default="runs-s5")
    ap.add_argument("--start-rep", type=int, default=1)
    ap.add_argument("--workers", type=int, default=1,
                    help="concurrent workers (default 1; use 2-3 for parallel)")
    ap.add_argument("--state-machine", action="store_true",
                    help="v16: P1e exploratory decomposition loop (multi-round backtracking + confirmed-fact injection)")
    ap.add_argument("--hierarchy", action="store_true",
                    help="v17: per-layer INDEX decomposition, unlimited budget (Chenglu 2026-11-09 design)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    qs = args.qs.split(",")
    os.makedirs(args.out, exist_ok=True)
    out_f = open(f"{args.out}/run.log", "a")
    t0 = time.time()

    # Build work list: (qid, rep, tag, fp)
    tasks = []
    for qid in qs:
        for rep in range(args.start_rep, args.reps + 1):
            tag = f"S5-{qid}-r{rep}"
            fp = f"{args.out}/{tag}.json"
            if os.path.exists(fp):
                continue  # skip completed
            tasks.append((qid, rep, tag, fp))

    total = len(tasks)
    print(f"S5 PIPELINE: {total} tasks, {args.workers} workers, qs={qs}", flush=True)
    if total == 0:
        print("S5 PIPELINE DONE (all cached)", flush=True)
        return

    done = 0
    lock = __import__("threading").Lock()

    def _worker(qid, rep, tag, fp):
        nonlocal done
        if getattr(args, "hierarchy", False) and not args.dry_run:
            # v17 hierarchical arm: per-layer INDEX decomposition (unlimited budget)
            rec2 = {"tag": tag, "arm": "S5-hier", "qid": qid, "rep": rep,
                    "model": LLM_MODEL, "ts": datetime.now(timezone.utc).isoformat(),
                    "stages": {}, "_use_hierarchy": True, "out_path": args.out}
            r = run_one(qid, rep, dry_run=False, rec_override=rec2)
        elif getattr(args, "state_machine", False) and not args.dry_run:
            # v16 state-machine arm: P1e loop (rec carries the flag)
            rec2 = {"tag": tag, "arm": "S5-sm", "qid": qid, "rep": rep,
                    "model": LLM_MODEL, "ts": datetime.now(timezone.utc).isoformat(),
                    "stages": {}, "_use_state_machine": True}
            r = run_one(qid, rep, dry_run=False, rec_override=rec2)
        else:
            r = run_one(qid, rep, args.dry_run)
        with open(fp, "w") as f:
            json.dump(r, f, ensure_ascii=False, indent=1)
        with lock:
            done += 1
            line = {"tag": tag, "ok": "error" not in r,
                    "cov": round((r.get("judge") or {}).get("coverage") or 0, 3),
                    "depth": r.get("depth_score"),
                    "n_verified": r.get("n_verified"), "wall_s": r.get("wall_s")}
            print(f"[{done}/{total}] {line} ({time.time()-t0:.0f}s)", flush=True)
            out_f.write(json.dumps(line, ensure_ascii=False) + "\n"); out_f.flush()

    if args.workers <= 1:
        # serial path (original behavior)
        for qid, rep, tag, fp in tasks:
            _worker(qid, rep, tag, fp)
    else:
        # parallel path
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {pool.submit(_worker, qid, rep, tag, fp): tag
                       for qid, rep, tag, fp in tasks}
            for fut in as_completed(futures):
                try:
                    fut.result()
                except Exception as e:
                    tag = futures[fut]
                    print(f"ERROR {tag}: {e}", flush=True)
                    with lock:
                        done += 1
    print("S5 PIPELINE DONE", flush=True)


if __name__ == "__main__":
    random.seed()
    main()