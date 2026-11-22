# N341: 2×RTX 4090 在推理负载下的总功耗 (Power_consumption_multi) 约为 900W (2 × 450W TDP)，而单卡 RTX 5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N120

## Claim

2×RTX 4090 在推理负载下的总功耗 (Power_consumption_multi) 约为 900W (2 × 450W TDP)，而单卡 RTX 5090 的功耗 (Power_consumption_single) 约为 575W (TDP)，功耗差值 ΔPower = 325W，该差值用于计算 3 年电力成本增量

## Corrected Claim

2×RTX 4090 在推理负载下的总功耗 (Power_consumption_multi) 约为 900W (2 × 450W TDP)，而单卡 RTX 5090 的功耗 (Power_consumption_single) 约为 575W (TDP)，功耗差值 ΔPower = 325W，该差值用于计算 3 年电力成本增量

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP 为 450W，RTX 5090 TDP 为 575W，计算 2*450 - 575 = 325W，数值与逻辑均正确。

## Search Query

RTX 4090 TDP watts vs RTX 5090 TDP watts
