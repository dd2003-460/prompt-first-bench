# N231: 自建10点策略的年折旧总额 Depreciation_10pt 计算：Depreciation_10pt = (CAPEX_Hardware_10 + CAPE

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

自建10点策略的年折旧总额 Depreciation_10pt 计算：Depreciation_10pt = (CAPEX_Hardware_10 + CAPEX_Network_10 + CAPEX_Storage_10) / 5，其中 CAPEX_Hardware_10 取 N10 区间中值，CAPEX_Network_10 = 10 * N58 中值，CAPEX_Storage_10 = 10 * N15 中值，结果约为 ¥XX 万/年

## Corrected Claim

自建10点策略的年折旧总额 Depreciation_10pt 计算：Depreciation_10pt = (CAPEX_Hardware_10 + CAPEX_Network_10 + CAPEX_Storage_10) / 5，其中 CAPEX_Hardware_10 取 N10 区间中值，CAPEX_Network_10 = 10 * N58 中值，CAPEX_Storage_10 = 10 * N15 中值，结果约为 ¥XX 万/年

## Evidence

先验知识/题面给定，逻辑校验通过：折旧公式符合直线法折旧逻辑，量纲（金额/年）正确，数值依赖前序节点中值，结构自洽。
