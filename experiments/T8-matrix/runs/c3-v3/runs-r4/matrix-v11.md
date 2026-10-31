# R4 全因子 × J1-strict-v11 判官矩阵

> origin: ai · 2026-10-31 · runner r45 后解析 runs-r4/*-J1v11.json (36/36)
> 判官: J1-strict-v11 (design/rubric-v2-density-test.json) · 模型: qwen3.8-27b @ :8787

| config | mean_pass_rate | D1/a | D1/b | D2/a | D2/b | floors触发 |
|---|---|---|---|---|---|---|
| A-full | 0.750 | 10/10 | 3/10 | 9/10 | 8/10 | — |
| B-nofreeze | 0.494 | 3/8|low_specificity | 8/10 | 4/8 | 3/10 | low_specificity |
| B-noevidence | 0.906 | 7/8 | 6/8 | 10/10 | 8/8 | — |
| B-noowner | 0.767 | 7/8 | 4/6 | 5/8 | 9/10 | — |
| B-2del-fe | 0.627 | 6/10 | 6/8 | 4/17|low_specificity | 12/13 | low_specificity |
| B-2del-fo | 0.523 | 5/10 | 3/10 | 4/6 | 5/8 | — |
| B-2del-eo | 0.606 | 6/8 | 14/16 | 3/10 | 3/6 | — |
| B-none | 0.678 | 4/8 | 7/9 | 18/30 | 10/12 | — |
| B-sham | 0.542 | 2/20|floor,evidence_floor,low_specificity | 4/10 | 14/14 | 4/6 | evidence_floor,floor,low_specificity |

## 观察

1. **B-noevidence=0.906 异常**：删证据组件反升 15pt。人工过 4 个原始输出：证据并未缺失（具体数值/厂商/正交分解都在），模型自发写出。假设：判官 specificity/echo 审计对'自然具体'比对'被逼具体'更宽容（待 A-full vs B-noevidence 的 density/echo_ratio 对比坐实）。
2. **B-none(0.678) > B-sham(0.542)**：v11 能区分真空组件与假消融；sham 触发 floor+evidence_floor（识别出引用不存在的冻结记录）。完整矩阵复现 v11 关键改进。
3. **B-noowner≈A-full**（0.767 vs 0.750）：owner 组件在两个任务域无可测贡献，或 rubric 10 项无直接考 owner 行为的题项。
4. B-nofreeze=0.494 最低：冻结件仍是最大单组件贡献（-35%），与 v11 部分验证一致。
