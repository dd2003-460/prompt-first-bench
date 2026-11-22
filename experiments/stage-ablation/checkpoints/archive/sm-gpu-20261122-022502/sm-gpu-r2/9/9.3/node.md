# N91: RTX 4090 在 W4A8 (INT4) 精度下的理论解码吞吐量：基于 1.0 TB/s GDDR6X 带宽，理论最大吞吐量 ≈ 1.0 TB/s / (2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

RTX 4090 在 W4A8 (INT4) 精度下的理论解码吞吐量：基于 1.0 TB/s GDDR6X 带宽，理论最大吞吐量 ≈ 1.0 TB/s / (27B * 0.5 bytes) ≈ 74 tokens/s；实际实测值预计为理论值的 50-60%，即 37-44 tokens/s。

## Corrected Claim

RTX 4090 在 W4A8 (INT4) 精度下的理论解码吞吐量：基于 1.0 TB/s GDDR6X 带宽，理论最大吞吐量 ≈ 1.0 TB/s / (27B * 0.5 bytes) ≈ 74 tokens/s；实际实测值预计为理论值的 50-60%，即 37-44 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 GDDR6X带宽约1.0TB/s，INT4权重每token约27B*0.5=13.5KB，理论吞吐1000/13.5≈74 tokens/s，符合算术逻辑；实际效率50-60%符合LLM推理经验规律。

## Search Query

RTX 4090 INT4 LLM inference benchmark tokens per second
