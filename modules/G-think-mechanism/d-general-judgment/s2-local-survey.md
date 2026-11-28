# S2 本地调研盘点：LLM strategic/metacognitive questioning 机制
# origin: ai · 2026-11-28 · 纯本地（未联网）
# 目标：D 式 general 判断 4 维（质疑方向/查前人/找更快/算性价比）——本地已有什么、缺什么、外查什么。
# 依据：m0-general-reasoning-survey.md（M0 报告）+ think-trigger/decomposition.md（T1-T4）+ oood-probe 两份 verdict + D1-persona-align/memory/ + pfb lit-survey 回执。

## 1. 本地已知机制清单

| # | 机制 | 出处文件 | 解决什么 | 不解决什么 |
|---|---|---|---|---|
| M1 | Zero-shot CoT 触发词（"let's think step by step"） | tasks/think-trigger/m0-general-reasoning-survey.md A1 | 把模型推入推理分布（激活已有能力） | 只改条件分布，不产生 strategic 层动作 |
| M2 | Step-Back 抽象升级（先问高层原理再作答） | 同上 A2 | 实例级→原理级检索，泛化程序 | 实测（redteam verdict v2 臂）未把审查顶到"查前人"层 |
| M3 | Least-to-Most / Plan-and-Solve 分解触发 | 同上 A3 | 跨 easy-hard 泛化缺口 | 分解结构本身增益存疑（T24 回执：naive 分解可 hurt） |
| M4 | 注入式解码 AID（阻止早停） | 同上 A4 | 证明"已会但默认不用"可被最小注入翻转 | 需解码层改造，非 prompt/harness 可用 |
| M5 | 输出 schema 约束（证据带 f(参数±Δ)） | 同上 A5 | 逼出已有参数敏感性程序 | 无同构文献（M0 gap-1）；T54 两次实证加规则负收益 |
| M6 | SpARE 知识选择转向（parametric vs contextual） | 同上 A6 | 证明知识选择行为可被外部信号控制 | 白盒残差流 steering，非 prompt-only |
| M7 | 信息增益驱动提问/行动选择（UoT/BALAR, expected MI） | 同上 A7 | 把"要不要贝叶斯更新"变成显式选择目标 | 只覆盖"提问/行动选择"，不含方向质疑与性价比 |
| M8 | T1 stop_hook 反思注入（薄思考检测→注入"general 机制是什么"） | tasks/think-trigger/decomposition.md T1（stage-gate 仓 1b30bc6） | 生产循环里"做多想少"的触发器；已实现+沙箱 5 场景验证 | 触发的是"爬层反思"，非 4 维 strategic 判断；未在生产测自发 [SEARCH] 率 |
| M9 | T2 "接着考虑"两臂实验（general 提示 vs 无） | 同上 T2（exp-results/scores_v2.md） | 证明 27b 在 general 提示下 3/3 爬到机制层+预言力 | 100% 域偏移（爬到混沌域非 D 的 landscape 域）——深度有了，方向判据（flip）全 0 |
| M10 | T4 修脚本打转检测（同报错≥2/同文件打转→general 思考注入） | 同上 T4（stage-gate 仓 7229159） | 卡住时的升级触发；12 生产 session 0 误报 | 触发条件是"卡住"，D 式质疑是先验的、不依赖卡住 |
| M11 | 缺口信号触发器（正则扫防御性语言→反思注入→模型写 [SEARCH]） | experiments/stage-ablation/oood-probe/trigger-verdict-20261128.md | 决定性正：习惯×信息×触发回路成立，查得精准对口 | 只在"模型已说出缺口"后点火；D 式"看到东西就质疑"发生在缺口表述之前，无缺口信号可扫 |
| M12 | 元层习惯注入（v4：质疑方向/查前人/找更快） | experiments/stage-ablation/oood-probe/redteam-inject-verdict-20261128.md | 买到"层次敏感度"（能指出层次错配） | 买不到"自发去查前人"——缺信息前提+触发器；5 臂全没问"M0 调研为何没用" |
| M13 | metacog 两轴测量（metacog 轴=信息状态监控，quality 轴=gold 条件覆盖） | tasks/metacog-main-conference-skeleton-20261123.md | 27b research agent 的 monitoring/repair 分离测量框架（可发表） | 测的是"信息缺口监控"，不是 4 维 strategic 判断的命中率 |
| M14 | 证据缺失时弃答/主动澄清（语义熵+口头置信度 +5 F1） | pfb/experiments/stage-ablation/lit-survey/t24-receipt.md Q-C | 缺证据时行为正确 | 证据误导时失效（GRAB-RAG 63% 复述植入错误）；且是被动响应，非先验质疑 |
| M15 | 分解增益归因：增益来自执行可靠性非规划能力 | 同上 Q-B（Sprague ICLR'25 110 篇元分析） | 校准"planning 注入"类机制的预期上限 | 直接削弱"注入 strategic 习惯能提升判断质量"的假设基础 |

