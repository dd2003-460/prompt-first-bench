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
