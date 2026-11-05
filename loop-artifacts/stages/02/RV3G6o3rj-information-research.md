# 02 — RV3G6-o3-claim-rejudge-scaffold · 信息研究（仓库内精读）

> goal: claim 级独立重判的仓库内闭环骨架 · 分支 ralph/rv3g6-o3-claim-rejudge-scaffold · 2026-10-30
> 本阶段 = 纯仓库内精读（无外部调研；web-llm 三 provider 登录态失效，r126 登记——如需外部交叉验证则 unverified 降级，不虚构）

## F1 — o3-claim-list.md 可机判化要素提取

| # | 要素 | 冻结件位置 | 对骨架的含义 |
|---|------|-----------|-------------|
| F1.1 | blind-packet 输入边界：判者只见 run 原文 + §2 对应行 claim 文本；不见 gold-tree 全文 / hit-matrix 现值 / 他判者结论 | §4.1「独立性定义」 | protocol D1 必须把该边界写成**逐字段白名单**（blind-packet 结构），否则不可机判 |
| F1.2 | 输出格式：每 cell yes/no + evidence（必须是产出中真实存在的句子，≤40 字惯例沿用 TASK-ablation Step 1） | §2.2「判定操作」+ TASK-ablation L24 | schema 字段：`h_claim ∈ {0,1}` + `evidence ⊆ run 原文子串`（子串性可机判 → 防编造 evidence） |
| F1.3 | M1/M2 口径：M1 = cell 级一致率（全量 248 + gold strict 40 两切片强制并报）；M2 = run 级聚合一致率（per-run 向量完全一致才计 1） | §3.1 | assert 复算公式直接照抄 §3.1 定义式，不发明新口径 |
| F1.4 | identity 锚点：独立执行前 M1/M2 ≡ 1.0；实际读数 = 与 1.0 的偏离量，偏离须按 (node, 方向) 切片逐格报告 | §3.2 口径声明 1/3 | assert 数据齐备分支的输出形态 = 偏离表（flip 清单 + 切片计数），不是单一数字 |
| F1.5 | κ 门禁顺序：先条目层 κ（二值判定一致性质检）→ 过门禁 → 再 §4.2 聚合。**κ 具体计算公式未在冻结件中定义**（§4.3 只给关系与阈值语义） | §4.3 | **UNRESOLVED 登记项 U-K1**：protocol 只引用顺序，不发明公式；导出裁定候选（见 03 A6） |
| F1.6 | S2 限定语叠加：凡引用基于 claim 清单的命中数字，§5.1 限定语 + gmr-criterion-freeze §4 tie-break 限定叠加生效 | §5.1 + §6 规则 4 | protocol 文头必须 byte-exact 引用 §5.1 段落（同 r116 R-06 逐字验证模式） |
| F1.7 | 「在独立重判完成前，本清单只定义判据、不产生任何新的 h 值」 | §4.4 | **本 goal 硬红线**：三件交付物零 h 值生成；assert 数据齐备分支只消费已落盘 judge 结果，不代判 |

## F2 — 既有脚本机制复用评估

| 机制 | 来源 | 可否复用 | 处置 |
|------|------|----------|------|
| 三分支主流程（缺失→SIGNAL exit 0 / schema 违例→ERROR exit 2 / 齐备→verdict exit 0/1） | assert-goldrank-crossdomain.py L235-279 | ✅ 直接对齐 | 本脚本采用同一 exit code 约定（0/1/2），stdout `[SIGNAL]` 前缀义务随 batch2-closure queue 项继承 |
| SIGNAL blocked-on-external 常态输出（不伪造转绿） | r136 kappa-receipt（FAIL 常态）/ r140 crossdomain（SIGNAL 常态） | ✅ 模式对齐 | 本脚本常态 = SIGNAL blocked-on-external exit 0（rejudge 结果 JSON 未落盘 ≠ 门禁失败，区别于 r136 的 FAIL 语义——kappa receipt 是「评分无效声明」，rejudge 结果是「待生产数据」，语义不同故 exit 语义不同，protocol 中显式说明） |
| gold-tree 数值黑名单（防泄漏） | assert-o3-claim-list.py `gold_numbers_per_node()` + `_noise_exempt()` | ⚠️ 作用对象不同 | 原检查对象 = claim 文本（不得含 gold 数值）；本脚本检查对象 = **judge evidence**（不得超出 run 原文）。两者正交：evidence 子串性检查（F1.2）才是本场景的防编造机制；数值黑名单对本场景意义有限（run 原文本身就含数值，evidence 引 run 原文必然含数值）。→ **不复用黑名单，改用子串包含检查**（current-goal 失败降级条款第 2 条触发路径） |
| 节点全集交叉核对（hit-matrix ∩ gold-tree） | assert-o3-claim-list.py `node_ids()` | ✅ 复用逻辑 | sample-plan.json 生成时同样做 hit-matrix 内部一致性 + gold-tree 交叉核对 |

## F3 — 数据结构事实（机算，供 02.5 核对）

从冻结 `hit-matrix.json` 独立复算（python3 现场执行，非引用文档）：

- runs = 8（run1..run8 字典序）；nodes = 31（各 run 节点集一致）；总 cell = 248
- h_id=1 cell = **98**（39.5%）；h_id=0 cell = **150**
- gold strict 切片（GOLD = N-2.1/N-3.2.2/N-2/N-4/N-1.3，与 assert-gmr-recompute.py L13 同源清单）= 5×8 = **40** cell；其中 h_id=1 = **10**（N-3.2.2×6 + N-4×4；N-2.1/N-2/N-1.3 零命中）
- 优先级分层：P0（h_id=0，FM-2 漏判方向优先）= 150 cell；P1（h_id=1）= 98 cell

以上数字与 o3-claim-list §3.2「数据分布注记」逐项一致（98/248 = 39.5% ✓；gold strict h=1 = 10/40 ✓；N-3.2.2×6 + N-4×4 ✓）——正式核对记录落 02.5。