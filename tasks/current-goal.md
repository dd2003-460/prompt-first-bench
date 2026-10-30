# Goal: RV3G3-goldrank-threshold-proof — gold 平均排名口径过线阈值正式论证

> 创建：2026-10-30 · ralph loop runner（`tasks/goal-queue.md` 候选「RV3G3-goldrank-threshold-proof」）
> 依据：G3 04.5 W6 导出；freeze doc §2.1 引用占位符 `threshold_top10 := RV3G3-goldrank-threshold-proof 产出值` + §2.3 门禁行 ❌

## 【目标】
top-10 辅助口径过线阈值的正式论证（超几何 n=31,k=5,r=10 精确基线升级 + 候选阈值评估 + 适用性边界声明）+ gmr vs top-10 同级备选地位的终裁材料，供 G6 定稿 O1 时消费。回填 `gmr-criterion-freeze.md` §2.1/§2.3（引用机制预留通道）。

**范围定位**：本 goal 给**材料与推荐**，最终阈值裁定权在成璐/G6（同 G3「推荐路径供 G6 非决策」惯例；双轨呈现 t=3/t=4 不代选）。

## 【阶段】
纯仓库内推导（冻结数据复算 + 文档落盘），零外部依赖。

## 【SOP 索引】
- `loop/prompt-first/01..04.5`；对象 `bench/rubric-v3/goldrank-threshold-proof.md`（新建）+ `gmr-criterion-freeze.md` §2（两行回填）+ `ablation/scripts/assert-goldrank-threshold.py`（新建防漂移断言）
- 数据源（只读冻结）：`prior-estimates.json` / `judge-blindtest-r1.json` / `assert-gmr-recompute.py` GOLD 清单

## 【验收标准】
- [ ] 论证文档 L1-L4 四层齐（精确基线 Fraction 值 / 候选阈值评估 / 适用性边界声明 / 同级备选终裁材料），全文统一 0-based 口径
- [ ] 超几何精确值与 freeze §2.2 锚点 byte 级一致（50/31、0.027438、0.175751）且补齐 t=1/2/5
- [ ] 当前数据实测表（8 方案×judge 的 top-10 计数 + gmr）与 G3 F3b L47/L48 + freeze §5 交叉核验零 mismatch
- [ ] freeze doc §2.1 回填（不再含未回填占位语）+ §2.3 门禁行 ❌→✅，diff 面 ≤3 行
- [ ] assert-goldrank-threshold.py exit 0 + 变异测试（篡改基线值 → FAIL）
- [ ] queue 条目划掉 + 结果注记

## 【失败降级】
- 复算发现与既有锚点 mismatch → 以现场 Fraction 复算为准，登记偏差来源（同 U3 口径裁定先例）
- freeze doc 回填被 04.5 判为需 APPROVALS → 补登记不阻塞（机制内通道论证见 stages01-03 A4）
- web-llm 不可用 → unverified 降级（纯推导边际贡献 ≈ 0，同族判据）