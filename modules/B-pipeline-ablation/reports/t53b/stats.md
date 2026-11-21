# T53b 统计汇总

生成: 2026-11-20T13:23:38+08:00
口径: per-run 聚合 | judge 族 qwen3.8-27b ×1 (non-IRR) | seed=42
已记录 run: 16 / 60 | 缺口: 0

## nat

| 臂 | n | coverage mean±SE | 95%CI | depth mean±SE | 95%CI | 高轮次(cov/depth>mean+1SE) |
|---|---|---|---|---|---|---|
| formula | 4 | 0.417±0.159 | [-0.090,0.924] | 0.633±0.060 | [0.441,0.825] | r01c,r04d |
| text | 0 | — | — | — | — | — |

## soc

| 臂 | n | coverage mean±SE | 95%CI | depth mean±SE | 95%CI | 高轮次(cov/depth>mean+1SE) |
|---|---|---|---|---|---|---|
| formula | 1 | 0.857±nan | [nan,nan] | 0.633±nan | [nan,nan] | — |
| text | 0 | — | — | — | — | — |

## gpu

| 臂 | n | coverage mean±SE | 95%CI | depth mean±SE | 95%CI | 高轮次(cov/depth>mean+1SE) |
|---|---|---|---|---|---|---|
| formula | 10 | 0.100±0.023 | [0.049,0.151] | 0.342±0.042 | [0.246,0.438] | r01d,r02c,r03c,r04d,r05c,r05d,r07d,r09c,r10c,r10d |
| text | 1 | 0.067±nan | [nan,nan] | 0.393±nan | [nan,nan] | — |

## 消融对比（主口径：同题内 Δ = formula − text）

| 题 | n_f | n_t | Δcoverage | Δdepth | 方向 |
|---|---|---|---|---|---|
| nat | 4 | 0 | — | — | 数据不足 |
| soc | 1 | 0 | — | — | 数据不足 |
| gpu | 10 | 1 | +0.033 | -0.051 | formula 优 |

注: 跨题绝对 coverage/depth 不可直接比较（rubric 粒度差异），上表 Δ 才是消融结论口径。

## r7 复现（gpu 题 L1 不确定性维度）
l1_uncertainty=true 的轮次: 1/10 [7]
判据: ≥3 轮 → FAIL/待数据

