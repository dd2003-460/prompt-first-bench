# T4 ablation-L1 汇总 — C4-arch

> origin: ai · 2026-10-23 Asia/Shanghai · variant=C4-arch
> prompt: `bench/prompts/variants/C4-arch/prompt.txt`
> 变体定义：C0 + 架构图（mermaid） — C0 + mermaid 架构图（graph TD 6 模块）
> rubric: bench/rubric.md（18 点，≥15 success）
> 通道：local degraded（decomp-bench 403/404，vllm/qwen3.8-27b-w8a16，conf 0.2）

## 原始分（3 runs）

| run | 分数 | 判定 | 种子/时间戳 |
|-----|------|------|------------|
| run1 | **15** | success | seed-20261023-C4-arch-r1 / 2026-10-23T08:40+08:00 |
| run2 | **15** | success | seed-20261023-C4-arch-r2 / 2026-10-23T09:00+08:00 |
| run3 | **15** | success | seed-20261023-C4-arch-r3 / 2026-10-23T09:20+08:00 |

## 统计

| 指标 | 值 |
|------|-----|
| n | 3 |
| Mean | **15.00** |
| σ_pop（总体） | 0.00 |
| σ_samp（样本，无偏） | 0.00 |
| success 率 | 3/3 (100%) |
| partial 率 | 0/3 (0%) |
| fail 率 | 0/3 (0%) |

## 判定

- **success**（mean ≥15）

## 变体特征

- 定义：C0 + mermaid 架构图（graph TD 6 模块）
- 对照目的：见 bench/rubric.md 变体定义表

## 文件清单

- `bench/runs/ablation-L1/C4-arch/run1.md`
- `bench/runs/ablation-L1/C4-arch/run1-score.md`
- `bench/runs/ablation-L1/C4-arch/run2.md`
- `bench/runs/ablation-L1/C4-arch/run2-score.md`
- `bench/runs/ablation-L1/C4-arch/run3.md`
- `bench/runs/ablation-L1/C4-arch/run3-score.md`
- `bench/runs/ablation-L1/C4-arch/summary.md`（本文件）
