# N168: FP8/INT8 量化 KV Cache 的精度损失量化：在 32K 长上下文下，KV Cache 量化为 INT8 导致的 Perplexity 增加通常比权

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N49, N50, N51

## Claim

FP8/INT8 量化 KV Cache 的精度损失量化：在 32K 长上下文下，KV Cache 量化为 INT8 导致的 Perplexity 增加通常比权重量化额外增加 0.1-0.3%，需评估其对最终生成质量的影响是否在可接受阈值内。

## Corrected Claim

在 32K 长上下文下，KV Cache 量化为 INT8 通常会导致 Perplexity 轻微增加，具体幅度取决于量化方法和模型，需评估其对最终生成质量的影响是否在可接受阈值内。

## Evidence

[质询]具体数值范围（0.1-0.3%）缺乏普遍性，高度依赖模型架构、量化算法（如SmoothQuant, KIVI）及校准策略，且不同文献中报告的Perplexity增加幅度差异较大，直接断言该固定区间可能不准确。 | 来源[1]仅定性提及激进量化可能损害精度，未提供具体数值支持；该事实属于经验性工程数据，逻辑自洽但缺乏直接来源支持具体数值区间。

## Search Query

KV cache quantization INT8 perplexity increase long context

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Transformer_%28deep_learning%29', 'type': 'wikipedia', 'title': 'Transformer (deep learning)'}
