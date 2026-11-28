# N331: 在 100 篇随机抽取的科研文本片段上，Qwen3.8-27B 与人类专家在定性主题编码（Thematic Coding）上的 Cohen's Kappa 系数

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N104, N105, N106

## Claim

在 100 篇随机抽取的科研文本片段上，Qwen3.8-27B 与人类专家在定性主题编码（Thematic Coding）上的 Cohen's Kappa 系数实测均值为 0.65，标准差 0.05；当引入 Chain-of-Thought 提示时，Kappa 提升至 0.72，但仍低于 0.80 的可发表级阈值。

## Corrected Claim

在缺乏具体实验数据支持的情况下，无法确认Qwen3.8-27B在科研文本主题编码上的Cohen's Kappa系数具体数值，仅能推断其可能具备中等水平的一致性。

## Evidence

[质询]参考来源仅涉及模型开源背景及通用性能评价，完全未提及‘科研文本片段’、‘定性主题编码’或‘Cohen's Kappa’等具体实验数据，无法验证该特定场景下的量化指标。 | 逻辑上Kappa值0.65-0.72符合大模型在复杂语义理解任务中通常表现（中等一致性），但作为经验事实，缺乏来源直接支持（来源[1]无关），故降级。

## Search Query

Cohen's Kappa LLM qualitative analysis human expert agreement thematic coding

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2076326126692185570&rut=2b419bbb28df927b509f204811130819b3a4ee03714f8e39cec41f5e43384a9a', 'type': 'ddg', 'title': '阿里开源 Qwen3.8-27B 本地实测：性能很强，但 Agent 适配仍待补课'}
