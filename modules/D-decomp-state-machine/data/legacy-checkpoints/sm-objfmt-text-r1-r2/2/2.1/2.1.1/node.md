# N41: Qwen3-27B 在 FP8 (E4M3) 精度下，针对数学推理 (GSM8K/MATH) 和代码生成 (HumanEval) 任务的准确率下降幅度通常为 0

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13, N14, N15

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下，针对数学推理 (GSM8K/MATH) 和代码生成 (HumanEval) 任务的准确率下降幅度通常为 0.5%-1.5%，低于通用困惑度 (Perplexity) 的增加幅度

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 精度下，针对数学推理和代码生成任务的准确率通常有轻微下降，具体幅度需参考官方技术报告或特定基准测试结果，一般认为低于通用困惑度的增加幅度。

## Evidence

[质询]参考来源中提到的模型版本（Qwen3.8/3.6）与陈述中的 Qwen3-27B 不一致，且来源摘要仅提及“保持性能”或“部署实战”，未提供 GSM8K/MATH/HumanEval 具体准确率下降 0.5%-1.5% 的量化数据，属于经验事实缺乏直接来源支持。 | 逻辑上 FP8 量化对推理任务影响较小符合直觉，但参考来源 [1][2][3] 均未提供具体的基准测试数值对比，且模型版本号存在差异，无法直接验证具体百分比范围，故降级。

## Search Query

Qwen3-27B FP8 quantization accuracy GSM8K HumanEval degradation benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=703955979b9fa5473f892e9cc833e8a83c17da81ae43d0b61ec72f10a13a0f3e', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00522/article/details/152001461&rut=e962f847fbde1f7870b27d43e3490e9d1b7c0436300838aa829c740346d573dd', 'type': 'ddg', 'title': '一文读懂 Qwen3.8-27B-FP8：FP8 量化、27B 参数与 262K 超长上下文-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/143005510&rut=7e7ceddc13d98217f5c36d870a51e6ed895abf0294f35eb8dc66e916c8a32a6f', 'type': 'ddg', 'title': 'Qwen3.6-27B-FP8 FP8量化技术深度剖析：如何保持性能的同时减小模型体积？_滑杏舒-智能体开发者社区'}
