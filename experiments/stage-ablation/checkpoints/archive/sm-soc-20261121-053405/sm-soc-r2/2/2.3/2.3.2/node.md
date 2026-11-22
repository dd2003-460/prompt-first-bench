# N42: 算法权重比值的可观测代理变量：由于 $w_{price}$ 和 $w_{freshness}$ 不可直接获取，定义代理指标 $R_{proxy} = \frac

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

算法权重比值的可观测代理变量：由于 $w_{price}$ 和 $w_{freshness}$ 不可直接获取，定义代理指标 $R_{proxy} = \frac{\text{CTR}_{high\_price, fresh}}{\text{CTR}_{low\_price, fresh}}$。若平台驱动高挂价，$R_{proxy}$ 应显著大于 1.0；需设定阈值 $R_{threshold}$（例如 1.2），当 $R_{proxy} > R_{threshold}$ 且控制其他特征后，方可推断 $w_{freshness} > w_{price}$ 对高溢价商品的相对优势。

## Corrected Claim

算法权重比值的可观测代理变量：由于 $w_{price}$ 和 $w_{freshness}$ 不可直接获取，定义代理指标 $R_{proxy} = \frac{\text{CTR}_{high\_price, fresh}}{\text{CTR}_{low\_price, fresh}}$。若平台驱动高挂价，$R_{proxy}$ 应显著大于 1.0；需设定阈值 $R_{threshold}$（例如 1.2），当 $R_{proxy} > R_{threshold}$ 且控制其他特征后，方可推断 $w_{freshness} > w_{price}$ 对高溢价商品的相对优势。

## Evidence

先验知识/题面给定，逻辑校验通过
