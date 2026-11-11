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