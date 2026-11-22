# N42: 算法权重比值的可观测代理变量：由于 $w_{price}$ 和 $w_{freshness}$ 不可直接获取，定义代理指标 $R_{proxy} = \frac

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

算法权重比值的可观测代理变量：由于 $w_{price}$ 和 $w_{freshness}$ 不可直接获取，定义代理指标 $R_{proxy} = \frac{\text{CTR}_{high\_price, fresh}}{\text{CTR}_{low\_price, fresh}}$。若平台驱动高挂价，$R_{proxy}$ 应显著大于 1.0；需设定阈值 $R_{threshold}$（例如 1.2），当 $R_{proxy} > R_{threshold}$ 且控制其他特征后，方可推断 $w_{freshness} > w_{price}$ 对高溢价商品的相对优势。

## Corrected Claim

算法权重比值的可观测代理变量：由于 $w_{price}$ 和 $w_{freshness}$ 不可直接获取，定义代理指标 $R_{proxy} = \frac{\text{CTR}_{high\_price, fresh}}{\text{CTR}_{low\_price, fresh}}$。若平台驱动高挂价，$R_{proxy}$ 应显著大于 1.0；需设定阈值 $R_{threshold}$（例如 1.2），当 $R_{proxy} > R_{threshold}$ 且控制其他特征后，方可推断 $w_{freshness} > w_{price}$ 对高溢价商品的相对优势。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点围绕‘控制混淆变量的严格程度’这一单一维度进行划分，分别对应高成本/低偏误、中成本/中偏误、零成本/高偏误三种工作点，彼此互斥且无逻辑矛盾；三者共同覆盖了从严格因果推断到快速定性判断的完整决策空间，未遗漏父节点中关于阈值设定和推断条件（如控制其他特征）的关键方面；各节点涉及不同的统计方法（完全控制、PSM、无控制）和数据要求，并非同一参数的简单取值，而是方法论层面的不同选择，因此不构成冗余。）
