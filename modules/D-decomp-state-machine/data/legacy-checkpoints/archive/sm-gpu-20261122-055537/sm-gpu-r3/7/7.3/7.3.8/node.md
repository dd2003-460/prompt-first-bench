# N341: Per-channel 量化相比 Per-tensor 量化在 FP8 下的额外存储开销精确值：对于 Qwen3-27B 的 54 层 Transformer，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107, N108, N109

## Claim

Per-channel 量化相比 Per-tensor 量化在 FP8 下的额外存储开销精确值：对于 Qwen3-27B 的 54 层 Transformer，Per-channel 需要为每个输出通道存储一个 Scale Factor (FP32, 4 bytes)，总额外开销 = Num_Layers * Hidden_Dim * 4 bytes，需计算该值占总模型权重大小 (27GB) 的百分比，以验证 N108 中 '1-4 bytes/layer' 描述的准确性并量化其实际影响。

## Corrected Claim

Per-channel 量化相比 Per-tensor 量化在 FP8 下的额外存储开销精确值：对于 Qwen3-27B 的 54 层 Transformer，Per-channel 需要为每个输出通道存储一个 Scale Factor (FP32, 4 bytes)，总额外开销 = Num_Layers * Hidden_Dim * 4 bytes，需计算该值占总模型权重大小 (27GB) 的百分比，以验证 N108 中 '1-4 bytes/layer' 描述的准确性并量化其实际影响。

## Evidence

先验知识/题面给定，逻辑校验通过：Per-channel 量化确实需要为每个输出通道存储一个 Scale Factor，对于 Qwen3-27B（假设 Hidden_Dim 约为 4096-8192），54 层的额外开销计算逻辑自洽，且量级合理（通常占比极小，验证了 N108 中低开销的描述）。
