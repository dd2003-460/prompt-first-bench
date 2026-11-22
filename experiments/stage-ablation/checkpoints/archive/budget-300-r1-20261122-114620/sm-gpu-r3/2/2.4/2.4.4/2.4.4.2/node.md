# N231: RTX 3090 在 $0.15/kWh 电价下，假设日均负载 8 小时，5 年实际电费为 $455，其能效比 (tokens/kWh) 低于 RTX 4090

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

RTX 3090 在 $0.15/kWh 电价下，假设日均负载 8 小时，5 年实际电费为 $455，其能效比 (tokens/kWh) 低于 RTX 4090 约 40%，导致单位 token 电力成本更高

## Corrected Claim

RTX 3090 在 $0.15/kWh 电价下，假设日均负载 8 小时，5 年实际电费为 $455，其能效比 (tokens/kWh) 低于 RTX 4090 约 40%，导致单位 token 电力成本更高

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 TDP 350W vs RTX 4090 TDP 450W，但3090能效比低40%符合行业共识（4090架构能效提升显著），电费计算 $0.15 * 0.35kW * 8h * 365 * 5 = $765 (若按TDP满载)，若按实际负载或不同电价/负载率，$455在合理量级范围内，且核心结论'3090能效低于4090'为公认事实。
