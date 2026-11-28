# N312: KL 散度计算的数值稳定性处理：当 p_gold(x) 或 p_model(x) 接近 0 时，log 项可能发散；需添加平滑参数 ε=1e-6，即 KL = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

KL 散度计算的数值稳定性处理：当 p_gold(x) 或 p_model(x) 接近 0 时，log 项可能发散；需添加平滑参数 ε=1e-6，即 KL = Σ (p_gold + ε) * log((p_gold + ε)/(p_model + ε))，并验证平滑前后 KL 值差异小于 1%

## Corrected Claim

KL 散度计算的数值稳定性处理：当 p_gold(x) 或 p_model(x) 接近 0 时，log 项可能发散；需添加平滑参数 ε=1e-6，即 KL = Σ (p_gold + ε) * log((p_gold + ε)/(p_model + ε))，并验证平滑前后 KL 值差异小于 1%

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

KL divergence numerical stability smoothing epsilon Laplace smoothing
