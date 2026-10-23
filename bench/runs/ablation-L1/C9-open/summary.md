# T4 ablation-L1 汇总 — C9-open

> origin: ai · 2026-10-23 Asia/Shanghai · variant=C9-open
> prompt: `bench/prompts/variants/C9-open/prompt.txt`
> 变体定义：开放式 prompt（无固定结构） — 无固定结构，仅一句任务描述，无角色/契约/草稿区/示例
> rubric: bench/rubric.md（18 点，≥15 success）
> 通道：local degraded（decomp-bench 403/404，vllm/qwen3.8-27b-w8a16，conf 0.2）

## 原始分（3 runs）

| run | 分数 | 判定 | 种子/时间戳 |
|-----|------|------|------------|
| run1 | **8** | fail | seed-20261023-C9-open-r1 / 2026-10-23T11:10+08:00 |
| run2 | **11** | partial | seed-20261023-C9-open-r2 / 2026-10-23T11:30+08:00 |
| run3 | **10** | partial | seed-20261023-C9-open-r3 / 2026-10-23T11:50+08:00 |

## 统计

| 指标 | 值 |
|------|-----|
| n | 3 |
| Mean | **9.67** |
| σ_pop（总体） | 1.25 |
| σ_samp（样本，无偏） | 1.53 |
| success 率 | 0/3 (0%) |
| partial 率 | 2/3 (67%) |
| fail 率 | 1/3 (33%) |

## 判定

- **fail**（<10）

## 变体特征

- 定义：无固定结构，仅一句任务描述，无角色/契约/草稿区/示例
- 对照目的：见 bench/rubric.md 变体定义表

## 文件清单

- `bench/runs/ablation-L1/C9-open/run1.md`
- `bench/runs/ablation-L1/C9-open/run1-score.md`
- `bench/runs/ablation-L1/C9-open/run2.md`
- `bench/runs/ablation-L1/C9-open/run2-score.md`
- `bench/runs/ablation-L1/C9-open/run3.md`
- `bench/runs/ablation-L1/C9-open/run3-score.md`
- `bench/runs/ablation-L1/C9-open/summary.md`（本文件）
