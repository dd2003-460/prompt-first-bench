# 03 行动分解 — self-optimization-tester

> origin: ai · 2026-10-23 · 断点 A/B/C 已过（gate-evidence-breakpoint-ABC.md）

## 剩余原子步骤（依赖顺序，无并行项）
| # | 步骤 | 输出 | 依赖 |
|---|------|------|------|
| S1 | 本地执行 loop 04 工件（execution-log：本任务自身的 per-step 记录） | stages/04/execution-log.md | 断点 A/B/C ✅ |
| S2 | 04.5 反方复核：找 §3.0 链路的矛盾与漏洞 | stages/04.5/review.md | S1 |
| S3 | bench 定义（≥5 指标 + 权重 + baseline）+ 计算总加权分数 | stages/04.5/bench.md | S2 |
| S4 | 发布：bench 工件 push pfb + ls-remote 验证 | pfb commit | S3 |
| S5 | loop-report.md（8 步链路复盘 + 卡点 + §3.0 改进建议） | loop-report.md | S4 |
| S6 | 新 goal 文本（含 §3.0 全节）落盘，create_goal 由 Lead 顶层执行 | new-goal-<date>.md | S5 |

## 执行级约束
- 每步产出落盘后再进下一步（pass 门禁）。
- bench 基线锚点：pfb rubric D1-D4 既有体系（0.9）+ token 效率新轴；外部开源 baseline 不可得 → 标 unverified，不虚构。

## 判定
pass
