# N146: 混合策略下，带宽成本波动10%导致每千请求成本增加量（ΔCost_Hybrid）的加权计算：ΔCost_Hybrid = (Traffic_Pub_per_1k

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

混合策略下，带宽成本波动10%导致每千请求成本增加量（ΔCost_Hybrid）的加权计算：ΔCost_Hybrid = (Traffic_Pub_per_1k * ΔP_Pct * Unit_Price_Pub + Traffic_Self_per_1k * 0) / 1000，由于自建部分无波动，结果介于全公有云与自建之间，具体数值取决于流量切分比例

## Corrected Claim

混合策略下，带宽成本波动10%导致每千请求成本增加量（ΔCost_Hybrid）的加权计算：ΔCost_Hybrid = (Traffic_Pub_per_1k * ΔP_Pct * Unit_Price_Pub + Traffic_Self_per_1k * 0) / 1000，由于自建部分无波动，结果介于全公有云与自建之间，具体数值取决于流量切分比例

## Evidence

先验知识/题面给定，逻辑校验通过：混合策略成本波动仅由公有云部分贡献，自建部分成本固定，加权公式符合线性叠加原理，量纲与逻辑自洽。
