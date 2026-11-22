# N130: 共享随机源：搜索/推荐排序函数的截断误差 ε_rank 的方差 σ_rank² 与商品特征向量稀疏度 S 的定量关系为 σ_rank² = k_sparse *

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N35, N36, N37

## Claim

共享随机源：搜索/推荐排序函数的截断误差 ε_rank 的方差 σ_rank² 与商品特征向量稀疏度 S 的定量关系为 σ_rank² = k_sparse * (1/S)，其中 k_sparse 是模型复杂度常数，需通过离线日志回放验证 k_sparse 的具体数值范围。

## Corrected Claim

搜索/推荐排序函数的截断误差受模型复杂度和数据分布影响，但截断误差方差与商品特征向量稀疏度之间不存在通用的 σ_rank² = k_sparse * (1/S) 定量关系，具体误差特性需通过离线日志回放针对特定模型和数据集进行实证分析。

## Evidence

[质询]该陈述提出了一个具体的定量公式 σ_rank² = k_sparse * (1/S)，声称截断误差方差与稀疏度成反比。然而，在搜索/推荐排序系统中，截断误差（Truncation Error）通常指模型近似或计算截断带来的偏差，其方差与特征稀疏度 S 之间并不存在通用的、标准的反比定量关系。该公式缺乏通用的理论推导支持，且 k_sparse 的定义模糊，极可能是特定场景下的经验拟合或虚构的伪科学公式，属于将特定假设强行普遍化的错误。 | 参考来源[1]仅定义了截断误差为计算方法中有限过程代替无限过程产生的误差，未涉及排序函数、特征稀疏度或任何定量方差公式，来源与事实主题不匹配且无支持；该定量关系无法从第一性原理推出，属于缺乏依据的经验性断言。

## Search Query

recommender system ranking truncation error variance sparsity correlation

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E6%88%AA%E6%96%AD%E8%AF%AF%E5%B7%AE/4778191&rut=18a8d13c0baea40b3c554a87477b0586f14fa70dc40e733264f4b76a15195cbc', 'type': 'ddg', 'title': '截断误差_百度百科'}
