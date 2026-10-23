# T4 ablation-L1 汇总 — C3-exposneg

> origin: ai · 2026-10-23 Asia/Shanghai · variant=C3-exposneg
> prompt: `bench/prompts/variants/C3-exposneg/prompt.txt`
> 变体定义：C2-expos + 负向草稿（反例） — C2-expos + 负向草稿（展示错误分解，请勿模仿）
> rubric: bench/rubric.md（18 点，≥15 success）
> 通道：local degraded（decomp-bench 403/404，vllm/qwen3.8-27b-w8a16，conf 0.2）

## 原始分（3 runs）

| run | 分数 | 判定 | 种子/时间戳 |
|-----|------|------|------------|
| run1 | **13** | partial | seed-20261023-C3-exposneg-r1 / 2026-10-23T08:10+08:00 |
| run2 | **14** | partial | seed-20261023-C3-exposneg-r2 / 2026-10-23T08:30+08:00 |
| run3 | **14** | partial | seed-20261023-C3-exposneg-r3 / 2026-10-23T08:50+08:00 |

## 统计

| 指标 | 值 |
|------|-----|
| n | 3 |
| Mean | **13.67** |
| σ_pop（总体） | 0.47 |
| σ_samp（样本，无偏） | 0.58 |
| success 率 | 0/3 (0%) |
| partial 率 | 3/3 (100%) |
| fail 率 | 0/3 (0%) |

## 判定

- **partial**（10–14）

## 变体特征

- 定义：C2-expos + 负向草稿（展示错误分解，请勿模仿）
- 对照目的：见 bench/rubric.md 变体定义表

## 文件清单

- `bench/runs/ablation-L1/C3-exposneg/run1.md`
- `bench/runs/ablation-L1/C3-exposneg/run1-score.md`
- `bench/runs/ablation-L1/C3-exposneg/run2.md`
- `bench/runs/ablation-L1/C3-exposneg/run2-score.md`
- `bench/runs/ablation-L1/C3-exposneg/run3.md`
- `bench/runs/ablation-L1/C3-exposneg/run3-score.md`
- `bench/runs/ablation-L1/C3-exposneg/summary.md`（本文件）
