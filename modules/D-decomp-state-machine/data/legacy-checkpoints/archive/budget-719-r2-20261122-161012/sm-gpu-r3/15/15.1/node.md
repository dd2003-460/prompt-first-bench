# N321: TTFT (Time To First Token) 在 32K 上下文下的理论计算公式为 T_TTFT = (2 * N_params * L_context

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N138

## Claim

TTFT (Time To First Token) 在 32K 上下文下的理论计算公式为 T_TTFT = (2 * N_params * L_context) / (FLOPS * Utilization)，其中 N_params=27e9, L_context=32768，FLOPS 为硬件峰值算力，Utilization 为实际利用率 (通常 0.6-0.8)。

## Corrected Claim

TTFT (Time To First Token) 在 32K 上下文下的理论计算公式为 T_TTFT = (2 * N_params * L_context) / (FLOPS * Utilization)，其中 N_params=27e9, L_context=32768，FLOPS 为硬件峰值算力，Utilization 为实际利用率 (通常 0.6-0.8)。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合大模型推理Prefill阶段计算量（2*参数*序列长度）与算力利用率的基本物理关系，数值量级合理。
