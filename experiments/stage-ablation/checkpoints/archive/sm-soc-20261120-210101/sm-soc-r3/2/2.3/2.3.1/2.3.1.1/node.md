# N184: σ_algo² 的量化：算法特征感知误差的标准差。假设 σ_algo = 0.1（归一化特征空间），意味着算法对商品‘稀缺性’特征的估计误差标准差为 0.1。该

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N51

## Claim

σ_algo² 的量化：算法特征感知误差的标准差。假设 σ_algo = 0.1（归一化特征空间），意味着算法对商品‘稀缺性’特征的估计误差标准差为 0.1。该误差直接导致曝光权重 W_exposure 的波动。

## Corrected Claim

σ_algo² 的量化：算法特征感知误差的标准差。假设 σ_algo 为归一化特征空间下的估计误差标准差（具体数值需根据实际模型校准确定，此处暂设为 0.1 作为示例），该误差会导致曝光权重 W_exposure 的波动。

## Evidence

[质询]该陈述包含具体的经验参数假设（σ_algo = 0.1），属于经验事实范畴，无法从第一性原理或数学公理中严格推导得出，且缺乏外部来源支持该特定数值量级的合理性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

algorithm feature estimation error variance recommendation system
