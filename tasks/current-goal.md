# Goal: RV3G4-kappa-receipt-assert — κ 门禁执行回执断言脚本

> 创建：2026-10-30 · ralph loop runner（`tasks/goal-queue.md` 候选「RV3G4-kappa-receipt-assert」）
> 依据：G4 交付物「给 G5 的导出」第一类 + g5-optimization-list.md C2 行（含最小 schema 提案义务）；消除 R3「κ 门禁 unverified」状态

## 【目标】
评分文件缺 κ 门禁执行回执 = FAIL 的断言脚本：**回执格式定义**（最小 schema，g5 C2 明示「schema 不存在（G1 gap），需最小 schema 提案」）+ **存在性/schema 检查**。参考 assert-prior-source.py 模式（r130/r135 刚验证过的同族结构）。

## 【阶段】
纯仓库内机判工作。schema 提案 + 脚本落地 + 变异测试 + 当前数据状态处置。

## 【SOP 索引】
- `loop/prompt-first/01..04.5`；对象 `bench/rubric-v3/ablation/scripts/assert-kappa-receipt.py`（新建）+ DRAFT v2 §R5 门禁条款（只读参照）

## 【验收标准】
- [ ] 最小 schema 提案落盘（字段集 + 类型 + 语义，依据 g5 C2 四字段 gate_passed/kappa_value/method/judges + DRAFT v2 R5 条款对齐）
- [ ] assert-kappa-receipt.py 落盘：回执缺失 → FAIL exit 1；schema 违例 → FAIL；κ<0.6 → SIGNAL（g5 C2 原文三分支）
- [ ] 变异测试：空目录/缺字段/κ 低值三场景行为实证
- [ ] **当前数据状态如实处置**：消融评分实际未执行换位双判门禁（g4 S3 实证）→ 脚本对当前 ablation 数据的真实输出是什么必须跑出来并如实记录（预期 = FAIL，这恰是脚本要暴露的事实——「κ 门禁无回执」从人工判断变机判事实）；不得为让脚本绿而伪造回执
- [ ] 冻结面零触碰（不新建 kappa-receipt.json 假数据；hit-matrix/prior-estimates 等只读）

## 【失败降级】
- 「FAIL 即收口还是登记已知缺口」的判定在 01 定：预注册 = 脚本正确性以变异测试为准，对真实数据的 FAIL 输出是**预期行为**而非脚本缺陷（与 assert-c4-timing 的 not-reconstructable SIGNAL 同构——机判工具的职责是让缺口可见）
- web-llm 不可用 → unverified 降级（机械改动边际贡献 ≈ 0，同族判据）