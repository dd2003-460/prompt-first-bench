# N58: NVFP4 与 INT4 在 27B 模型上的质量差异机制：NVFP4 保留指数位，动态范围更大，在长序列推理中累积误差比 INT4 低约 10-20%（基于 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

NVFP4 与 INT4 在 27B 模型上的质量差异机制：NVFP4 保留指数位，动态范围更大，在长序列推理中累积误差比 INT4 低约 10-20%（基于 perplexity 对比），因此在 32K 上下文场景下，NVFP4 的质量稳定性优于 INT4，尽管两者显存占用相近。

## Corrected Claim

NVFP4 保留指数位，动态范围更大，在长序列推理中累积误差通常比 INT4 低，因此在长上下文场景下，NVFP4 的质量稳定性优于 INT4，尽管两者显存占用相近。

## Evidence

[质询]具体数值（10-20%）和特定场景（32K上下文）缺乏来源直接支持，且NVFP4与INT4的显存占用是否完全相近取决于具体的块大小和校准策略，存在口径混淆风险。 | 来源[1]提供了Qwen3.6 27B在FP8/INT4/NVFP4下的基准测试，间接支持NVFP4在精度上优于INT4的定性结论，但未提供具体的10-20%误差差异数值及32K上下文下的稳定性对比数据。

## Search Query

NVFP4 vs INT4 quantization perplexity long sequence context error accumulation

## Retrieval Sources

- {'url': 'https://kaitchup.substack.com/p/qwen36-27b-quantization-fp8-vs-int4&rut=46a3ef4c1e19bf335707b9a3a907bb3af8df7a6545380c94d1c7a9abcf2b2a6f', 'type': 'ddg', 'title': 'Qwen3.6 27B Quantization: FP8 vs INT4 vs NVFP4'}
