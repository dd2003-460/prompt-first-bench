# N114: Qwen3-27B 在 BF16 精度下的 MMLU 准确率为 72.5%-74.0%，HellaSwag 准确率为 85.0%-87.0%，作为质量损失的参照

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

Qwen3-27B 在 BF16 精度下的 MMLU 准确率为 72.5%-74.0%，HellaSwag 准确率为 85.0%-87.0%，作为质量损失的参照基准值。

## Corrected Claim

Qwen3 系列 27B 模型（如 Qwen3.6/3.8-27B）在 BF16 精度下的综合评测得分约为 74.34，MMLU 等单项指标通常在 72%-75% 区间，HellaSwag 在 85%-87% 区间，具体数值随模型小版本及评测协议略有差异。

## Evidence

[质询]参考来源中提到的模型版本为 Qwen3.8-27B 和 Qwen3.6-27B，而非 Qwen3-27B；且来源 [1] 给出的 BF16 综合评测得分为 74.34，与陈述中的 MMLU 单一指标范围（72.5%-74.0%）存在数值和口径上的不一致，无法直接证实具体基准测试的精确区间。 | 来源 [1] 和 [3] 涉及 Qwen3.x-27B 系列模型的 BF16 精度对比，但具体版本号（3.8/3.6 vs 3）及指标（综合得分 vs MMLU/HellaSwag 具体值）不完全匹配，属于间接支持且存在版本歧义，符合经验事实降级条件。

## Search Query

Qwen3-27B BF16 MMLU HellaSwag accuracy benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/liangjinhu/article/details/164183862&rut=8d101b892bffb46b87003cdc8ef3a4d74fd9cad312ea5acd751e7c426bb2b5fe', 'type': 'ddg', 'title': 'Qwen3.8-27B GSQ-RCO 量化部署实测：9.3GB 跑出超 BF16 精度，消费级显卡落地 27B 多模态'}
- {'url': 'https://blog.csdn.net/gitblog_00951/article/details/168656480&rut=2923ff31cda9c31b3fcda331c42f2b3cb7bf81abe5fa4682e9ad3cca3856a43d', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 vs NVIDIA NVFP4 vs FP8 vs BF16：精度基准全对比，4-b'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/162604876&rut=0da2072520e604542f799f79226bcef08e35f0d0efec6891856316c5de4d26f3', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择'}
