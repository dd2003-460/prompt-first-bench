# N145: 共享随机源：干预参数调整幅度 $\Delta \theta$ 的分布特征：$\Delta \theta \sim \mathcal{N}(\mu_{\Delta

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

共享随机源：干预参数调整幅度 $\Delta \theta$ 的分布特征：$\Delta \theta \sim \mathcal{N}(\mu_{\Delta}, \sigma_{\Delta}^2)$，其中 $\mu_{\Delta}$ 为算法迭代平均步长，$\sigma_{\Delta}$ 为参数波动标准差；该随机源同时影响 $\Delta w_{price}$ 和 $\Delta w_{freshness}$ 的实际落地值，导致理论最小调整量与实际调整量存在偏差 $\epsilon_{impl} = \Delta \theta_{actual} - \Delta \theta_{theoretical}$。

## Corrected Claim

共享随机源：干预参数调整幅度 $\Delta \theta$ 的分布特征：$\Delta \theta \sim \mathcal{N}(\mu_{\Delta}, \sigma_{\Delta}^2)$，其中 $\mu_{\Delta}$ 为算法迭代平均步长，$\sigma_{\Delta}$ 为参数波动标准差；该随机源同时影响 $\Delta w_{price}$ 和 $\Delta w_{freshness}$ 的实际落地值，导致理论最小调整量与实际调整量存在偏差 $\epsilon_{impl} = \Delta \theta_{actual} - \Delta \theta_{theoretical}$。

## Evidence

先验知识/题面给定，逻辑校验通过
