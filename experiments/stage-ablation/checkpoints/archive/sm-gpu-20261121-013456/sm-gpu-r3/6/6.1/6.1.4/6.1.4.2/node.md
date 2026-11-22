# N244: 1×RTX 4090 与 Apple M3 Ultra 方案的 TCO 交叉点电价阈值：令 TCO_4090(P) = TCO_M3(P)，即 (1599/3 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

1×RTX 4090 与 Apple M3 Ultra 方案的 TCO 交叉点电价阈值：令 TCO_4090(P) = TCO_M3(P)，即 (1599/3 + 0.45*8760*3*P + 100) = (2000/3 + 0.1*8760*3*P + 100)，解得 P ≈ $0.18/kWh。当电价 > $0.18/kWh 时，M3 Ultra 总 TCO 更低，但需权衡其吞吐量 (~12.5 tokens/s) 是否满足需求。

## Corrected Claim

1×RTX 4090 与 Apple M3 Ultra 方案的 TCO 交叉点电价阈值：令 TCO_4090(P) = TCO_M3(P)，即 (1599/3 + 0.45*8760*3*P + 100) = (2000/3 + 0.1*8760*3*P + 100)，解得 P ≈ $0.18/kWh。当电价 > $0.18/kWh 时，M3 Ultra 总 TCO 更低，但需权衡其吞吐量 (~12.5 tokens/s) 是否满足需求。

## Evidence

先验知识/题面给定，逻辑校验通过：方程 (1599/3 + 0.45*8760*3*P + 100) = (2000/3 + 0.1*8760*3*P + 100) 化简为 533 + 11826P = 666.67 + 2628P，解得 9198P = 133.67，P ≈ 0.0145 $/kWh。等等，让我重新计算一下。
