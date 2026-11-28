# N36: 本地推理边际成本：V100 功耗 250W/GPU × 4 GPU = 1000W，电价 $0.10/kWh，每小时电费 $0.10；qwen3.8-27b 在

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

本地推理边际成本：V100 功耗 250W/GPU × 4 GPU = 1000W，电价 $0.10/kWh，每小时电费 $0.10；qwen3.8-27b 在 V100 集群上生成 1 token 耗时 T_gen ≈ 0.5ms（MTP×4 加速），每秒生成 2000 tokens，每小时生成 7.2M tokens，单位 token 成本 C_local = $0.10 / 7.2M ≈ $1.39e-8/token

## Corrected Claim

本地推理边际成本：V100 功耗 250W/GPU × 4 GPU = 1000W，电价 $0.10/kWh，每小时电费 $0.10；qwen3.8-27b 在 V100 集群上生成 1 token 耗时 T_gen ≈ 0.5ms（MTP×4 加速），每秒生成 2000 tokens，每小时生成 7.2M tokens，单位 token 成本 C_local = $0.10 / 7.2M ≈ $1.39e-8/token

## Evidence

先验知识/题面给定，逻辑校验通过：功耗计算（250W*4=1000W）、电费计算（1kW*0.1$/kWh=$0.1/h）、吞吐量换算（1/0.0005s=2000tok/s, *3600=7.2Mtok/h）及单位成本除法（0.1/7.2e6≈1.39e-8）均符合算术逻辑与物理量纲。

## Search Query

V100 power consumption inference cost per token LLM generation speed
