# N118: 基础信息方差 $\sigma_{info}$ 的量化估算：基于二手市场常见信息缺失（如电池健康度、维修史），假设 $\sigma_{info} \approx 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

基础信息方差 $\sigma_{info}$ 的量化估算：基于二手市场常见信息缺失（如电池健康度、维修史），假设 $\sigma_{info} \approx 0.10 \times P_{market}$，即信息不对称导致买家估值偏差约为市场公允价的 10%，该系数需通过 A/B 测试（展示完整参数 vs 隐藏参数）中的决策方差差异进行校准。

## Corrected Claim

基础信息方差 $\sigma_{info}$ 的量化估算：基于二手市场常见信息缺失（如电池健康度、维修史），假设 $\sigma_{info} \approx 0.10 \times P_{market}$，即信息不对称导致买家估值偏差约为市场公允价的 10%，该系数需通过 A/B 测试（展示完整参数 vs 隐藏参数）中的决策方差差异进行校准。

## Evidence

先验知识/题面给定，逻辑校验通过
