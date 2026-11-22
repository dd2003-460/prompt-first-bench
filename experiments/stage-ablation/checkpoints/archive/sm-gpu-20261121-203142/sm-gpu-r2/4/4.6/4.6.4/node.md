# N100: 单位成本吞吐量（Tokens/$/Hour）计算框架：Cost_per_token = (Hardware_Depreciation + Electricity

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

单位成本吞吐量（Tokens/$/Hour）计算框架：Cost_per_token = (Hardware_Depreciation + Electricity_Cost) / (TPS * B_max * 3600 * 24)，需将N25的TPS与N26的B_max结合，并代入N19/N20的TCO数据，以量化不同硬件在满负载下的经济性。

## Corrected Claim

单位成本吞吐量（Tokens/$/Hour）计算框架：Cost_per_token = (Hardware_Depreciation + Electricity_Cost) / (TPS * B_max * 3600 * 24)，需将N25的TPS与N26的B_max结合，并代入N19/N20的TCO数据，以量化不同硬件在满负载下的经济性。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（成本/时间 / (吞吐量/秒 * 并发数 * 秒/小时 * 小时/天) = 成本/Token），且符合硬件经济性分析的基本定义。
