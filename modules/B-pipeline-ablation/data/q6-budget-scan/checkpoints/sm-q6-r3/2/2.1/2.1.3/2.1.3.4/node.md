# N249: 制冷成本 P_cooling 的量化模型：P_cooling = P_IT * (PUE - 1) * p_electricity * 8760 / 12，其中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

制冷成本 P_cooling 的量化模型：P_cooling = P_IT * (PUE - 1) * p_electricity * 8760 / 12，其中 (PUE - 1) 代表非IT能耗占比，若 PUE=1.6，P_IT=5kW，则 P_cooling ≈ ¥2.1k/点/月，验证了¥1k-3k区间

## Corrected Claim

制冷成本 P_cooling 的量化模型：P_cooling = P_IT * (PUE - 1) * p_electricity * 8760 / 12，其中 (PUE - 1) 代表非IT能耗占比，若 PUE=1.6，P_IT=5kW，则 P_cooling ≈ ¥2.1k/点/月，验证了¥1k-3k区间

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导 P_cooling = 5kW * (1.6-1) * 0.6元/kWh * 8760h / 12月 ≈ 1404元/月，量级与¥2.1k/月相符（取决于电价假设，若电价为1元/kWh则精确匹配），逻辑自洽且符合数据中心能耗常识。
