# N141: 若 vLLM 在 V100 上确实实现了软件模拟的 FP8 KV Cache（即显存中存储 1 字节/元素），则需验证 CUDA Kernel 中 FP8 到 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34, N35, N38

## Claim

若 vLLM 在 V100 上确实实现了软件模拟的 FP8 KV Cache（即显存中存储 1 字节/元素），则需验证 CUDA Kernel 中 FP8 到 FP16 的反量化开销对 Attention 计算延迟的影响，预计会导致单 token 生成延迟增加 10-20%，需实测 tokens/sec 以确定净收益。

## Corrected Claim

若 vLLM 在 V100 上实现软件模拟的 FP8 KV Cache，需验证 CUDA Kernel 中 FP8 到 FP16 的反量化开销对 Attention 计算延迟的影响，具体延迟增加比例需实测 tokens/sec 以确定，预计会有显著开销但具体幅度取决于 Kernel 优化程度。

## Evidence

[质询]该陈述包含具体的性能预测数值（10-20%延迟增加），这属于经验事实。参考来源[1]仅介绍TensorRT支持的FP8格式，未涉及vLLM或V100上的具体性能开销；来源[2]讨论的是FP8量化在特定基准下的表现，但未提供V100上FP8 KV Cache反量化导致Attention延迟增加10-20%的具体数据或因果证明。此外，V100硬件本身不支持原生FP8计算单元，软件模拟的开销可能远高于此范围，或者因Kernel优化不同而有极大差异，缺乏直接证据支持该特定百分比区间。 | 逻辑上，低精度存储后需反量化会增加计算开销，方向合理；但具体数值10-20%为经验估计，参考来源[1][2]均未提供vLLM在V100上FP8 KV Cache的具体延迟增量数据，属于经验事实且缺乏直接来源支持。

## Search Query

FP8 dequantization overhead latency impact attention kernel V100 software emulation

## Retrieval Sources

- {'url': 'https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/work-with-quantized-types.html&rut=f94a20b8d59d67b61c2bebf27078ab1eacc8fb9ad32dee98280cbd7ca9762ed1', 'type': 'ddg', 'title': 'Working with Quantized Types — NVIDIA TensorRT'}
- {'url': 'https://github.com/aas008/spec-decode-benchmark-guide/blob/main/06-fp8-quantization.md&rut=dfc0a0977037e5ccf3e364cca6b3e92858892ee4a56888044eb53ad676daa7d2', 'type': 'ddg', 'title': 'spec-decode-benchmark-guide/06-fp8-quantization.md at main - GitHub'}
