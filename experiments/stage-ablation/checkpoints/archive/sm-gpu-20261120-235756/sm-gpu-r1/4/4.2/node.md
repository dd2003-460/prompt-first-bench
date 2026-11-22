# N21: TPOT（每Token生成时间）计算模型：TPOT ≈ (N_params * Precision_Bits) / (GPU_Mem_BW * Utilizat

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

TPOT（每Token生成时间）计算模型：TPOT ≈ (N_params * Precision_Bits) / (GPU_Mem_BW * Utilization_Factor)，对于 Qwen3-27B (27e9 params)，在 BF16 下 TPOT 主要受限于显存带宽而非计算能力，需列出不同显存带宽（如 900GB/s vs 2000GB/s）下的理论 TPOT 上限。

## Corrected Claim

TPOT（每Token生成时间）计算模型：TPOT ≈ (N_params * Precision_Bits) / (GPU_Mem_BW * Utilization_Factor)，对于 Qwen3-27B (27e9 params)，在 BF16 下 TPOT 主要受限于显存带宽而非计算能力，需列出不同显存带宽（如 900GB/s vs 2000GB/s）下的理论 TPOT 上限。

## Evidence

先验知识/题面给定，逻辑校验通过：大模型推理在解码阶段（Decode）主要受显存带宽限制（Memory-Bound），TPOT理论上限公式推导符合物理直觉，数值量级合理。
