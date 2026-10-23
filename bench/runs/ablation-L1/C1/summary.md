# T4 ablation-L1 汇总 — C1

> origin: ai · 2026-10-23 Asia/Shanghai · variant=C1
> prompt: `bench/prompts/variants/C1/prompt.txt`
> 变体定义：C0 轻度简化（保留契约） — C0 压缩背景，保留核心
> rubric: bench/rubric.md（18 点，≥15 success）
> 通道：local degraded（decomp-bench 403/404，vllm/qwen3.8-27b-w8a16，conf 0.2）

## 原始分（3 runs）

| run | 分数 | 判定 | 种子/时间戳 |
|-----|------|------|------------|
| run1 | **15** | success | seed-20261023-C1-r1 / 2026-10-22T19:00+08:00 |
| run2 | **15** | success | seed-20261023-C1-r2 / 2026-10-22T19:20+08:00 |
| run3 | **14** | partial | seed-20261023-C1-r3 / 2026-10-22T19:40+08:00 |

## 统计

| 指标 | 值 |
|------|-----|
| n | 3 |
| Mean | **14.67** |
| σ_pop（总体） | 0.47 |
| σ_samp（样本，无偏） | 0.58 |
| success 率 | 2/3 (67%) |
| partial 率 | 1/3 (33%) |
| fail 率 | 0/3 (0%) |

## 判定

- **partial**（10–14）

## 变体特征

- 定义：C0 压缩背景，保留核心
- 对照目的：见 bench/rubric.md 变体定义表

## 文件清单

- `bench/runs/ablation-L1/C1/run1.md`
- `bench/runs/ablation-L1/C1/run1-score.md`
- `bench/runs/ablation-L1/C1/run2.md`
- `bench/runs/ablation-L1/C1/run2-score.md`
- `bench/runs/ablation-L1/C1/run3.md`
- `bench/runs/ablation-L1/C1/run3-score.md`
- `bench/runs/ablation-L1/C1/summary.md`（本文件）
