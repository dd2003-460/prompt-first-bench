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