**本地结论一句话**：习惯（M1-M7/M12 可注入）、信息（检索通道）、触发（M8/M10/M11 harness 层）三件套都有本地实证，但全部是"缺口驱动"（先发现缺口→再查），而 D 式 general 判断是"先验驱动"（看到任何东西→下意识过 4 维）。这一差别本地没有任何机制覆盖。

## 2. Gap 清单（要做 4 维 general 判断，本地还缺什么）

1. **4 维 rubric 未定义**：方向/前人/更快/性价比 各维 0/1/2 分档、判据、可测量指标全部空缺（decomposition S1 待办）。没有 rubric 就没有命中率可言。
2. **"先验质疑"的触发信号未知**：M11 触发器依赖模型自己说出的防御性语言；D 式质疑发生在缺口表述之前。本地没有"何时该质疑"的上游信号研究（比如：任何新方向/新实验设计出现即触发 4 维检查？还是某种输出特征？）——这是本 goal 与 M 线的核心分界，本地零覆盖。
3. **"查前人"无自发行为基准**：M12 证明了不查，但没有"给检索工具的 27b 在 agent 循环里会不会自发先搜前人"的正向测量（redteam verdict 路线 A 未执行）。本地缺一个最小可复现的自发检索率 baseline。
4. **"找更快/性价比"两维：机制层空白，但有 2 个相邻锚点**：M0 七个机制 + T 系列全部围绕"想得深/想得对"，没有一条覆盖"让 LLM 自发做成本感知推理"（何时该换更便宜的路径、产投比判断）。M13 的 budget 轴只测 accuracy-under-budget，不测"模型会不会主动选更便宜的解法"。已核相邻锚点（2026-11-28 宽 grep 补查）：① `stage-ablation/decomposition-research-agi-budget.md`（Pareto 预算控制 goal，D 原话"性价比+最快路径"）= 实验设计层，非 LLM 自发判断机制；② `idea53-goal/idea53-study-note-20261125.md` L96 cost-aware 级联分类器 3 篇文献（1008.3742/2110.14256/1710.03368）= "找更快"维的前人方案线索，可作外查起点。
5. **ground truth 标注方案未设计**：4 维判断命中率需要 D 的纠正信号或 LLM-judge 标注（decomposition S3 待办）；本地没有标注协议，也没有 D 纠正信号的结构化台账对接（qanda-ledger 存在但未对齐 4 维口径）。
6. **strategic 层评测无 benchmark**：M0 gap-2 已声明（ARC-AGI 测抽象、知识冲突探针测选择行为，无单一 benchmark 测"strategic 判断成熟度"）；本地 OOD 探针（oood-general-probe）测的是核迁移，不测 4 维判断。

## 3. 需外查的具体问题（可直接执行的检索 query）

1. LLM research agent 何时自发发起文献/前人检索：`"LLM agent" autonomous literature search "prior work" decision when to search` + `self-directed search policy LLM agent when to retrieve`
2. metacognition/uncertainty 触发检索的行为研究（缺口驱动 vs 先验驱动）：`LLM metacognition uncertainty-triggered retrieval "knowing what you don't know" proactive`
3. 成本感知推理/早停（"找更快"维）：`cost-aware reasoning LLM early stopping token budget utility` + `compute-optimal reasoning LLM adaptive effort allocation`
4. 方向质疑/问题重构（"质疑方向"维）：`LLM problem reformulation questioning the question research direction critique`
5. novelty/collision checking 自动化（"查前人"维的工程实现）：`automated novelty check LLM research idea prior art collision detection`
6. research prioritization / opportunity sizing（"性价比"维）：`research prioritization framework "potential impact" "opportunity space" AI-assisted` + `cost-effectiveness reasoning LLM decision making`
7. strategic reasoning benchmark（4 维评测的现成构念）：`strategic reasoning benchmark LLM "level-k" OR "game theory" OR research planning evaluation`
8. 先验怀疑态度可否注入（对照 M12 负结果）：`LLM skepticism prior belief injection "devil's advocate" prompt strategic questioning`

## 4. 检索记录
- 本地 grep：pfb-thinkmech/tasks/（think-trigger、d-general-judgment、metacog skeleton）、D1-persona-align/memory/（objfunc-signal-log、general-thinking-template、d-thinking-mechanism-first-principles、research-thinking-vs-style）、pfb/experiments/stage-ablation/lit-survey/（仅 t24-receipt.md；decomp-prerequisite-survey.jsonl 在 arena agent workspace，本地无副本）。
- 补查（gap-4 修正）：cost-aware/性价比/产投比/Pareto 宽关键词全量 grep 两目录 md，逐一核命中文件性质 → 机制层确无覆盖，但发现 2 个相邻锚点（research-agi-budget goal + idea53 cost-aware 级联文献），已写入 gap-4。
- 注：`pfb/lit-survey/`（任务书所指路径）不存在，实为 `pfb/experiments/stage-ablation/lit-survey/`；65 篇 JSONL 原件不在本地，只有 t24-receipt 摘要可用。
