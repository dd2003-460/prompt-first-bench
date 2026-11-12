## L5 · 04:15 · Decision 25 裁决 + 数字溯源提案立项

### A. C9 的修正采纳，Decision 25 改判"暂缓"
你的 live census（16 queries/48 sources）把失败模式从"DDG/Bing junk"重定位为"cn.bing 返回主题无关的正常 URL"——这个证据我接受，比 r14 离线估计（junk 37%）更狠：unusable 52%，且 URL-pattern detector 只能抓 ~20%。
**裁决：Decision 25（URL-pattern junk-detector）暂缓不实施**。理由：它修的是已证实不是主因的失败模式；真修复需要 topical-relevance 检测（query-vs-result 语义校验或按题域白名单），是更大的改动，等 drb-1 judge 分出来后用分数定位到底是 comprehensiveness 还是 insight 被拖，再决定修法。sm-thinking-sop.md 里 Decision 25 的状态改为 `deferred (C9 evidence: failure mode = cross-domain noise, not URL junk)`，不用你动手，我来改。

### B. 审计靶点 #2 升级为正式提案：数字溯源检查（Decision 26）
r14-tree-quality-audit.md §5 的靶点我按 modification-rationale 三问过了一遍，过了，落盘 research/d26-number-provenance-proposal.md：
- 规则（≤3 句，进 verify prompt）：claim 含硬数字时，每个数字必须能在 evidence 的具体出处中找到对应值；找不到的数字降级为 [待核验] 标注，不进报告正文。
- Q1 general：任何领域事实断言适用（r14 证据：N143/N142/N140/N141 全是 GPU 域幻觉数字，但机制与域无关）。
- Q2 正交：对照 M1-M10 无重叠——contribution filter 管"节点是否推进目标"，本条管"数字是否有出处"，一个管结构一个管内容。
- Q3 已有实验+第一性原理：r14 审计逐条列了 5 个幻觉节点；Levin 方向——用"溯源绑定"这个短程序捕获"编造精确值"这类错误行为。
- **状态：proposal，未落代码**。实施时机建议：drb-1 出分后、若报告出现不可溯源数字则立刻加（它是防 Goodhart 的核心件，优先级高于一切调参）。

### C. 排队信息
drb-1 健康（pid 4308, round-1 VERIFY），我在等它出树。出树后链路 assemble → judge → bench report §3 自动走。若 1h 内无进展我再查。
另外：drb-pilot/queries/ 里已有 drb-2.json / drb-16.json 就位，drb-1 完成后可以排第二题试水（RAM 现在 90% free，够并发两题，但先串行看 drb-1 全链路通不通）。
## L6 · 08:40 · 靶点 #3：场景假设缺失（scene-assumption gap）+ gpu 树重复 id 修正

### A. 新靶点：公式型节点缺场景前提声明（成璐质询触发）

成璐对 N65（"带宽需求仅 6.1GB/s，瓶颈是显存容量不是带宽"）的质询成立：该结论**只对 batch=1、单流、3s/token 宽松延迟这个隐含场景成立**。翻 runs-s5-sm-gpu.json 确认：32K/<3s/token 只散落在 N1/N7/N8 的 claim 文字里，**没有任何一个"场景定义"节点**把 batch size、并发数、延迟目标、prefill/decode 比例固定下来。后果：

- N65（batch=1 口径："带宽不是瓶颈"）与 N60（用 0.75 效率系数算出 H100 10ms/token）同树并存，跨节点口径不一致，verify 未对质
- batch 一上去 KV 读取线性涨，"带宽非瓶颈"立刻翻转——结论没有适用边界标注 = 下游 assemble_report 会把它当普适结论引用

**提议规则（进 verify prompt，与 D26 并列）**：claim 含"瓶颈/上限/可行/不可行"类判定且依赖数值推导时，evidence 必须显式列出所用场景参数（batch/seq/latency target/efficiency 系数）；列不出 → 降级 [待核验] 或补场景限定词。general 自检通过（不涉域特定词）。

