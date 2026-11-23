# N323: 全自建策略在流量增长 50% 时的单位变动成本 $C_{var, new}^{self} = P_{bw}^{self} \times (V_{new} - V

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121

## Claim

全自建策略在流量增长 50% 时的单位变动成本 $C_{var, new}^{self} = P_{bw}^{self} \times (V_{new} - V_{base}) / R_{new}$，由于自建带宽通常按峰值预留，若峰值带宽未随流量线性增长（受缓存命中率提升影响），则变动成本增量可能小于流量增量，需量化 $\Delta C_{var}^{self}$。

## Corrected Claim

全自建策略在流量增长 50% 时的单位变动成本 $C_{var, new}^{self} = P_{bw}^{self} \times (V_{new} - V_{base}) / R_{new}$，由于自建带宽通常按峰值预留，若峰值带宽未随流量线性增长（受缓存命中率提升影响），则变动成本增量可能小于流量增量，需量化 $\Delta C_{var}^{self}$。

## Evidence

先验知识/题面给定，逻辑校验通过
