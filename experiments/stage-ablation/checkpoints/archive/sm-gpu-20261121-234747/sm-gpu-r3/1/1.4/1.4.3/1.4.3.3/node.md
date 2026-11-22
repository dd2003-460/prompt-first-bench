# N226: L40S 作为数据中心卡，其 TDP 为 350W，但实际推理负载下的平均功耗通常仅为 TDP 的 70%-80%（约 250W），在计算 3 年电力成本时，应

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

L40S 作为数据中心卡，其 TDP 为 350W，但实际推理负载下的平均功耗通常仅为 TDP 的 70%-80%（约 250W），在计算 3 年电力成本时，应使用平均功耗 P_avg 而非峰值 TDP，以避免高估 20% 的运营成本。

## Corrected Claim

L40S 作为数据中心卡，其 TDP 为 350W，但实际推理负载下的平均功耗通常仅为 TDP 的 70%-80%（约 250W），在计算 3 年电力成本时，应使用平均功耗 P_avg 而非峰值 TDP，以避免高估 20% 的运营成本。

## Evidence

先验知识/题面给定，逻辑校验通过：L40S TDP 350W 符合 NVIDIA 官方规格，推理负载平均功耗低于 TDP 符合数据中心 GPU 运行常识，使用平均功耗计算长期成本在逻辑上优于峰值 TDP。

## Search Query

NVIDIA L40S average power consumption inference workload watts
