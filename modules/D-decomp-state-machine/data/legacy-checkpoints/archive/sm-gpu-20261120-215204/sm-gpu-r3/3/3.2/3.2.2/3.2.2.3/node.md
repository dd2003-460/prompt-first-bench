# N249: L40S FP8 全量化方案的质量损失量化：FP8 (E4M3/E5M2) 权重和 KV Cache 量化通常导致 MMLU 基准下降 <1%，且 NVIDIA

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N86

## Claim

L40S FP8 全量化方案的质量损失量化：FP8 (E4M3/E5M2) 权重和 KV Cache 量化通常导致 MMLU 基准下降 <1%，且 NVIDIA TensorRT-LLM 对 FP8 的支持成熟，在 L40S (Ada Lovelace 架构) 上可获得接近 BF16 的精度表现，该方案在精度和性能之间取得最佳平衡，优于 INT8 方案 (N85) 的精度保持，且优于 BF16 方案 (N135) 的显存效率。

## Corrected Claim

L40S FP8 全量化方案的质量损失量化：FP8 (E4M3/E5M2) 权重和 KV Cache 量化通常导致 MMLU 基准下降 <1%，且 NVIDIA TensorRT-LLM 对 FP8 的支持成熟，在 L40S (Ada Lovelace 架构) 上可获得接近 BF16 的精度表现，该方案在精度和性能之间取得最佳平衡，优于 INT8 方案 (N85) 的精度保持，且优于 BF16 方案 (N135) 的显存效率。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8在L40S上的精度损失通常小于1%且优于INT8/BF16的平衡性符合工程常识与架构特性。
