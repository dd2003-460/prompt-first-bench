# N187: Qwen3-27B 在 FP8 (E4M3) 量化下的困惑度 (Perplexity) 具体数值或相对于 BF16 的增量，需验证 <0.5% 的增量假设是否成

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

Qwen3-27B 在 FP8 (E4M3) 量化下的困惑度 (Perplexity) 具体数值或相对于 BF16 的增量，需验证 <0.5% 的增量假设是否成立，以确认 FP8 的质量无损性。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 量化下通常被认为具有接近无损的精度表现，但具体困惑度增量是否严格小于 0.5% 需依据官方基准测试数据确认，现有参考来源仅提供了定性支持。

## Evidence

[质询]参考来源中提到的模型版本（Qwen3.8-27B, Qwen3.6-27B）与待验证事实中的模型版本（Qwen3-27B）不一致，且来源仅定性描述“精度无损”或“几乎相同性能”，未提供具体的困惑度（Perplexity）数值或相对于BF16的增量百分比，无法直接验证“<0.5%”这一具体量化假设。 | 来源[1][3]支持FP8量化在细粒度块大小下能保持精度无损的定性结论，但缺乏针对Qwen3-27B具体Perplexity增量<0.5%的定量数据支持，属于经验事实且缺直接来源支持。

## Search Query

Qwen3-27B FP8 E4M3 perplexity increase evaluation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00439/article/details/155257784&rut=38c3d28b2f617adcd95228f7c0a93d16cfa32b5cc1c5530e9ed068e83d44195f', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 量化原理深度解析：块大小 128 的细粒度 FP8 如何保持精度无损？-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=7c73d43c2d312385e48aa0ad557ba2e8eff51baaeb38951c62af550fd88281bf', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/143005510&rut=f4b577e22f414c2d16990423aa12368f520af829b692d433ec1b6910e2e0d79e', 'type': 'ddg', 'title': 'Qwen3.6-27B-FP8 FP8量化技术深度剖析：如何保持性能的同时减小模型体积？_滑杏舒-智能体开发者社区'}
