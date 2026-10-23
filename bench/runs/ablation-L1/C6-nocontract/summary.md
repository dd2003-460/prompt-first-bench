# T4 ablation-L1 汇总 — C6-nocontract

> origin: ai · 2026-10-23 Asia/Shanghai · variant=C6-nocontract
> prompt: `bench/prompts/variants/C6-nocontract/prompt.txt`
> 变体定义：C0 - 契约条款 — C0 去掉接口契约段（无函数签名/验收方式）
> rubric: bench/rubric.md（18 点，≥15 success）
> 通道：local degraded（decomp-bench 403/404，vllm/qwen3.8-27b-w8a16，conf 0.2）

## 原始分（3 runs）

| run | 分数 | 判定 | 种子/时间戳 |
|-----|------|------|------------|
| run1 | **12** | partial | seed-20261023-C6-nocontract-r1 / 2026-10-23T09:40+08:00 |
| run2 | **14** | partial | seed-20261023-C6-nocontract-r2 / 2026-10-23T10:00+08:00 |
| run3 | **13** | partial | seed-20261023-C6-nocontract-r3 / 2026-10-23T10:20+08:00 |

## 统计

| 指标 | 值 |
|------|-----|
| n | 3 |
| Mean | **13.00** |
| σ_pop（总体） | 0.82 |
| σ_samp（样本，无偏） | 1.00 |
| success 率 | 0/3 (0%) |
| partial 率 | 3/3 (100%) |
| fail 率 | 0/3 (0%) |

## 判定

- **partial**（10–14）

## 变体特征

- 定义：C0 去掉接口契约段（无函数签名/验收方式）
- 对照目的：见 bench/rubric.md 变体定义表

## 文件清单

- `bench/runs/ablation-L1/C6-nocontract/run1.md`
- `bench/runs/ablation-L1/C6-nocontract/run1-score.md`
- `bench/runs/ablation-L1/C6-nocontract/run2.md`
- `bench/runs/ablation-L1/C6-nocontract/run2-score.md`
- `bench/runs/ablation-L1/C6-nocontract/run3.md`
- `bench/runs/ablation-L1/C6-nocontract/run3-score.md`
- `bench/runs/ablation-L1/C6-nocontract/summary.md`（本文件）
