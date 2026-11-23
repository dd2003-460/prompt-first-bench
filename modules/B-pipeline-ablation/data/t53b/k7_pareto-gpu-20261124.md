# K7 预算扫描 Pareto 分析

完成 run: 15, 有效: 15

⚠ 质量轴声明（anatomy-0.5184.md）: depth_score 与旧 judge cov15 r=0.861，质量轴 = 同族 LLM judge 分（self-judge 偏差），非独立结构度量；结论限于开源 27b + 4×V100 条件。

## 每档 depth 聚合 + bootstrap 95% CI

| budget | n | mean | CI95 | min | max |
|---|---|---|---|---|---|
| 50 | 3 | 0.3842 | [0.3597, 0.4126] | 0.3597 | 0.4126 |
| 100 | 3 | 0.4352 | [0.4276, 0.4392] | 0.4276 | 0.4392 |
| 150 | 3 | 0.4743 | [0.4300, 0.5184] | 0.4300 | 0.5184 |
| 300 | 3 | 0.4275 | [0.3516, 0.4811] | 0.3516 | 0.4811 |
| 719 | 3 | 0.4376 | [0.4042, 0.4782] | 0.4042 | 0.4782 |

## 实际节点数 vs depth（n=15）

- Spearman ρ = 0.221
- Pearson r = 0.202

| 节点数 | depth | run |
|---|---|---|
| 103 | 0.4126 | gpu_budget50_r2 |
| 122 | 0.4276 | gpu_budget100_r3 |
| 123 | 0.4392 | gpu_budget100_r2 |
| 136 | 0.3597 | gpu_budget50_r3 |
| 167 | 0.4745 | gpu_budget150_r2 |
| 175 | 0.3803 | gpu_budget50_r1 |
| 314 | 0.4389 | gpu_budget100_r1 |
| 364 | 0.4811 | gpu_budget300_r1 |
| 381 | 0.3516 | gpu_budget300_r3 |
| 391 | 0.5184 | gpu_budget150_r3 |
| 392 | 0.4300 | gpu_budget150_r1 |
| 415 | 0.4497 | gpu_budget300_r2 |
| 665 | 0.4305 | gpu_budget719_r1 |
| 709 | 0.4782 | gpu_budget719_r3 |
| 747 | 0.4042 | gpu_budget719_r2 |

## Pareto 包络

| 节点数 | depth | run | 包络点 |
|---|---|---|---|
| 103 | 0.4126 | gpu_budget50_r2 | ★ |
| 122 | 0.4276 | gpu_budget100_r3 | ★ |
| 123 | 0.4392 | gpu_budget100_r2 | ★ |
| 136 | 0.3597 | gpu_budget50_r3 |  |
| 167 | 0.4745 | gpu_budget150_r2 | ★ |
| 175 | 0.3803 | gpu_budget50_r1 |  |
| 314 | 0.4389 | gpu_budget100_r1 |  |
| 364 | 0.4811 | gpu_budget300_r1 | ★ |
| 381 | 0.3516 | gpu_budget300_r3 |  |
| 391 | 0.5184 | gpu_budget150_r3 | ★ |
| 392 | 0.4300 | gpu_budget150_r1 |  |
| 415 | 0.4497 | gpu_budget300_r2 |  |
| 665 | 0.4305 | gpu_budget719_r1 |  |
| 709 | 0.4782 | gpu_budget719_r3 |  |
| 747 | 0.4042 | gpu_budget719_r2 |  |
