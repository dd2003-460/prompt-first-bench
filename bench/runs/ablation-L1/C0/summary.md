# T4 ablation-L1 汇总 — C0

> origin: ai · 2026-10-23 Asia/Shanghai · variant=C0
> prompt: `bench/prompts/variants/C0/prompt.txt`
> 变体定义：完整 prompt 基线（full） — 含角色+任务+契约条款+草稿区+输出结构+约束
> rubric: bench/rubric.md（18 点，≥15 success）
> 通道：local degraded（decomp-bench 403/404，vllm/qwen3.8-27b-w8a16，conf 0.2）

## 原始分（3 runs）

| run | 分数 | 判定 | 种子/时间戳 |
|-----|------|------|------------|
| run1 | **15** | success | seed-20261023-C0-r1 / 2026-10-22T19:00+08:00 |
| run2 | **16** | success | seed-20261023-C0-r2 / 2026-10-22T19:20+08:00 |
| run3 | **15** | success | seed-20261023-C0-r3 / 2026-10-22T19:40+08:00 |

## 统计

| 指标 | 值 |
|------|-----|
| n | 3 |
| Mean | **15.33** |
| σ_pop（总体） | 0.47 |
| σ_samp（样本，无偏） | 0.58 |
| success 率 | 3/3 (100%) |
| partial 率 | 0/3 (0%) |
| fail 率 | 0/3 (0%) |

## 判定

- **success**（mean ≥15）

## 变体特征

- 定义：含角色+任务+契约条款+草稿区+输出结构+约束
- 对照目的：见 bench/rubric.md 变体定义表

## 文件清单

- `bench/runs/ablation-L1/C0/run1.md`
- `bench/runs/ablation-L1/C0/run1-score.md`
- `bench/runs/ablation-L1/C0/run2.md`
- `bench/runs/ablation-L1/C0/run2-score.md`
- `bench/runs/ablation-L1/C0/run3.md`
- `bench/runs/ablation-L1/C0/run3-score.md`
- `bench/runs/ablation-L1/C0/summary.md`（本文件）
