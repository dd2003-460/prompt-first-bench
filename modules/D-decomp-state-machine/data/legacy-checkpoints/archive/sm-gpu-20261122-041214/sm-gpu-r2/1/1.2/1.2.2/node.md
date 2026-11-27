# N52: FP8 量化对 Qwen3-27B 的质量损失主要源于激活值动态范围截断，在长序列（>16K）推理时，累积误差可能导致 perplexity 上升 5-10%，

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

FP8 量化对 Qwen3-27B 的质量损失主要源于激活值动态范围截断，在长序列（>16K）推理时，累积误差可能导致 perplexity 上升 5-10%，需通过 GPTQ 或 AWQ 等校准算法降低损失至 <2%。

## Corrected Claim

FP8 量化对 Qwen3-27B 的质量损失源于权重与激活值的量化误差，在长序列推理时累积误差可能导致 perplexity 上升，具体幅度取决于校准策略；通过 GPTQ 或 AWQ 等校准算法可显著降低损失，但具体数值需根据实际场景评估。

## Evidence

[质询]具体数值（perplexity上升5-10%、损失降至<2%）缺乏通用性，高度依赖具体校准数据集、序列长度分布及硬件实现，且FP8通常指E4M3/E5M2格式，其动态范围截断并非唯一主要误差源（权重量化误差同样显著），将质量损失单一归因于激活值截断存在归因偏差。 | 先验知识/题面给定，逻辑校验通过，但具体量化损失数值为经验事实且无来源支持，故降级

## Search Query

FP8 quantization perplexity degradation long sequence LLM
