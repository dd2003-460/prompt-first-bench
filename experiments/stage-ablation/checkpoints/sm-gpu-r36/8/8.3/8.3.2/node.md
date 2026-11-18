# N268: H100 SXM 在 Qwen3-27B FP8 推理下的稳态平均功耗为 620W ± 10W，相比 BF16 降低约 5%，源于 FP8 计算单元能效比更高及

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83

## Claim

H100 SXM 在 Qwen3-27B FP8 推理下的稳态平均功耗为 620W ± 10W，相比 BF16 降低约 5%，源于 FP8 计算单元能效比更高及 KV Cache 访问模式变化，需作为 FP8 部署场景下的电力成本基准值。

## Corrected Claim

H100 SXM 在 Qwen3-27B FP8 推理下的稳态平均功耗预计低于 BF16 模式，具体数值需实测确定，FP8 部署可带来能效提升。

## Evidence

[质询]具体数值（620W ± 10W）及特定模型（Qwen3-27B）的功耗数据属于经验事实，参考来源中未包含该特定硬件在特定模型下的实测功耗数据，无法验证具体数值量级。 | 来源[2]间接支持FP8能降低计算成本和内存流量，从而可能降低功耗，但未提供H100 SXM在Qwen3-27B下的具体功耗数值；来源[1]无关。

## Search Query

H100 FP8 inference power consumption efficiency vs BF16 watts

## Retrieval Sources

- {'url': 'https://en.m.wikipedia.org/wiki/Mortal_Kombat', 'type': 'bing', 'title': 'Mortal Kombat - Wikipedia'}
- {'url': 'http://arxiv.org/abs/2601.18150v2', 'type': 'arxiv', 'title': 'FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learnin'}
