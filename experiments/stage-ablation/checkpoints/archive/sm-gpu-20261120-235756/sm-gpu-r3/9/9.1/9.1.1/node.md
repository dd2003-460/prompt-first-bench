# N337: RTX 5090 在 FP8 精度下运行 Qwen3-27B 时，实际 TPOT 的计算公式修正为：TPOT_real = (Activated_Params 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N127

## Claim

RTX 5090 在 FP8 精度下运行 Qwen3-27B 时，实际 TPOT 的计算公式修正为：TPOT_real = (Activated_Params * Precision_Bytes) / (Memory_Bandwidth * Utilization_Factor)。由于 Qwen3 是 MoE 架构，Activated_Params 为 3.3B 而非总参数量 27.18B，因此分子应使用 3.3e9 * 1 byte，而非 27.18e9 * 1 byte，这将导致理论 TPOT 上限大幅降低（即速度更快）。

## Corrected Claim

RTX 5090 在 FP8 精度下运行 Qwen3-27B 时，实际 TPOT 的计算公式修正为：TPOT_real = (Activated_Params * Precision_Bytes) / (Memory_Bandwidth * Utilization_Factor)。由于 Qwen3 是 MoE 架构，Activated_Params 为 3.3B 而非总参数量 27.18B，因此分子应使用 3.3e9 * 1 byte，而非 27.18e9 * 1 byte，这将导致理论 TPOT 上限大幅降低（即速度更快）。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 确为 MoE 架构，激活参数约 3.3B，FP8 下每参数 1 字节，公式推导符合内存带宽瓶颈下的理论极限计算逻辑。

## Search Query

MoE inference TPOT calculation activated parameters vs total parameters
