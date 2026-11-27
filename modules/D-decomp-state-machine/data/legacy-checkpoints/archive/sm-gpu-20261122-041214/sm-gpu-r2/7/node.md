# N45: FP8 与 INT8 在长上下文（32K+）下的精度衰减差异：FP8 由于保留了指数位，在长序列累积误差方面通常优于 INT8，预计 FP8 在 32K 上下文

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

FP8 与 INT8 在长上下文（32K+）下的精度衰减差异：FP8 由于保留了指数位，在长序列累积误差方面通常优于 INT8，预计 FP8 在 32K 上下文下的困惑度 (Perplexity) 增加 <0.5%，而 INT8 可能增加 1-2%，因此若预算允许，FP8 是更稳健的质量选择 [待核验]。

## Corrected Claim

FP8 由于保留了指数位，具有更大的动态范围，在长序列累积误差方面通常优于 INT8。若预算允许，FP8 通常是更稳健的质量选择，但具体精度衰减幅度需视模型和量化策略而定。

## Evidence

[质询]具体数值（FP8 <0.5%, INT8 1-2%）缺乏直接来源支持，且长上下文下的精度衰减受模型架构、量化策略（如SmoothQuant）及具体任务影响极大，通用化数值可能不准确。 | 来源[1]和[2]支持FP8因保留指数位在动态范围上优于INT8的定性结论，但未提供32K上下文下具体的Perplexity增加数值，属于经验事实缺具体数据支持。

## Retrieval Sources

- {'url': 'https://arxiv.org/html/2303.17951v2&rut=09427c5f57dfbe9ba05244d4de11fc3cd6231d63f30479b218b5cbc7f7e38b26', 'type': 'ddg', 'title': 'FP8 versus INT8 for efficient deep learning inference - arXiv.org'}
- {'url': 'https://zhuanlan.zhihu.com/p/694120813&rut=d42b5056aa2ba8bfc05f86e200a2372fb94b59cdb6f27e20eacef35d097342ec', 'type': 'ddg', 'title': 'LLM推理量化：FP8 versus INT8 - 知乎'}
