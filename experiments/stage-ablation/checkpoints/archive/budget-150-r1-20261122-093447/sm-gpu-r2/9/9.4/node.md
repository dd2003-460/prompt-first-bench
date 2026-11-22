# N123: 显存容量与精度映射的交互效应：精度越低 (W4)，显存需求越小，但量化误差累积在长上下文 (32K) 下可能放大，导致输出质量下降；FP8 在 32K ctx 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N38

## Claim

显存容量与精度映射的交互效应：精度越低 (W4)，显存需求越小，但量化误差累积在长上下文 (32K) 下可能放大，导致输出质量下降；FP8 在 32K ctx 下的困惑度增加通常 < 1.5%，W4 可能 > 5% [待核验：需查 Qwen3-27B 官方量化报告或社区实测数据]

## Corrected Claim

精度越低 (W4)，显存需求越小，但量化误差在长上下文 (32K) 下通常比 FP8 更显著，可能导致输出质量下降；具体困惑度增加幅度取决于量化算法与评测基准，FP8 通常表现优于 W4，但具体数值需参考特定模型的实测报告。

## Evidence

[质询]具体数值（FP8 < 1.5%, W4 > 5%）缺乏针对 Qwen3-27B 在 32K 上下文下的直接实证支持，属于特定模型的经验性数据，不同量化算法（如 GPTQ, AWQ, GGUF）和评测基准会导致结果差异巨大，直接断言具体百分比存在以偏概全风险。 | 来源[1]仅提供了显存计算和量化概念的一般性解释，未包含 Qwen3-27B 在 32K 上下文下的具体困惑度（Perplexity）增加数值，无法直接支持或反驳具体的百分比阈值；该陈述为经验事实，逻辑自洽但缺来源直接支持。

## Search Query

Qwen3-27B quantization perplexity long context 32K

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/32811882452&rut=465f99098bdbe8d6affc1fe787d8ee1b57b61d574c04055ec2f42a17d9094f8a', 'type': 'ddg', 'title': '模型精度（FP16、FP8等），所需显存计算以及量化概念!'}
