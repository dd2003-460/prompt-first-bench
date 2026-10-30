# Goal: RV3G6-kappa-formula-adjudicate — U-K1 κ 公式裁定备料（三方案对照，不代裁）

> 创建：2026-10-30 · ralph loop runner（queue 消费——r141 04.5 B4 导出项，纯仓库内备料型工作）
> 依据：o3-claim-list §4.3「条目层 κ 门禁」只给了序关系未给计算公式（U-K1 UNRESOLVED，r141 judge-protocol-batch1.md §4 已登记）；DRAFT v2 R-02/R5 阈值 0.6 的口径绑定悬空。同 RV3B1-jaccard-adjudicate 先例：**runner 只备三方案对照材料 + 裁定后执行清单，最终裁定权在成璐，不代裁**。

## 【目标】
落盘 `bench/rubric-v3/kappa-u1k1-adjudication-materials.md`：(a) U-K1 缺口精确定位（§4.3 原文 byte-exact 引用 + 哪些下游消费者依赖该公式——judge-protocol-batch1.md §4 / assert-kappa-receipt.py method 字段 / DRAFT v2 R-02/R5 阈值 0.6）；(b) 三候选公式对照表（Cohen's κ / Fleiss'κ / pairwise 平均 Cohen's κ），逐方案给出：定义式、N=3 判者下的适用性（Cohen's 为二判者指标——N=3 时是否适用/如何降级）、条目粒度选项（单 node 跨判者 vs 跨 cell 全量）、与 0.6 阈值的口径绑定方式、计算成本与可机判性；(c) 推荐排序 + 折中出口（如降为 SIGNAL）+ **裁定后执行清单**（回填 judge-protocol-batch1.md §4 UNRESOLVED 标记的具体 diff 面 + assert-kappa-receipt.py method 字段约束收紧点）。裁定前冻结件零触碰。

**范围定位**：纯仓库内文本/数学工作（读 o3-claim-list §4 + DRAFT v2 R-02/R5 + assert-kappa-receipt.py schema + r141 protocol §4，零外部依赖，零实际 κ 计算——那是 RV3G4-kappa-gate-execution 的职责，blocked-on-external）。

## 【阶段】
01 分解 → 02 研究（§4.3 原文 + 下游消费者枚举 + 三公式数学性质核实）→ 02.5 交叉核对（与 DRAFT v2 0.6 阈值原文对齐 + 与 jaccard-m5 备料先例格式对齐）→ 03 行动分解 → 04 执行验证（材料落盘 + 引用 byte-exact 核验 + 公式数值自检小例）→ 04.5 反方复核

## 【SOP 索引】
- `loop/prompt-first/01..04.5` + `sop/arena-loop-pipeline.md`
- 协议参考（只读）：`ablation/o3-claim-list.md` §4（多判者协议）/ `DRAFT-rubric-v3-v2.md` R-02/R5（κ 条目层 + 0.6 阈值）/ `ablation/scripts/assert-kappa-receipt.py`（method 字段 schema）/ r141 `rejudge/judge-protocol-batch1.md` §4（U-K1 UNRESOLVED 登记处）
- 格式先例（只读）：`bench/rubric-v3/jaccard-m5-adjudication-materials.md`（备料模式五要素：溯源 byte-exact / 选项对照表 / 推荐+理由 / 折中出口 / 裁定后执行清单）

## 【验收标准】
- [ ] kappa-u1k1-adjudication-materials.md 落盘，五要素齐（同 jaccard-m5 先例结构）
- [ ] §4.3 原文 + DRAFT v2 0.6 阈值原文 byte-exact 引用（grep/diff 验证）
- [ ] 三方案对照表每格有依据（公式来源 + N=3 适用性论证，非拍脑袋）
- [ ] 数值自检：≥1 个手算小例（如 3 判者 × 2 条目已知标注矩阵）验证所引公式实现正确
- [ ] 裁定后执行清单可照做（具体文件 + 行级 diff 面描述）
- [ ] 冻结件零修改（git status 验证）；04.5 verdict pass；queue 更新（本 goal 划掉 + 结果注记）

## 【失败降级】
- 若 §4.3 原文存在多种合理读法导致三方案边界模糊 → 把读法分歧本身作为材料的一部分显式登记（同 jaccard-m5「孤儿读法」处置先例），不强行收敛
- 若发现 0.6 阈值在 DRAFT v2 中有多处不一致引用 → 如实登记为附加发现，导出独立勘误候选，不在本 goal 修