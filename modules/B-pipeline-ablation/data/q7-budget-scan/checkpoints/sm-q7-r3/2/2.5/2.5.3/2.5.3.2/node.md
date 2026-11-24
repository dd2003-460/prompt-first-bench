# N234: 冷数据实际取回量 Q_retrieval = 冷数据总量 400TB × 年访问率 10% = 40TB = 40,960 GB，该计算基于“每次访问读取完整对

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

冷数据实际取回量 Q_retrieval = 冷数据总量 400TB × 年访问率 10% = 40TB = 40,960 GB，该计算基于“每次访问读取完整对象”且“无重复读取”的保守假设。

## Corrected Claim

冷数据实际取回量 Q_retrieval = 冷数据总量 400TB × 年访问率 10% = 40TB = 40,960 GB，该计算基于“每次访问读取完整对象”且“无重复读取”的保守假设。

## Evidence

先验知识/题面给定，逻辑校验通过：400TB * 10% = 40TB，且 40TB * 1024GB/TB = 40960GB，数值换算与逻辑推导均正确。
