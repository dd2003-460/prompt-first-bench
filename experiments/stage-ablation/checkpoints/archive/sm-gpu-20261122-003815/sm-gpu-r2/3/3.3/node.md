# N21: 精度选择的决策阈值：若 FP8 退化 <1% 且硬件支持 FP8 加速 (如 H100, L40S)，则 FP8 为最优性价比选择。若 INT8 退化 <2% 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

精度选择的决策阈值：若 FP8 退化 <1% 且硬件支持 FP8 加速 (如 H100, L40S)，则 FP8 为最优性价比选择。若 INT8 退化 <2% 且消费级卡 (RTX 4090) 支持 INT8 推理 (通过 llama.cpp/vLLM)，则 INT8 为消费级最优。若 INT4 退化 >5%，则不建议用于生产环境。

## Corrected Claim

精度选择的决策阈值：若 FP8 退化 <1% 且硬件支持 FP8 加速 (如 H100, L40S)，则 FP8 为最优性价比选择。若 INT8 退化 <2% 且消费级卡 (RTX 4090) 支持 INT8 推理 (通过 llama.cpp/vLLM)，则 INT8 为消费级最优。若 INT4 退化 >5%，则不建议用于生产环境。

## Evidence

先验知识/题面给定，逻辑校验通过
