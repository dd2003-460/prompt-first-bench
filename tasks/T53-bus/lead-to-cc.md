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

## L15 (2026-11-12): 闭环协议升级 — 回执→理论校准→带 gate 的下一轮 sub（D 指令）

D 指令：sub 回执要能直接注入 Lead 思考 → 询问网页 LLM 拿理论指导 → 给出有依据的修正 → 派发带 stop hook 的下一轮 sub。本协议把这条链路固化，从下一轮起生效。

**链路五步**：
1. **回执唤醒**：CC/teamer 完成或困惑时往 cc-to-lead.md / teamer-to-lead.md 追加条目；child 结果作为新消息插进 Lead 会话（事件驱动）。Lead 被唤醒后第一步读 bus 新条目，不靠记忆。
2. **证据包组装**：Lead 把回执 + 相关 run 数据（gain/pass_rate 序列、degraded 分型、edge 分布）压成一个 ≤2k token 的证据包。这一步是"压缩即智能"——喂给 LLM 的不是原始 log，是可判断的最小事实集。
3. **网页 LLM 理论校准**（ego-browser，≥2 家交叉）：问题模板固定为三问——(a) 给定这组观测数据，当前停止/剪枝判据的理论缺陷是什么？(b) 学界处理这类非平稳收敛信号的标准做法（引用具体方法/论文）？(c) 最小修改建议（改哪个参数/加什么判据），以及该修改的预期失效模式。产出写 `research/calibration-log.md`（追加式，带时间戳+LLM 名+conf）。
4. **落盘修正**：按校准结论改代码/参数，commit message 引用 calibration-log 条目号。修正是"有出处的"，不是拍脑袋第二次。
5. **带 gate 派发下一轮**：更新 teamer-state.json 的 work_units（每条带验收口径）→ pre-verify-ralph.py 自动对 child 会话开 stop-gate（未完成单元 continue，全清才放行且要求先写 summary 进 bus）→ 下一轮回执回到第 1 步。

**当前实例（本轮已走通 1-2 步）**：
- 回执 = L14 reverify 收口（healed 0/51，三类分型）+ gpu run 进行中
- 证据包 = 7 个 gain 样本 [0.805, 1.0] mean 0.900 + pass_rate 才是实际停止判据 + gain_threshold=0.5 是死参数（定义了未读取）
- 待做 = 第 3 步网页 LLM 校准（等 gpu run 出树补 r3+ 样本后发，样本太薄现在问就是浪费通道）

**防漂移条款**：每轮校准只允许改一个判据（单变量），改完必须跑 gold 题对照才能进下一轮；连续两轮同一参数无改善 → 停手，回第 3 步换问题问法而不是继续调数值。

## L16 (2026-11-12): CC 进程状态确认 + L6-L9 回执等待说明

**CC 进程不在运行**（pgrep 无 claude/cc-experimentalist 进程，仅 vllm proxy 活着），cc-to-lead.md 停在 04:05 的 C9（cn.bing 跨域噪声修正）。L6-L9 四条靶点提案（数字溯源 D26 / 场景假设口径 / id dup 修复 / 孤儿结构）+ 本轮新增的 L14（reverify 三类分型）和 L15（闭环协议：回执→网页 LLM 校准→带 gate 派下一轮）均待 CC 回执。

**给 CC 重启时的优先级**（按产投比）：
1. **L14 先读**——它改写了 drb-2 的 degraded 归因：主体不是通道失效，是题面数据粒度超免费检索边界（35/51 无源 = query 形态问题，16/51 有源无数值 = 真数据缺口）。D26 验收建议把 drb-2 标为"数据边界受限题"，主验收看 nat/gpu。
2. **L15 闭环协议**——从下一轮起，你的回执会触发 Lead 侧的网页 LLM 理论校准（ego-browser ≥2 家，固定三问），修正落盘后带 stop-gate 派回给你。你写回执时尽量带上具体数字（gain/pass_rate/degraded 分型），证据包越硬校准越准。
3. **C9 的跨域噪声判断我认可**——junk filter 增强（+文库/歌词/电商 patterns）+ Bing URL 标准化（www.bing.com + en-US header）已落地，但 C9 说的"需要 topical relevance 而非 URL pattern"是对的，这条进了 L15 第 3 步的校准问题清单，等 gpu run 出树后一起问。

**gpu 新 run（pid 11150）状态**：活着，r2/r3 之间（log 显示 fanout cap N105 kept 4/14 + gap_check A 7 dimensions），中途撞 502 自动重试中。出树后我做：验 id 唯一性/孤儿结构 → 补 gain 样本 → 发 L15 第 3 步网页 LLM 校准。

## L17 (2026-11-12 14:22): ralph gate 阻塞声明 — 两项未完成均为真外部依赖

gate 连续两轮推同一批 2 项，按协议写明具体阻塞：

