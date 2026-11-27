# N215: INT8 量化对 Qwen3-27B MMLU 分数的具体影响系数：在代码生成和数学推理子任务上，INT8 量化导致的分数下降通常为 0.5-1.5%，在常识推

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N80

## Claim

INT8 量化对 Qwen3-27B MMLU 分数的具体影响系数：在代码生成和数学推理子任务上，INT8 量化导致的分数下降通常为 0.5-1.5%，在常识推理子任务上下降接近 0%，加权平均后总 MMLU 下降约 0.5-1%，需以具体子任务权重为准 [待核验]

## Corrected Claim

INT8量化对Qwen3-27B MMLU分数通常有轻微负面影响，具体下降幅度需参考官方基准测试或特定量化实现报告，一般认为在1%以内，但不同子任务表现可能存在差异。

## Evidence

[质询]参考来源[1]讨论的是Qwen3.6-27B的FP8与INT8对比，且未提供MMLU具体子任务（代码/数学/常识）的量化下降系数数据，无法直接支持该陈述中具体的0.5-1.5%等数值范围；此外，Qwen3-27B与Qwen3.6-27B可能存在版本差异，来源相关性存疑。 | 逻辑上INT8量化对大模型性能影响较小符合常识，但参考来源[1]仅提及Qwen3.6-27B的量化版本对比，未提供MMLU子任务具体下降数据，属于间接/无关支持，且为经验事实，缺乏直接来源支持。

## Search Query

Qwen3 INT8 quantization MMLU score drop benchmark

## Retrieval Sources

- {'url': 'https://www.toutiao.com/article/7633052620612977167/&rut=4afdd7bcd56c88ffb2140c8952498cd5c3fb1f5d4e10a21551b80ce996d3e88f', 'type': 'ddg', 'title': 'Qwen3.6-27B量化大反转!FP8竟不如INT8，选模型必避的坑'}
