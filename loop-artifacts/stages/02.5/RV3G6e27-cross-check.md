# 02.5 — 交叉核对：RV3G6-o3-claim-list-erratum-27

## X1 — 三口径数字独立复算（本 goal 自跑，非引用 r142）

方法：从 hit-matrix.json + gold-tree.md 原始数据重算，token 提取与命中判定逻辑逐行对照 assert-hitmatrix-evidence.py A4 段（L140-154）实现（`re.findall(r"\d+(?:\.\d+)?", evidence)` ∩ blacklist 非空即命中；blacklist = per-line 节点行 token 并集 − noise_exempt）。

| 口径 | 本次复算 | r142 A4 | 一致 |
|------|---------|---------|------|
| V1 (per-line − 豁免) | **13**/98 | 13/98 | ✓ |
| V2 (全文件 − 同豁免) | **34**/98 | 34/98 | ✓ |
| V3 (per-line 无豁免) | **35**/98 | 35/98 | ✓ |

V1 全部 13 例清单（本次复算输出，与 r142 A4「已落盘」清单比对一致）：
run1/N-1.1.1, run1/N-3.2.1, run1/N-3.2.2, run2/N-3.2.1, run2/N-3.2.2, run2/N-5, run3/N-3.2.2, run3/N-5, run4/N-5, run5/N-5, run6/N-3.2.1, run6/N-3.2.3, run7/N-3.2.4。

**注意**：首次复算时我用 `tok in ev`（子串包含）粗判得 V1=46——那是我的临时脚本 bug（'1'/'2' 类短 token 的子串误匹配），改用脚本同源的「evidence 自身 token 集合 ∩ blacklist」后精确复现 13。**教训登记**：备料文档中所有数字必须用与既有 assert 完全同源的判定逻辑复算，禁止手写简化版判定（子串包含 ≠ token 交集）。

## X2 — 下游消费者枚举复核（F3 验证）

grep 全仓（排除 .git/ 与本 goal 工件）「27 个 evidence」/「声明 4」：

- o3-claim-list.md L137（失实处本体）✓ F3 已列
- assert-hitmatrix-evidence.py L26（docstring 描述）+ L151 `declared = 27` 常量 + L152-154 输出文案 ✓ F3 已列——**补充发现**：L26 docstring 也含「27 个」字样，方案 A 执行时需同步 3 处（L26/L151/L154 文案），不是 1 处。已更新裁定后执行清单。
- tasks/goal-queue.md L16/L23（历史完成注记 + 本候选条目）——描述发现过程，不改 ✓
- loop-artifacts/stages/0{2,2.5,4}/RV3G6o3ea-*（r142 历史工件）——审计链保留原始状态，不改 ✓
- 其他零命中 ✓

## X3 — 与 jaccard-m5 备料先例格式对齐性

jaccard-m5-adjudication-materials.md 六节结构：溯源 byte-exact / 关键发现 / 三选项对照表 / 推荐（供消费非裁定）/ 裁定后执行清单 / 边界声明。本 goal 材料按同构组织（02 F1-F5 → 04 落盘的 materials 六节映射：F1=溯源 / F2+F3=关键发现 / F4=三选项对照 / F5=推荐 / 04 内=执行清单 / 04 内=边界声明）✓ 对齐。

## X4 — 预期风险声明

- 若成璐选 B/C，assert 脚本的 declared 常量处置不同：B → declared 改为 13 且注明「机判基准=V1，文中并列值仅历史溯源」；C → declared 机制整体移除（A4 段降级为纯计数报告，不再做 mismatch 对照）。三种改法的脚本侧 diff 均已预写（见 04 执行清单）。
- 勘误落地前，assert-hitmatrix-evidence.py 常态输出 MISMATCH 提示——这是**预期行为**（信号源职责），不因本 goal 收口而改变。