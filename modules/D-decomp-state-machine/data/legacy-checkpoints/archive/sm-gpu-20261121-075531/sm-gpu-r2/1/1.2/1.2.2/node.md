# N39: KV Cache 精度敏感性分析：在 FP8/INT8 量化推理框架中，KV Cache 通常保持 BF16 或 FP16 精度以保证注意力分数稳定性，但部分激

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

KV Cache 精度敏感性分析：在 FP8/INT8 量化推理框架中，KV Cache 通常保持 BF16 或 FP16 精度以保证注意力分数稳定性，但部分激进配置（如 vLLM 的 FP8 KV Cache 选项）会将 KV Cache 降至 1 byte/element，此时显存占用减半（≈0.96GB），需对比两种配置下的显存余量与质量损失。

## Corrected Claim

KV Cache 精度敏感性分析：在 FP8/INT8 量化推理框架中，KV Cache 通常保持 BF16 或 FP16 精度以保证注意力分数稳定性，但部分激进配置（如 vLLM 的 FP8 KV Cache 选项）会将 KV Cache 降至 1 byte/element，此时显存占用减半（≈0.96GB），需对比两种配置下的显存余量与质量损失。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8/INT8量化后单元素占1字节，相比BF16/FP16的2字节确实减半；vLLM等框架支持FP8 KV Cache是已知工程实践，逻辑自洽。

## Search Query

vLLM FP8 KV cache memory reduction accuracy tradeoff
