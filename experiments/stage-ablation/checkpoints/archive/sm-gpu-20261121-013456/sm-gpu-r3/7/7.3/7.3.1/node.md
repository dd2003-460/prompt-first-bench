# N271: AMD Radeon PRO W7900 的 TDP 规格为 300W，但实际 27B BF16 推理满载功耗需实测，预期在 250W-280W 区间（低于 T

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N106

## Claim

AMD Radeon PRO W7900 的 TDP 规格为 300W，但实际 27B BF16 推理满载功耗需实测，预期在 250W-280W 区间（低于 TDP 上限），该值直接决定电力成本项的计算基数。

## Corrected Claim

AMD Radeon PRO W7900 的最大功耗规格为 295W（来源 [1]），实际 27B BF16 推理满载功耗需实测，预期在 250W-280W 区间（低于 TDP 上限），该值直接决定电力成本项的计算基数。

## Evidence

[质询]陈述中声称 TDP 为 300W，但参考来源 [1] 明确记载最大功耗为 295W，数值存在偏差；此外，250W-280W 的实测预期值属于经验性推测，缺乏直接来源支持。 | 来源 [1] 指出最大功耗为 295W 而非 300W，且未提供 27B BF16 推理的具体实测功耗数据，仅能间接支持功耗低于 TDP 上限的逻辑，但具体数值区间缺乏直接证据。

## Search Query

AMD Radeon PRO W7900 TDP wattage AI inference power consumption

## Retrieval Sources

- {'url': 'https://www.techpowerup.com/gpu-specs/radeon-pro-w7900.c4147&rut=032a0517bd49507844fd1ce3e5a9db49414a1cdff9485059e87f985221eb7ba7', 'type': 'ddg', 'title': 'AMD Radeon PRO W7900 Specs | TechPowerUp GPU Database'}
