# N188: 实际 LFU 命中率 $H_{LFU}^{act}$ 的保守下界：取 $\epsilon_{freq} = 20\%$，$\epsilon_{overhead}

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

实际 LFU 命中率 $H_{LFU}^{act}$ 的保守下界：取 $\epsilon_{freq} = 20\%$，$\epsilon_{overhead} = 2\%$，则 $H_{LFU}^{act} \approx 0.8 H_{LFU}^{max} - 0.02$。若 $H_{LFU}^{max} = 100\%$，则 $H_{LFU}^{act} \approx 78\%$。

## Corrected Claim

实际 LFU 命中率 $H_{LFU}^{act}$ 的保守下界：取 $\epsilon_{freq} = 20\%$，$\epsilon_{overhead} = 2\%$，则 $H_{LFU}^{act} \approx 0.8 H_{LFU}^{max} - 0.02$。若 $H_{LFU}^{max} = 100\%$，则 $H_{LFU}^{act} \approx 78\%$。

## Evidence

先验知识/题面给定，逻辑校验通过：0.8 * 100% - 2% = 78%，计算无误且符合LFU实际性能低于理论上限的工程直觉。
