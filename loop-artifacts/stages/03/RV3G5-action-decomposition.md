# 阶段 03：行动分解 — RUBRIC-V3-FULL-AUDIT / G5 优化清单

> goal: rubric-v3-audit-g5 · 分支 ralph/rubric-v3-audit-g5 · 2026-10-30

## DAG

| # | 行动 | owner | 依赖 | 验收方式 |
|---|------|-------|------|----------|
| A1 | 写交付物 `bench/rubric-v3/ablation/g5-optimization-list.md`（五节结构） | runner | 02/02.5 完成 | 文件存在且含全部五节；机判化表 ≥5 行；并行化表 ≥5 行；成本总表含 12 blocker 三级分类 |
| A2 | 改写 `tasks/current-goal.md` 为 G5 收口态 | runner | A1 | 五字段格式，【目标】= G5 收口，【阶段】= 04.5 完成 |
| A3 | commit + push + merge main + queue checkpoint | runner | A1+A2 | ls-remote 验证 + main @ 新 commit + queue 进度注记追加 |

## 关键判读分支预注册

- **若 12 blocker 中某条无法分级**（信息不足以判断 L1/L2/L3）→ 标"待 G6 判定"而非强行归类。
- **若机判化候选中有实际不可机判的项**（如语义级重判）→ 移入负面结果声明节，不留在候选表。
- **若并行化候选的成本估算超出本轮可估范围**（外部依赖不可控）→ 标"信息边界"并说明缺什么信息。

## 不做的事边界

- **不实现任何 assert 脚本**——C1/C2 已入队 RV3G4-*，本 goal 只做设计+成本。
- **不替 G6 做定稿决策**——不给 O1/O2/O3 最终推荐，只给候选+成本供 G6 取舍。
- **不修改冻结数据**——prior-estimates.json / judge-blindtest-r1.json / hit-matrix.json / gold-tree.md / DRAFT-rubric-v3.md 全部只读。
- **不执行并行化步骤**——P1-P5 只评估可行性+成本，不实际运行。

→ 进入 04。