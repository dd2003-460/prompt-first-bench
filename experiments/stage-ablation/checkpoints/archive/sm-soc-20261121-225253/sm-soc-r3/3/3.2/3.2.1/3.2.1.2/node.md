# N89: 曝光损失的非线性边界条件：当 |P_ask - P_avg|/P_avg > 30% 时，线性模型 E_new = E0 * (1 - k*d) 失效，实际曝光

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

曝光损失的非线性边界条件：当 |P_ask - P_avg|/P_avg > 30% 时，线性模型 E_new = E0 * (1 - k*d) 失效，实际曝光损失趋于饱和（E_new → 0），需引入对数修正：E_new = E0 * exp(-k' * d)，其中 k' ≈ 0.01-0.02；若仍用线性模型，在 d=40% 时高估曝光量约 20-30%。

## Corrected Claim

曝光损失的非线性边界条件：当 |P_ask - P_avg|/P_avg > 30% 时，线性模型 E_new = E0 * (1 - k*d) 失效，实际曝光损失趋于饱和（E_new → 0），需引入对数修正：E_new = E0 * exp(-k' * d)，其中 k' ≈ 0.01-0.02；若仍用线性模型，在 d=40% 时高估曝光量约 20-30%。

## Search Query

non-linear exposure penalty saturation effect price deviation threshold
