# N200: 数据时效性与来源标注规范：所有价格数据（如N63-N69）标记为[Time-Sensitive: 2024Q4]，需在最终推荐前通过实时电商API或供应商报价单

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

数据时效性与来源标注规范：所有价格数据（如N63-N69）标记为[Time-Sensitive: 2024Q4]，需在最终推荐前通过实时电商API或供应商报价单核验。所有性能参数（如N56-N62）标记为[Verified: Datasheet]，视为静态事实。所有基于社区反馈的效率系数（如N92的0.5-0.8）标记为[Estimate: Community Benchmark]，需在TCO模型中引入±20%的置信区间进行敏感性分析。

## Corrected Claim

数据时效性与来源标注规范：建议对价格数据标记时效性（如[Time-Sensitive]）并在推荐前核验；对性能参数标记来源（如[Verified: Datasheet]）；对基于社区反馈的系数标记为估计值（如[Estimate]）并在TCO模型中引入置信区间进行敏感性分析。

## Evidence

[质询]该陈述属于特定项目或文档的内部规范定义（如具体的标签格式、特定的置信区间数值±20%），而非通用的行业事实或第一性原理可推导的客观真理。参考来源仅提供了数据时效性和元数据标注的一般性理论框架，并未包含该特定规范的具体细节（如具体的标签字符串或特定的敏感性分析参数），因此无法通过外部来源直接验证其具体内容的正确性，只能确认其逻辑自洽。 | 逻辑自洽，但参考来源[1][2]仅涉及数据时效性和元数据标注的一般性原则，未直接支持该特定规范的具体标签格式和参数值，属于经验性/规范性事实，缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_43198581/article/details/140069434&rut=ad9fe3bcd46f7741c512a50e5fd5f5aa854e5e193764b54e2b3892da6617d625', 'type': 'ddg', 'title': '数据质量管理-时效性管理_数据时效规范-csdn博客'}
- {'url': 'https://blog.csdn.net/weixin_35094083/article/details/159743954&rut=57c7a1a420e703d7167b78bc5ccc0a83ccfadac02095b3f88c2c03c8601a296b', 'type': 'ddg', 'title': 'GTE+SeqGPT知识库治理：元数据标注、时效性标记、来源可信度分级体系-CSDN博客'}
