# Goal: RV3G4-prior-source-assert — prior-estimates.json 独立 p̃ 生成源断言脚本

> 创建：2026-10-30 · ralph loop runner（`tasks/goal-queue.md` 候选「RV3G4-prior-source-assert」）
> 依据：G4 交付物「给 G5 的导出」第一类 + S3 降档教训（纸面协议零防护力直到被执行）；参考 R5.2 系列 assert-* 模式

## 【目标】
assert 脚本校验 `bench/rubric-v3/ablation/prior-estimates.json` 必须记录 ≥N 个独立 p̃ 生成源（source 字段缺失/单源 = FAIL），消除「p̃ 来源不可机判」状态。

**范围发现（阶段 A 实证）**：该 goal 的核心交付物已存在——`scripts/assert-prior-source.py`（commit 0fedf42, r130）+ `prior-estimates.json:p_tilde_provenance` 双源登记块，8/8 PASS exit 0。→ 本 goal 收口为**验证+补强**而非从零新建：(a) 复验现有脚本基线；(b) 变异测试证明防单源能力真实生效（队列候选的验收语义）；(c) 缺口审计——对照队列原文逐条核销；(d) 残余缺口登记/处置。

## 【阶段】
纯仓库内机判工作。单脚本验证 + 变异测试 + 可能的补强小修。

## 【SOP 索引】
- `loop/prompt-first/01..04.5`；对象 `bench/rubric-v3/ablation/scripts/assert-prior-source.py` + `prior-estimates.json`（冻结面——只读，要改走 APPROVALS）

## 【验收标准】
- [ ] 现有脚本实跑 8/8 PASS exit 0（基线复验）
- [ ] 变异测试：删除 independent_sources 一条 → 脚本 FAIL exit 1（防单源能力实证，非纸面声明）
- [ ] 变异测试：删除整个 p_tilde_provenance 块 → 脚本 FAIL exit 1（source 字段缺失路径实证）
- [ ] 队列候选原文逐条核销表（「≥N 个独立源 / source 缺失 FAIL / 单源 FAIL / signal-only 或 verdict 二选一在 01 定」四项）
- [ ] 冻结面零触碰（prior-estimates.json 只读；变异测试用 /tmp 副本）

## 【失败降级】
- 现有脚本有真缺陷（变异不触发）→ 修复脚本本身（新文件改动允许，数据文件不动）
- web-llm 不可用 → unverified 降级（机械验证边际贡献 ≈ 0，同族判据）