# T4 ablation-L1 汇总 — C8-noscratch-hard

> origin: ai · 2026-10-23 Asia/Shanghai · variant=C8-noscratch-hard
> prompt: `bench/prompts/variants/C8-noscratch-hard/prompt.txt`
> 变体定义：C0 - 草稿区（硬约束） — C0 去掉草稿区且显式禁止（严禁出现 <scratch>）
> rubric: bench/rubric.md（18 点，≥15 success）
> 通道：local degraded（decomp-bench 403/404，vllm/qwen3.8-27b-w8a16，conf 0.2）

## 原始分（3 runs）

| run | 分数 | 判定 | 种子/时间戳 |
|-----|------|------|------------|
| run1 | **11** | partial | seed-20261023-C8-noscratch-hard-r1 / 2026-10-23T10:40+08:00 |
| run2 | **13** | partial | seed-20261023-C8-noscratch-hard-r2 / 2026-10-23T11:00+08:00 |
| run3 | **13** | partial | seed-20261023-C8-noscratch-hard-r3 / 2026-10-23T11:20+08:00 |

## 统计

| 指标 | 值 |
|------|-----|
| n | 3 |
| Mean | **12.33** |
| σ_pop（总体） | 0.94 |
| σ_samp（样本，无偏） | 1.15 |
| success 率 | 0/3 (0%) |
| partial 率 | 3/3 (100%) |
| fail 率 | 0/3 (0%) |

## 判定

- **partial**（10–14）

## 变体特征

- 定义：C0 去掉草稿区且显式禁止（严禁出现 <scratch>）
- 对照目的：见 bench/rubric.md 变体定义表

## 文件清单

- `bench/runs/ablation-L1/C8-noscratch-hard/run1.md`
- `bench/runs/ablation-L1/C8-noscratch-hard/run1-score.md`
- `bench/runs/ablation-L1/C8-noscratch-hard/run2.md`
- `bench/runs/ablation-L1/C8-noscratch-hard/run2-score.md`
- `bench/runs/ablation-L1/C8-noscratch-hard/run3.md`
- `bench/runs/ablation-L1/C8-noscratch-hard/run3-score.md`
- `bench/runs/ablation-L1/C8-noscratch-hard/summary.md`（本文件）