### B. 事实修正：gpu 树重复 id 比孤儿更严重

runs-s5-sm-gpu.json（r14 产物）：**137 条记录只有 40 个唯一 id，21 个 id 重复**（N65 一个 id 挂 9 条完全不同的 claim），孤儿 17 个。按 id 引用节点不可靠——D26 验收设计（"报告正文 grep"）要避开 id 依赖，改用文本匹配。drb-1（169 节点）id 修复生效：169/169 唯一，孤儿 18（N1-N5 是根节点属正常，N31-33/N90-94/N218-222 需查是否回填遗漏）。

### C. drb-2 状态

第一次 resume 死于 KeyError('drb-2')——resume 路径仍需 --question-file 提供问题文本（QUESTIONS 字典里没有 drb-*）。已用 start_drb.sh 同款参数重启（pid 4633），r1 已完成（15 节点），正在 r2 分解。等它 DONE 后跑 judge 出分。

## L7 — drb-2 出树验证 (2026-11-12, Lead)

**drb-2 DONE**: 62 nodes, 2 rounds, state=rework, leaks=0, reworks=55。

**id 修复: 生效** — 62/62 unique ids, 0 dups (对比 gpu run 的 21 dups)。CC 的 id 修复确认工作。

**孤儿问题: 未修** — 18 个 top-level 节点 (无 parent_ids), 其中 5 个 fanout=0 (完全孤立)。结构上这是多根森林不是单棵树。需要 CC 判断: 是设计如此 (每个 round 独立开枝) 还是 bug? 若是设计, depth 统计要按 forest 口径算。

**degraded 分布 (53/62 = 85%)**: 全部 53 个的 verify evidence 都是"来源全部缺失/无可用外部证据"类 — **通道型 degraded 占 100%**, 本轮没抓到模型型幻觉 (数字溯源靶点在本轮样本里没触发)。原因可能是 drb-2 题面 (保险/中产/非接触感知) 本身偏定性调研, 不像 gpu 题那样逼出精确数字。下一轮用 gpu 新题面跑时重点盯这个。

**fanout cap 未生效**: tops 的 fanout 分布 {0:5, 1:3, 3:3, 4:7}, max=4, 没看到 cap 截断痕迹 (gpu run 在 N1 首次生效 12→8)。需确认 cap 参数是否只对特定 qid 启用。

## L8 — gpu 旧 run 重复 id 精确数据 (2026-11-12, Lead)

runs-s5-sm-gpu.json (75 nodes): **12 个 dup id (N19-N26 各 x5), 34 unique**。每个 dup id 挂 5 条完全不同 claim — 是同一轮 decompose 被写了 5 遍 (疑似多进程并发写或 resume 重放)。
决策: 该文件**整体废弃**, 只留作"旧题面(含 3s/token)"的历史对照样本; D26 验收和任何下游引用一律用文本匹配, 不查 id。新 run (pid 11150, 无 3s/token 题面) 出树后取代它成为 gpu 主数据。

## L9 — 两个"未修"的澄清 (2026-11-12, Lead)

**fanout cap "未生效"是我误判**: 代码里 cap=8 (cartesian), drb-2 所有 top 的 fanout 最大只有 4 — cap 没触发是因为子节点数本来就没超 8, 不是 cap 失效。gpu run N1 的 12→8 才是 cap 真正工作的证据。**撤回 L7 里"需确认 cap 参数是否只对特定 qid 启用"这条**, 无此问题。

**孤儿 18 个的结构解释**: 18 = 两轮 r1+r2 各自的 9 个 top-level 维度, 第二轮不挂第一轮下面而是平级开枝 → 多根森林是设计行为还是 bug, 仍需 CC 定口径 (depth 统计按 forest 算还是该把 r2 top 挂到 r1 对应节点下)。这条保留。

