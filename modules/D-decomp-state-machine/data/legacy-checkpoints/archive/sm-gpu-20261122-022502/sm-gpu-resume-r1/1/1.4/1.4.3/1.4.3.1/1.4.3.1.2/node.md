# N518: RTX 4090 在 FP8 精度下因缺乏原生硬件支持，需通过 TensorRT-LLM 或 PyTorch 进行 INT8/BF16 模拟或反量化，其有效 F

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N158

## Claim

RTX 4090 在 FP8 精度下因缺乏原生硬件支持，需通过 TensorRT-LLM 或 PyTorch 进行 INT8/BF16 模拟或反量化，其有效 FP8 等效算力为 BF16 峰值 165 TFLOPS 乘以效率系数 0.4-0.6，即 66-99 TFLOPS，主要损耗来自额外的 Dequantize 指令开销 [待核验：TensorRT-LLM 文档中 FP8 在 Ada Lovelace 架构上的支持状态]

## Corrected Claim

RTX 4090 在 FP8 精度下因缺乏原生硬件支持（需 Compute Capability 9.x），需通过软件模拟或反量化实现，其有效 FP8 等效算力低于 BF16 峰值，主要损耗来自额外的 Dequantize 指令开销。

## Evidence

[质询]数值量级与效率系数缺乏来源支持：来源仅证实4090不支持原生FP8，但未提供'66-99 TFLOPS'的具体等效算力数值或'0.4-0.6'的效率系数，该具体数值属于经验事实且无外部证据直接支持。 | 来源[1]直接支持'RTX 4090缺乏原生FP8硬件支持'这一核心前提（AssertionError: Device compute capability 9.x required），但参考来源未覆盖具体的等效算力数值（66-99 TFLOPS）及效率系数（0.4-0.6），属于经验事实缺来源支持。

## Search Query

RTX 4090 FP8 inference efficiency TensorRT-LLM dequantize overhead effective FLOPS

## Retrieval Sources

- {'url': 'https://forums.developer.nvidia.com/t/4090-doesnt-have-fp8-compute/232256&rut=abcef42d1f68f7c3b3f56e9fcd4a36865268d696ae9dd8b33bc0eecdaf470139', 'type': 'ddg', 'title': "4090 doesn't have fp8 compute? - NVIDIA Developer Forums"}
