# 阶段 04：执行日志 — RUBRIC-V3-FULL-AUDIT / G5 优化清单

> goal: rubric-v3-audit-g5 · 分支 ralph/rubric-v3-audit-g5 · 2026-10-30

## A1 ✅ 交付物 g5-optimization-list.md

落盘 `bench/rubric-v3/ablation/g5-optimization-list.md`，五节结构完整：

1. **机判化候选表**（6 行 C1-C6）：每条含判定内容/输入文件/断言逻辑摘要/可复用性/成本/防住的风险。C1/C2 标注"含 schema 提案"前置依赖；C6 登记为低价值不实施。合计 ~9 回合（合并后 ~7）。
2. **并行化候选表**（5 行 P1-P5）：每条含步骤/并行理由/前置条件/执行保真度风险/成本。P1/P2/P3 标"信息边界"（外部依赖不可控）；P4 BLOCKED by finding #17；P5 风险最低（样本清单已就绪）。
3. **成本估算总表**：3a 机判+并行汇总；3b 12 blocker 逐条三级分类（L1×5 ≈ 10 回合 + L2×7 ≈ 22 回合 = ~32 回合），B2 注明完整修复路径为信息边界；3c 16 major + 4 minor 处置建议（不逐条估成本，属 G6 范围）。
4. **负面结果声明**（6 条）：W0 退化 / W1 tie-sensitive / new W3 top5_gold tie-sensitive / per-run 无 run 过线 / 语义级重判不可机判 / κ 值计算本身不可机判。
5. **给 G6 的导出**：建议 G6 前落地 5 项（按优先级排序）+ 留给后续 goal 5 项 + G6 硬约束提醒 3 条（S2 限定语 / 32 findings 处置表 / tie-sensitivity 限定语）。

## A2 ✅ current-goal.md 改写

五字段格式更新为 G5 收口态（见收口序列）。

## A3（commit/push/merge/queue）— 见收口序列

## 未完成项与诚实保留

- **κ/p̃ source schema 未定义**：C1/C2 的断言逻辑依赖 schema，本 goal 只给了最小 schema 提案（字段名+类型），未定稿。schema 定稿属 RV3G4-* 或 G6 范围。
- **12 blocker 中 B2 的完整修复成本为信息边界**：完整修复需异族 judge 或双 gold（L3 外部依赖），本 goal 只估了"声明局限"路径的成本（~4 回合）。
- **16 major 未逐条分级**：3c 节只给了粗略分布估计（~8 L1 + ~8 L2），未逐条列出。逐条处置表属 G6 定稿范围。
- **web-llm 三 provider 全失效**：无法做外部交叉验证（如查文献中类似 assert 脚本的实现模式），所有设计基于仓库内已有脚本先例。
- **成本估算单位为 runner 回合数**：非人时，不同 runner 配置下实际耗时可能不同。估算基于类比（R5.2 脚本 ~143 行 / assert-g1-audit 137 行），非精确工时。