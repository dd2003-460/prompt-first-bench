# N242: 平台注意力权重 $W_{algo}$ 的具体量化指标定义：$W_{algo} = w_{dwell} \cdot DwellTime + w_{ctr} \cd

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

平台注意力权重 $W_{algo}$ 的具体量化指标定义：$W_{algo} = w_{dwell} \cdot DwellTime + w_{ctr} \cdot CTR + w_{gmv} \cdot GMV$，需估算各系数比 $\kappa = w_{dwell}/w_{gmv}$ 的阈值以验证其对高溢价商品的加权效应。

## Corrected Claim

平台注意力权重 $W_{algo}$ 的具体量化指标定义：$W_{algo} = w_{dwell} \cdot DwellTime + w_{ctr} \cdot CTR + w_{gmv} \cdot GMV$，需估算各系数比 $\kappa = w_{dwell}/w_{gmv}$ 的阈值以验证其对高溢价商品的加权效应。

## Evidence

先验知识/题面给定，逻辑校验通过
