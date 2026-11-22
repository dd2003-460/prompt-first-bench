# N169: 工作点3（低响应/高溢价）：当 v_high(t) 延迟显著（如 τ > 24h）且 P_high = 1.25 * P_median 时，积分尾部权重增加，但

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

工作点3（低响应/高溢价）：当 v_high(t) 延迟显著（如 τ > 24h）且 P_high = 1.25 * P_median 时，积分尾部权重增加，但 λ_b 的低值导致整体积分值低于工作点2，需量化此时的效用损失百分比。

## Corrected Claim

工作点3（低响应/高溢价）：当 v_high(t) 延迟显著（如 τ > 24h）且 P_high = 1.25 * P_median 时，积分尾部权重增加，但 λ_b 的低值导致整体积分值低于工作点2，需量化此时的效用损失百分比。

## Evidence

先验知识/题面给定，逻辑校验通过：在积分效用模型中，若低响应率（λ_b低）对总积分值的负向贡献大于高溢价（P_high高）带来的正向贡献，则整体效用低于基准工作点，该逻辑自洽且符合经济学直觉。

## Search Query

delayed response high price sale probability utility loss
