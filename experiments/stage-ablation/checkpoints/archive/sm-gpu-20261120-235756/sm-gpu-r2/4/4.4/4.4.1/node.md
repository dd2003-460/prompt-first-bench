# N91: TPOT 理论加速比公式：Speedup_Ratio = BW_BF16 / BW_Quantized，其中 BW_Quantized 受限于量化后权重读取带宽

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

TPOT 理论加速比公式：Speedup_Ratio = BW_BF16 / BW_Quantized，其中 BW_Quantized 受限于量化后权重读取带宽及反量化计算开销，实际加速比通常低于理论 2x (BF16->FP8/INT8)。

## Corrected Claim

TPOT 理论加速比公式：Speedup_Ratio = BW_BF16 / BW_Quantized，其中 BW_Quantized 受限于量化后权重读取带宽及反量化计算开销，实际加速比通常低于理论 2x (BF16->FP8/INT8)。

## Evidence

先验知识/题面给定，逻辑校验通过：在内存带宽受限（Memory-Bound）场景下，理论加速比确实由带宽比决定；实际加速比低于理论值是因为反量化（Dequantization）引入了额外的计算开销（Compute Overhead），且实际推理往往并非完全带宽受限，该表述符合系统性能分析的基本原理。

## Search Query

quantization inference speedup ratio theoretical vs actual
