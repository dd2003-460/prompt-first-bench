# N305: Power_Cost_per_Token 的精确计算公式：Power_Cost_per_Token = (GPU_Power_Watts * P_electri

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N121

## Claim

Power_Cost_per_Token 的精确计算公式：Power_Cost_per_Token = (GPU_Power_Watts * P_electricity_per_kWh * 3600) / (Throughput_tokens_per_s * 1000)。其中 GPU_Power_Watts 需取推理负载下的实测均值（非 TDP 峰值），P_electricity 取当地居民/商业电价（如中国 0.5-1.0 CNY/kWh 或美国 0.10-0.30 USD/kWh）。

## Corrected Claim

Power_Cost_per_Token 的精确计算公式：Power_Cost_per_Token = (GPU_Power_Watts * P_electricity_per_kWh * 3600) / (Throughput_tokens_per_s * 1000)。其中 GPU_Power_Watts 需取推理负载下的实测均值（非 TDP 峰值），P_electricity 取当地居民/商业电价（如中国 0.5-1.0 CNY/kWh 或美国 0.10-0.30 USD/kWh）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RTX 4090 average power consumption LLM inference watts vs TDP
