# N460: 样本量 n=30 的标准误计算验证：SE = sqrt(p(1-p)/n)，在 p=0.5 (最坏情况) 时 SE = sqrt(0.25/30) ≈ 0.09

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N161

## Claim

样本量 n=30 的标准误计算验证：SE = sqrt(p(1-p)/n)，在 p=0.5 (最坏情况) 时 SE = sqrt(0.25/30) ≈ 0.0913，不满足 SE < 0.05 的要求；若要 SE < 0.05，需 n >= p(1-p)/0.05^2 = 0.25/0.0025 = 100，因此 n=30 仅在 p 极接近 0 或 1 时成立

## Corrected Claim

样本量 n=30 的标准误计算验证：SE = sqrt(p(1-p)/n)，在 p=0.5 (最坏情况) 时 SE = sqrt(0.25/30) ≈ 0.0913，不满足 SE < 0.05 的要求；若要 SE < 0.05，需 n >= p(1-p)/0.05^2 = 0.25/0.0025 = 100，因此 n=30 仅在 p 极接近 0 或 1 时成立

## Evidence

先验知识/题面给定，逻辑校验通过：SE=sqrt(0.25/30)≈0.0913>0.05，且n=100为p=0.5时的最小样本量，推导正确
