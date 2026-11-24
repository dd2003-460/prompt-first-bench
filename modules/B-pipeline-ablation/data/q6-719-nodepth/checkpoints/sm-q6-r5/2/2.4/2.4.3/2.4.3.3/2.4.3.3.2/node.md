# N589: 工作点 B（西部低密度区域）：西部单 POP 承载流量较少，但回源比例高。假设西部 5 POP 承载 40% 流量，单 POP λ ≈ 2,222 req/s。

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N193

## Claim

工作点 B（西部低密度区域）：西部单 POP 承载流量较少，但回源比例高。假设西部 5 POP 承载 40% 流量，单 POP λ ≈ 2,222 req/s。ρ = 2,222 / 16,000 ≈ 0.14。然而，若采用 N192 的保守工作点 C（μ=8,000 req/s），则 ρ = 2,222 / 8,000 ≈ 0.28。模型仍有效，但需关注长尾请求导致的瞬时 ρ 波动。

## Corrected Claim

工作点 B（西部低密度区域）：西部单 POP 承载流量较少，但回源比例高。假设西部 5 POP 承载 40% 流量，单 POP λ ≈ 2,222 req/s。ρ = 2,222 / 16,000 ≈ 0.14。然而，若采用 N192 的保守工作点 C（μ=8,000 req/s），则 ρ = 2,222 / 8,000 ≈ 0.28。模型仍有效，但需关注长尾请求导致的瞬时 ρ 波动。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（2222/16000≈0.14, 2222/8000≈0.28），排队论逻辑自洽，符合低负载高回源场景特征。

## Search Query

CDN edge node traffic distribution west china low density
