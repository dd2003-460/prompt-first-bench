# N20: 工作点B（中成本最优性价比）：混合架构（本地V100处理80%常规任务+云端API处理20%复杂推理），每日总成本≈$35，幻觉率<3%，MTTR<15min，

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

工作点B（中成本最优性价比）：混合架构（本地V100处理80%常规任务+云端API处理20%复杂推理），每日总成本≈$35，幻觉率<3%，MTTR<15min，边际收益/成本比最高

## Corrected Claim

工作点B（中成本最优性价比）：采用混合架构（本地V100处理大部分常规任务+云端API处理复杂推理），旨在平衡成本与性能，预期具有较低的边际收益/成本比，但具体每日成本、幻觉率及MTTR需根据实际业务负载和模型表现进行实测评估。

## Evidence

[质询]该陈述包含具体的经验性数值（每日成本$35、幻觉率<3%、MTTR<15min），这些并非第一性原理可推导的数学或物理事实，而是依赖于特定业务负载、模型版本及运维策略的经验数据。参考来源仅涉及Qwen3.8-27B在V100上的部署基准测试，未提供关于混合架构成本效益、幻觉率或MTTR的具体数据，因此缺乏直接外部证据支持这些具体数值。 | 逻辑上混合架构降低成本的思路自洽，但具体数值（$35, <3%, <15min）属于经验事实，参考来源[1]仅讨论本地部署性能，未覆盖成本、幻觉率或运维指标，无法提供直接支持。

## Search Query

cloud API cost per token complex reasoning vs local GPU inference cost efficiency comparison

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072074634476909289&rut=d97b6d9efd23719ef153d2ef7ccd044b4627c803640d57d09052962666bf48ca', 'type': 'ddg', 'title': 'Qwen3.8-27B 实测：V100 上的部署要点与 Q4/Q8 全量基准'}
