# N108: INT4 (AWQ/GPTQ) 量化对 Qwen3-27B 的困惑度 (Perplexity) 增加具体数值（通常在 1.0-3.0% 范围内，且受量化算法影响

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

INT4 (AWQ/GPTQ) 量化对 Qwen3-27B 的困惑度 (Perplexity) 增加具体数值（通常在 1.0-3.0% 范围内，且受量化算法影响显著），需区分 AWQ 和 GPTQ 的差异 [待核验]

## Corrected Claim

INT4 (AWQ/GPTQ) 量化对 Qwen3-27B 的困惑度 (Perplexity) 通常有轻微增加，具体数值需查阅特定基准测试报告，一般认为在可接受范围内（如1%-3%左右），且受量化算法影响。

## Evidence

[质询]参考来源仅提供了量化方案（GPTQ/AWQ）的原理和模型规格，未提供具体的困惑度（Perplexity）增加数值（如1.0-3.0%），属于经验事实且缺乏直接数据支持。 | 来源[1][2][3]确认了Qwen3-27B存在INT4量化版本及AWQ/GPTQ算法，但均未给出具体Perplexity增量数值，逻辑上该范围合理但缺直接证据。

## Search Query

Qwen3-27B INT4 AWQ GPTQ perplexity degradation comparison

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00713/article/details/170621454&rut=e7ee03e7dc653f2619c6fb23cb65d32f42966be6d078d6262f2bf13b6b5ab964', 'type': 'ddg', 'title': '为什么量化几乎无损？Qwen3.8-27B-INT4 的 GPTQ W4A16 + AWQ 量化方案原理拆解-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00204/article/details/163501375&rut=45a0f468012803016727c2be27c66ab1b5deba2f39d2ae9a885ef3433354b257', 'type': 'ddg', 'title': '为什么选AWQ量化？Qwen3.8-27B-AWQ的INT4 W4A16原理与优势深度解析-CSDN博客'}
- {'url': 'https://blog.gitcode.com/d5806f487998608f8f55721d3336e544.html&rut=aaa667bb9d4e0db42068acb560a166563939180b8ee7eb805550dd6ad10c02ea', 'type': 'ddg', 'title': '为什么量化几乎无损？Qwen3.8-27B-INT4 的 GPTQ W4A16 + AWQ 量化方案原理拆解'}
