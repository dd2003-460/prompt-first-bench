# N7: 热度-大小负相关（ρ ≈ -0.3）对 LRU 命中率的影响：热门对象平均大小 S_hot = S_mean * (1 + ρ * σ_S/μ_S)，冷对象平均

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

热度-大小负相关（ρ ≈ -0.3）对 LRU 命中率的影响：热门对象平均大小 S_hot = S_mean * (1 + ρ * σ_S/μ_S)，冷对象平均大小 S_cold = S_mean * (1 - ρ * σ_S/μ_S)，命中率加权 = (S_hot * H_hot + S_cold * H_cold) / (S_hot + S_cold)

## Corrected Claim

热度-大小负相关（ρ ≈ -0.3）对 LRU 命中率的影响：热门对象平均大小 S_hot = S_mean * (1 + ρ * σ_S/μ_S)，冷对象平均大小 S_cold = S_mean * (1 - ρ * σ_S/μ_S)，命中率加权 = (S_hot * H_hot + S_cold * H_cold) / (S_hot + S_cold)

## Evidence

先验知识/题面给定，逻辑校验通过
