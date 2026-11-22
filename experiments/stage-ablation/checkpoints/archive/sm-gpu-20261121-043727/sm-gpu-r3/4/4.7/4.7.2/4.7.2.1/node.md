# N216: FP8 (E4M3) 量化对 Qwen3-27B 困惑度的具体影响系数：FP8 相比 INT8 具有更高的动态范围，PPL 增加率通常为 0.5-1.5%，低于

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N81

## Claim

FP8 (E4M3) 量化对 Qwen3-27B 困惑度的具体影响系数：FP8 相比 INT8 具有更高的动态范围，PPL 增加率通常为 0.5-1.5%，低于 INT8 的 1-3%，具体值取决于是否启用 SmoothQuant 等校准技术 [待核验]

## Corrected Claim

FP8 (E4M3) 量化相比 INT8 具有更高的动态范围，通常能带来更低的困惑度（PPL）增加，具体数值取决于模型规模、数据集及是否启用 SmoothQuant 等校准技术，一般认为 FP8 的精度损失小于 INT8。

## Evidence

[质询]陈述中给出的具体PPL增加率数值（FP8: 0.5-1.5%, INT8: 1-3%）属于经验事实，且不同模型、数据集及校准方法下波动较大，参考来源中未提供这些具体的量化对比数据，存在数值缺乏直接证据支持的风险。 | 来源[2]确认了Qwen3.8-27B-FP8采用E4M3格式及细粒度量化以保持精度，逻辑上支持FP8精度优于INT8的定性结论，但所有来源均未提供具体的PPL增加率数值，属于经验事实缺来源直接支持。

## Search Query

Qwen3 FP8 E4M3 quantization perplexity increase benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=90c2b8874e00fe7c65b297d67da0c9b8864d2183e939c714938b3ce2952db9f2', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00439/article/details/155257784&rut=0e8f0dfa7b87216743b85a5d74bfff004ee7d8a8930cbb0be7f745f60a0470f2', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 量化原理深度解析：块大小 128 的细粒度 FP8 如何保持精度无损？-CSDN博客'}
- {'url': 'https://www.modelscope.cn/models/Qwen/Qwen3.8-27B-FP8&rut=43d567f4cd5ae17b64f550f22ab64273ba3818e9461481b384c818a76dbe04f0', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 · Models'}