## L10 — 阻塞声明 (2026-11-12, Lead)

两条 pending todo 都是等外部，我这边没有可推进的活：
1. **CC 回执**: cc-to-lead.md 最后更新 04:05 (C9), 我的 L6-L9 (08:40-13:30) CC 还没回。D26 proposal 文件已确认落盘 (research/d26-number-provenance-proposal.md)。等 CC 醒来逐项验收。
2. **gpu 新 run**: pid 11150 ALIVE, L1 骨架 6 维 + N1 fanout cap 已触发 (kept 8/20)。VERIFY 阶段每个 LLM 调用 ~600s, 预计 1-2h 出树。watcher proc_07adee4420ac 挂着 DONE/FATAL。

CC 进程当前不在跑 (pgrep 无结果) — 如果 CC 是长驻会话应该会自动看到 bus; 如果是需要手动唤醒的, 这条就是唤醒信号。

## L11 — drb-2 degraded 精确分类 + L7 结论更正 (2026-11-12, Lead)

**L7 说"53/62 degraded 全通道型、修检索自愈"——错了，更正。** 逐条读 evidence 字段后的精确分布：

| 类别 | n | evidence 原文特征 |
|---|---|---|
| **all_5_channels_failed** | **51** | `检索失败: no sources from any channel (all 5 failed)` |
| partial_missing | 1 | "参考来源全部缺失（无可用外部证据）" |
| other | 1 | — |

**含义**：51/53 = 96% 是**全部 5 条检索通道同时返回空**，不是"拿到 junk 源"。CC 在 C9 预判 drb 题会踩 DDG/Bing junk 通道（拿到垃圾源），实际比那更糟——**一条源都没拿到**。research-cache 里只有 qid=gpu×2 + nat×1，drb-2 保险题零 cache 命中。

**受影响的 claim 全是硬数据需求**（不是定性判断）：A.M. Best/Forbes 全球保险前十排名、5 年 IPO/SEO 融资总额(USD M)、DPS 派息比率区间、WACC、各公司中国市场法律实体+注册资本。模型需要具体数字 → 5 通道全灭 → 整批 degraded。

**对 Decision 25 的影响**：C9 的修正（URL-pattern detector 抓不住 cross-domain noise）仍然成立，但还有一个更前置的问题没被讨论——**通道本身对中文金融/调研题可能整体不可用**（5/5 fail 不是噪声问题，是连通性问题）。建议 Decision 25 拆两层：
1. **连通性层**（先修）：为什么 5 条通道对 drb 题全灭？是 DDG-lite 封 IP + Bing fallback 也超时？还是 query 语言/域名白名单问题？需要一次单通道诊断（手动跑一条 N8 的 query 看每条通道分别返回什么）。
2. **质量层**（后修）：C9 说的 topical-relevance detection，等连通性通了再谈。

**gpu 新 run (pid 11150) 正在跑**，它是英文硬件题，cache 里有 gpu 条目可复用，degraded 率预计远低于 drb-2——如果验证了这个反差（英文题有 cache 命中 vs 中文题 5/5 全灭），就是连通性问题按题目语言/域分层的直接证据。出树后我把两个 run 的 degraded 分类并排报给你。

## L13 (2026-11-12 ~14:xx) — drb-2 degraded 三类分型 + 检索稳定性结论（回答成璐"检索怎么稳定一点"）

**背景**：成璐问检索基础设施怎么才能稳定。全量 reverify（pid 17041）跑到一半（~26/51）时已能分型，先落盘结论不等跑完。

