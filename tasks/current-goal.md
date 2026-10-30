# Goal: RV3G6-o3-claim-list-erratum-27 — §3.2 声明 4「27/98」数字勘误备料（三口径对照，不代裁）

> 创建：2026-10-30 · ralph loop runner（queue 消费——r142 导出项，纯仓库内备料型工作）
> 依据：r142 (RV3G6-o3-claim-rejudge-evidence-audit) A4 节独立复算发现 o3-claim-list.md §3.2 口径声明 4「已核：98 个 h=1 cell 中 **27** 个 evidence 含 gold-tree 数值 token」三口径均 ≠ 27（V1 per-line−豁免=13 / V2 全文件−同豁免=34 / V3 per-line 无豁免=35）。27 为起草期不可复现人工计数，结论方向不受影响（机制论证对任一计数成立），仅数字失实。
> 边界：同 RV3B1-jaccard-adjudicate / RV3G6-kappa-formula-adjudicate 先例——**runner 只备三方案对照材料 + 裁定后执行清单，最终裁定权在成璐，不代裁**。冻结件 o3-claim-list.md 零触碰（§6 红线：修改需 APPROVALS 登记 + 成璐裁定改法）。

## 【目标】
落盘 `bench/rubric-v3/o3-claim-list-erratum-27-materials.md`：(a) 事实链溯源（r142 A4 三口径表 byte-exact 引用 + assert-hitmatrix-evidence.py V1 口径实现锚点）；(b) 三方案对照表——A 直接改 13（V1 口径，与 assert 脚本同源最可复现）/ B 三口径并列呈现（13/34/35 + 各口径定义，信息最全但改动面大）/ C 删具体数字只留机制表述（「部分 evidence 含 gold-tree 数值 token」+ 指向 assert 脚本机判路径，最保守）；(c) 推荐排序 + 理由（产投比/可复现性/改动面三维）；(d) 裁定后执行清单（每方案的精确 diff 位置：o3-claim-list.md §3.2 L? 行号 + revision-log 条目模板 + APPROVALS 登记模板）。

## 【阶段】
01 分解 → 02 研究（o3-claim-list.md §3.2 原文精读 + r142 A4 材料复核 + assert-hitmatrix-evidence.py V1 口径代码锚点）→ 02.5 交叉核对（三口径数字独立复算验证 + 与 assert-o3-claim-list.py 黑名单 38 token 一致性）→ 03 行动分解 → 04 执行验证（材料文档落盘 + 数字复算断言）→ 04.5 反方复核

## 【SOP 索引】
- `loop/prompt-first/01..04.5` + `sop/arena-loop-pipeline.md`
- 事实源（只读冻结）：`ablation/o3-claim-list.md` §3.2 口径声明 4 / `ablation/hit-matrix.json` / `ablation/runs-C0-run1..8.md`
- 前序工件（只读）：`loop-artifacts/stages/04/RV3G6o3ea-execution-verification.md` A4 节（三口径表 + V1 全 13 例清单）
- 同源脚本（只读）：`ablation/scripts/assert-hitmatrix-evidence.py`（V1 口径实现）/ `ablation/scripts/assert-o3-claim-list.py`（gold-token 黑名单 38 token 同源）
- 备料模式先例：`bench/rubric-v3/jaccard-m5-adjudication-materials.md`（格式参照）

## 【验收标准】
- [ ] o3-claim-list-erratum-27-materials.md 落盘（六节：事实链/三方案对照/推荐+理由/裁定后执行清单/边界声明/冻结声明）
- [ ] 三口径数字独立复算（13/34/35 或发现新 mismatch 如实登记）——用 assert-hitmatrix-evidence.py 既有 V1 口径 + 自写临时脚本算 V2/V3，不落盘临时脚本到 bench/
- [ ] 三方案各自给出 o3-claim-list.md 的精确行号定位 + diff 预览
- [ ] 冻结件零修改（git status 验证）
- [ ] 04.5 verdict pass；queue 更新（本 goal 标 `[~]` 待成璐裁定，同 jaccard-adjudicate 惯例——不划掉）

## 【失败降级】
- 若独立复算与 r142 A4 数字不一致 → 以本次复算为准并登记差异来源（不静默采用 r142 数字）
- 若 o3-claim-list.md §3.2 行号定位困难（多版本并存）→ 以 git HEAD main 版本为准，标注 commit hash