# N110: t_refill 的长尾效应：t_refill 服从 LogNormal(μ=5ms, σ=2ms) 时，P(t_refill > 50ms) ≈ 0.001，

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

t_refill 的长尾效应：t_refill 服从 LogNormal(μ=5ms, σ=2ms) 时，P(t_refill > 50ms) ≈ 0.001，但在这些长尾事件中，P(miss|refill) ≈ 1 - exp(-578.7 * 0.05) ≈ 0.9999，对整体 miss 率的贡献为 0.001 * 0.9999 ≈ 0.001，相比均值情况下的 0.999 * 0.951 ≈ 0.950，长尾影响可忽略（<0.1%）。

## Corrected Claim

t_refill 的长尾效应：t_refill 服从 LogNormal(μ=5ms, σ=2ms) 时，P(t_refill > 50ms) ≈ 0.001，但在这些长尾事件中，P(miss|refill) ≈ 1 - exp(-578.7 * 0.05) ≈ 0.9999，对整体 miss 率的贡献为 0.001 * 0.9999 ≈ 0.001，相比均值情况下的 0.999 * 0.951 ≈ 0.950，长尾影响可忽略（<0.1%）。

## Search Query

lognormal distribution tail probability impact on cache miss rate