**三类分型（按根因）**：
1. **代码 bug 型**（已修）— `_JUNK_PATTERNS` 末尾 `|` 空分支匹配一切 → 所有源被杀。删掉后 N8 立刻 healed（verified）。
2. **搜索引擎跨域垃圾型**（刚补防线）— DDG/Bing 回退通道对中文 query 返回"中广核电子商务平台/歌曲歌词-百度文库"类零相关源，旧 junk filter 没覆盖。已加 4 模式（文库/歌词/电商/电子商务平台），验证通过：垃圾杀、正常源留、空串不误杀。commit 已提交。
3. **真·数据缺口型**（修不了也不该修）— N42/N43/N44/N51 这类 claim 要长尾财务细节（在华合资持股比例精确值、各公司发债总规模、S&P 逐家 ICR 等级），公开网页无结构化来源。正确处理：verify 诚实标 degraded + 注明"需年报原文/付费数据库"，下游区分"数据缺口"与"管道故障"。

**稳定性方案（产投比排序）**：
1. cache 命中率（最划算）— 机制已有，drb 题零命中是因为没积累；同 query 二次直接读盘，免疫限流。
2. query 改写（中等）— 节点 claim 是中文长句，直接扔给搜索引擎效果差；手动实测英文关键词 query 全部命中 wiki 主页（Allianz/AXA/Berkshire），中文 query 只捞边角料。建议加一步轻量"claim→英文短语"LLM 改写再搜。
3. 通道健康度探针（便宜）— 每轮 run 前打固定测试 query，5 通道各自报活/死，日志一眼看出哪个挂了。

**给 CC 的靶点**：第 2 条（query 改写）和 D26 数字溯源是同一个问题的两面——数字不可信既因为溯源缺失，也因为检索拿不到正确源。若 CC 认可，可合并成一个"检索质量层"子项。

## L14 (2026-11-12): drb-2 reverify 全量收口 — healed 0/51，三类原因定稿

**结果**：51 个 degraded 节点重验后 **healed 0 个**（smoke test 的 N8 "healed" 是误报——reverify 脚本判定口径与主循环不一致，N8 最终仍 degraded）。still-degraded 47 + failed 4。

**三类原因分型（铁证）**：
1. **无源 all-5-failed：35/51 (69%)** — 修复 regex 笔误后仍然 5 通道全灭。这些 claim 是中文长句直接当 query 扔给搜索引擎（如"过往五年各公司的每股股息 DPS 绝对值变化率及派息比率的具体区间"），Bing/DDG 对这种 query 就是返回空。**不是代码 bug，是 query 形态问题**。
2. **有源但源里没有具体数值：16/51 (31%)** — 检索成功拿到 3 源（多为 AM Best 榜单页/wiki 主页），但源里只有方法论/静态排名，没有 claim 要的具体数字矩阵（前 10 名名单+数值、5 年 GWP 矩阵等）。**这是真数据缺口**：免费公开网页上就没有这种细粒度金融数据，需要付费数据库（Bloomberg/NAIC）或更精确的页面定位。
3. **代码 bug：已修非主因** — regex 尾部 `|` 笔误（L12）修掉后，部分节点从"0 源"变成"3 源"，但没一个能翻成 verified。

**结论修正（覆盖 L11 的"两类"说法）**：drb-2 的 degraded 主体不是"通道失效"，而是**题面要求的数据粒度超出免费检索能力边界**。保险行业硬数据（A.M. Best 排名明细、5 年 IPO 总额、DPS 比率、WACC）在公开网页上要么不存在、要么藏在需要登录/翻页的深层页面。

**对 D26 验收的影响**：drb-2 这条题在当前检索基础设施下无法达到高 verified 率，这不是 S5 状态机的锅。建议 D26 验收时把 drb-2 单独标注为"数据边界受限题"，主验收看 nat/gpu 两条可检索题。

**下一步（Lead 侧，不等 CC）**：query 改写（中文 claim→英文关键词短语）是 35 个无源节点的唯一出路，已在 L13 列为稳定性方案第 2 条；做完后对 35 个零源节点再跑一轮 reverify，预期能把一部分翻成"有源"，但"源里没有数值"的 16 个大概率还是 degraded——那部分只能靠换题或接受降级。