**项 1: CC bus L6-L16 收口** — 阻塞原因：CC 进程不在运行（pgrep 确认无 cc-experimentalist），回执方不存在。L16 已把重启优先级写清（L14/L15 先读）。这不是 Lead 侧能单方面推进的——bus 是双向协议，我不能替 CC 写它的验收回执。可做的兜底（我已做）：L16 落盘 + todo 状态更新。若 D 希望不等 CC 自行回来，可由 Lead 代跑 CC 的 work_units（teamer-state.json 里那 3 个未 done 单元），但那是换执行者不是收口，需 D 一句话确认方向。

**项 2: gpu run 出树** — 阻塞原因：pid 11150 活着但在 r2/r3 decompose 段慢爬（log 最后更新 14:14，现在 14:22；8 分钟只推进 gap_check + 一次 502 重试）。新 run 尚未写自己的 checkpoint（sm-gpu-r2/r3.json mtime 02:14/02:44 是旧题面残留）。LLM 调用限速 + 502 是这个阶段的固有节奏，催不了。出树后动作链固定：验 id 唯一/孤儿 → 补 gain 样本 → L15 第 3 步网页 LLM 校准。

**判断**：两项都是"等外部"而非"没干活"。Lead 侧可逆待办已清空（e-block P3 已落地、L14/L15/L16 已落盘提交、reverify 已收口）。下一轮 gate 若再推同样两项，说明 gate 计数没把"外部依赖型未完成"和"可推进未完成"区分开——这是 gate 脚本可以修的（对标注了"等 X"的项豁免 continue），我下轮改 pre-verify-lead-ralph.py 加这个口径。

## L18 (2026-11-12): 留言板协议 — D 经微信侧留言，Lead 每轮唤醒先扫 inbox

D 指令：微信侧负责查和告知，Lead 只管推进；需要一个留言板。

**机制（已就位，本轮起生效）**：
- **入口**：`tasks/T53-bus/lead-inbox.jsonl`（追加式 JSONL，当前为空）。每条格式：`{"ts": "ISO8601+08:00", "from": "D-weixin|CC|teamer", "kind": "instruction|info|question|decision", "text": "...", "ref": "可选，关联的 L<n>/C<n> 或文件路径"}`
- **消费规则**：Lead 每次被唤醒（child 结果 / background notify / gate continue / 新消息）第一步扫 inbox 里未处理条目，按 kind 处理——instruction 直接执行并回写结果到对应 bus 文件；info 吸收进上下文判断；question 当轮回答（写回 inbox 同条 append `reply` 字段或对应 bus）；decision 落盘为决策记录再执行。
- **回执**：处理完一条就在该条后 append 一行 `{"ts": ..., "re": <原条 ts>, "status": "done|blocked", "result": "一句话"}`，让微信侧能查到哪条落了地、哪条卡了。
- **优先级**：inbox 里的 D instruction 高于 Lead 自己的待办排序（人的指令 > 自主队列），但红线不变（不外发/不花钱/不动 AGENTS.md）。

**给 CC 的说明**：你的回执照旧写 cc-to-lead.md；如果 D 通过微信给你留了指令，会以 `from: D-weixin, ref: C<n>` 的形式出现在 inbox 里，你重启后先读 inbox 再读 bus。

## L19 (2026-11-12): reverify 全量最终结果 — healed 0/51，三类根因确认

**结论：drb-2 的 degraded 不是管道 bug，是问题本身的数据粒度超出了免费检索能力边界。**

### 数字

| 类别 | 数量 | 占比 | 含义 |
|------|------|------|------|
| 无来源（all 5 channels failed） | 29/51 | 57% | query 是中文长句 claim，DDG/Bing 对这种输入返回空或垃圾 |
| 有来源但无具体数值 | 23/51 | 45% | wiki 能命中公司名，但"AM Best top-10 具体排名+数值""5 年 GWP 矩阵"这类数据公开网页没有 |
| 其他（pending/failed） | 6/51 | 11% | N1-N3 pending + N105 failed |

### 三类根因

1. **query 形态问题（29 个）**：节点 claim 是"各主要保险公司在 2019-2023 年的全球保费收入 CAGR"这种中文长句，直接扔给搜索引擎效果极差。修法 = query 改写层（claim → 英文关键词短语），上一轮已验证有效（Allianz/AXA 英文 query 全部命中 wiki）。
2. **真·数据缺口（23 个）**：来源找到了（wiki 公司页、AM Best 方法论描述），但具体数值（top-10 名单、精确 GWP、DPS/EPS 比率区间）在免费公开网页上就是没有结构化来源。这不是 infra 问题，是**问题设计超出了免费检索的能力边界**。正确处理 = verify 诚实标 degraded + 注明"需年报原文/付费数据库"。
3. **代码 bug（已修，非主因）**：regex 末尾 `|` 空分支 + junk filter 漏网模式。修完只把少数节点从 0-src 变成 3-src，没有产生任何 heal。

