# N61: KV Cache 精度独立性：KV Cache 通常保持 BF16 存储以保证注意力计算精度，即使权重为 FP8/INT8。因此 KV Cache 大小不随权重

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

KV Cache 精度独立性：KV Cache 通常保持 BF16 存储以保证注意力计算精度，即使权重为 FP8/INT8。因此 KV Cache 大小不随权重精度减半，仅当使用 FP8 KV Cache 优化时减半至约 3.9 GB。需确认推理引擎是否支持 FP8 KV Cache。

## Corrected Claim

KV Cache 精度独立性：KV Cache 通常保持 BF16 存储以保证注意力计算精度，即使权重为 FP8/INT8。因此 KV Cache 大小不随权重精度减半，仅当使用 FP8 KV Cache 优化时减半至约 3.9 GB。需确认推理引擎是否支持 FP8 KV Cache。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 精度通常独立于权重精度，默认保持 BF16 以保障注意力计算稳定性，仅在特定优化下使用 FP8 减半大小，符合主流推理引擎（如 vLLM, TensorRT-LLM）的工程实践。

## Search Query

FP8 KV cache support vLLM TensorRT-LLM precision independent of weights
