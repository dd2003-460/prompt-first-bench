# N79: Prefill 阶段（计算受限）的吞吐量近似公式为 T_prefill ≈ FLOPS_eff / (2 * N_params)，其中 FLOPS_eff 为有

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

Prefill 阶段（计算受限）的吞吐量近似公式为 T_prefill ≈ FLOPS_eff / (2 * N_params)，其中 FLOPS_eff 为有效算力（峰值算力 * MFU，MFU 通常取 0.5-0.7），N_params 为参数量（27e9）

## Corrected Claim

Prefill 阶段（计算受限）的吞吐量近似公式为 T_prefill ≈ FLOPS_eff / (2 * N_params)，其中 FLOPS_eff 为有效算力（峰值算力 * MFU，MFU 通常取 0.5-0.7），N_params 为参数量（27e9）

## Evidence

先验知识/题面给定，逻辑校验通过：Prefill阶段为计算密集型，每token处理需约2*N_params FLOPs，故吞吐量=有效算力/单token计算量，公式推导正确且量级合理。

## Search Query

LLM prefill throughput formula FLOPS parameters MFU
