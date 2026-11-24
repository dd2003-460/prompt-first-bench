# N372: 10个POP点年度电力总成本需按各POP所在城市的电价分别计算后求和，而非使用单一平均电价，若10个POP分布在5个不同省份，需加权计算：Σ(PUE_i × P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

10个POP点年度电力总成本需按各POP所在城市的电价分别计算后求和，而非使用单一平均电价，若10个POP分布在5个不同省份，需加权计算：Σ(PUE_i × Power_i × 8760h × Price_i)

## Corrected Claim

10个POP点年度电力总成本需按各POP所在城市的电价分别计算后求和，而非使用单一平均电价，若10个POP分布在5个不同省份，需加权计算：Σ(PUE_i × Power_i × 8760h × Price_i)

## Evidence

先验知识/题面给定，逻辑校验通过：电力成本计算遵循基本物理与经济原理，总成本为各节点成本之和，且不同地区电价不同，必须分别计算后求和，公式量纲与逻辑自洽。
