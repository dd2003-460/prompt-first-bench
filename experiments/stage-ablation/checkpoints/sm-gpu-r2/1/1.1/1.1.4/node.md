# N41: KV Cache 精度策略：主流推理框架 (vLLM, SGLang, llama.cpp) 中，KV Cache 通常独立于权重精度，默认使用 BF16 (2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

KV Cache 精度策略：主流推理框架 (vLLM, SGLang, llama.cpp) 中，KV Cache 通常独立于权重精度，默认使用 BF16 (2 bytes) 或 FP16，即使权重为 W4/INT8，KV Cache 仍占 2 bytes/element 以保持注意力计算精度。

## Corrected Claim

KV Cache 精度策略：主流推理框架 (vLLM, SGLang, llama.cpp) 中，KV Cache 通常独立于权重精度，默认使用 BF16 (2 bytes) 或 FP16，即使权重为 W4/INT8，KV Cache 仍占 2 bytes/element 以保持注意力计算精度。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM KV cache precision independent of weight quantization