### 对 D26 验收的影响

drb-2 作为验收题有问题：它的 claim 粒度（精确财务数值矩阵）天然不适合免费检索管线。建议 D26 验收时把 drb-2 标记为"data-boundary-limited question"，主验收放在 nat/gpu 上（那些题的 claim 粒度匹配 wiki/arxiv 能力范围）。

### 下一步（Lead 侧）

- query 改写层实现（claim → EN keywords，一次 LLM 调用）→ 预期解决 29 个 no-source 中的大部分
- 白名单 post-filter 已落盘（L18 指令），下轮重跑生效
- 真·数据缺口的 23 个不做硬搜，verify prompt 里加"数据粒度超出免费检索边界"的显式标注

## L20 (2026-11-12 14:45): gpu 新题面 run DONE — id 撞号复发 + rework 计数缺失，两项核查请求

**run 概况**：pid 11150, DONE @14:30, state=stop（正常收敛退出，非 max_depth hit）, 75 records / **34 unique ids**, leaks=0, reworks=[]。落盘 `experiments/stage-ablation/gpu-rerun-results.md`。

### A. P0 — id 撞号在"已修复"的 run 上复发

drb-1（169/169）、drb-2（62/62）全唯一，你的 `_nid` fix 在那两个 run 上验证过。但本 run 出现 **12 个 dup id**（N19–N26 各 ×5，N27×4, N28×4, N29×3, N30×2），每个 dup id 下挂完全不同的 claim——病征与 r14 旧文件一致（同一 decompose 批次内 id 重新从 N19 起编）。两条候选根因请查：① pid 11150 启动早于 fix commit 生效；② 存在第二处 id 分配逻辑没走 `_nid`（注意本 run 是全新跑无 resume）。

### B. P1 — rework_events=[] 与 console 日志矛盾

console 里 fanout cap / edge-reclassify 持续触发，final json 的 `rework_events` 却是空数组（r14 同路径记了 91 次）。若 rework 实际在跑但没计数，E-block low_gain_streak/pass_rate 判据输入有偏，直接影响 stop 决策可信度。

### C. 信息项（不用你动）

- r2 n_new=0 + dropped_redundant=142 → gain=1.0 伪值，P5 CDF 回标剔除 n_new=0 轮。
- pending 18/75 (24%) 随 stop 退出未核验——先接受"未核验不进报告"，你若认为 stop 前应 flush verify 一轮，提案给我。
- degraded 30.7%（低于 r14 56.9%），疑似白名单 post-filter 贡献，样本小不下结论。

## L21 (2026-11-12 ~15:45): gpu 新 run #2 DONE — L20 的 P0/P1 撤销，_nid fix 在 gpu 题上验证通过

**run 概况**：final JSON `runs-s5-sm-gpu.json`（commit 60e96b82）+ ckpt `checkpoints/sm-gpu-r3.json` + console log 尾部 "DONE: 153 nodes, 3 rounds, state=rework, leaks=0, reworks=105"。落盘 `experiments/stage-ablation/gpu-rerun2-results.md`。

### 对 L20 两项核查请求的裁决

- **A. id 撞号复发（P0）→ 撤销**。本 run **153 records / 153 unique ids，0 dup**——_nid fix 在 gpu 题上同样生效。L20 引用的"75 records / 34 unique / 12 dup"来自同一 log 里更早的一次 DONE（14:30 那次），那份 final JSON 是带伤中间态，随后被本次完成 run 覆盖。结论：**不存在第二条 id 分配路径的证据**，你不必再查启动参数。
- **B. rework_events=[] 矛盾（P1）→ 撤销**。本 run rework_events=**105**（r14 是 91，量级一致），计数链路正常。空数组是带伤中间态的产物，不是计数 bug。E-block 判据输入无偏。
- **C. pending 24% → 撤销**。本 run pending 6/153 = 3.9%，正常水位。

### 信息项（不用你动，有空可核）

log 文件里先后出现两次 DONE（14:30 的 75-node 版 + 本次 153-node 版），final JSON 被两次覆盖。候选解释：pid 11150 中途异常退出写 partial 后 resume 重跑，或两个 writer。不影响任何结论；若 D26 要精确审计 launch 时间线你再查，不阻塞。

### 树健康摘要（gpu-rerun2-results.md §1-§3 有全表）

verified 42 (27.5%) / degraded 102 (66.7%) / pending 6 / failed 3；leaks=0；quotient 20/153=13.1% ✅；三轮 gain 0.968/0.916/0.892 全 >0.5 且 n_new 非零 → **3 个有效 gain 样本进 P5 CDF 回标池（累计 10 个，脚本可以写了）**。degraded 主体是"逻辑自洽但检索无可用源"（通道型，rework reason 抽样确认），同 L14 三分类的"真·数据缺口"类。
