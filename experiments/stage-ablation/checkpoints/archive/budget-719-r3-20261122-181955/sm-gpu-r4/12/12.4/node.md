# N381: RTX 5090 的 TDP 为 575W (官方规格)，在 LLM 推理负载下平均功耗约为 0.7 * 575W ≈ 402.5W，年电力成本 (7x24 运

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N128

## Claim

RTX 5090 的 TDP 为 575W (官方规格)，在 LLM 推理负载下平均功耗约为 0.7 * 575W ≈ 402.5W，年电力成本 (7x24 运行, $0.15/kWh) 约为 402.5W * 8760h * $0.15/kWh ≈ $529 USD/年。

## Corrected Claim

RTX 5090 的 TDP 约为 575W（待核实），在 LLM 推理负载下平均功耗估算约为 402.5W，年电力成本估算约为 $529 USD/年。

## Evidence

[质询]RTX 5090 的官方 TDP 规格（575W）属于具体硬件参数，且 LLM 推理负载下的平均功耗系数（0.7）为经验估算值，缺乏直接来源支持，存在口径混淆或数值偏差风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证 TDP 具体数值及负载系数）

## Search Query

RTX 5090 TDP power consumption watts
