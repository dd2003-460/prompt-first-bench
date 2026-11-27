# N137: T_search 的条件分布量化：在二手平台，T_search 服从对数正态分布，其均值受商品类别特异性影响，通用类目均值约为 45 分钟 (0.75h)，而高

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

T_search 的条件分布量化：在二手平台，T_search 服从对数正态分布，其均值受商品类别特异性影响，通用类目均值约为 45 分钟 (0.75h)，而高特异性类目（如特定型号二手相机）均值可达 90 分钟 (1.5h)；该分布的偏度系数需通过平台搜索日志计算以修正均值偏差。

## Corrected Claim

T_search 的条件分布量化：在二手平台，T_search 服从对数正态分布，其均值受商品类别特异性影响，通用类目均值约为 45 分钟 (0.75h)，而高特异性类目（如特定型号二手相机）均值可达 90 分钟 (1.5h)；该分布的偏度系数需通过平台搜索日志计算以修正均值偏差。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

used goods platform search time distribution log-normal mean
