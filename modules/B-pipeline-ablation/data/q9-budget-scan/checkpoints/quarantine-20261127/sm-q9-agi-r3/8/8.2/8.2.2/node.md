# N277: 将关键证据置于 Prompt 首尾 10% 区域后，Qwen3.8-27B 在长上下文（>16k tokens）任务中的事实召回准确率较未重排基线提升 12-1

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95

## Claim

将关键证据置于 Prompt 首尾 10% 区域后，Qwen3.8-27B 在长上下文（>16k tokens）任务中的事实召回准确率较未重排基线提升 12-15 个百分点，具体数值依赖于证据密度，需通过 A/B 测试标定。

## Corrected Claim

将关键证据置于 Prompt 首尾区域通常能改善长上下文任务的表现，但具体提升幅度（如12-15个百分点）需针对特定模型版本和任务场景进行A/B测试验证，现有公开部署基准未直接证实该具体数值。

## Evidence

[质询]参考来源主要关注部署性能（V100、vLLM、llama.cpp对比）和基准测试，未涉及Prompt结构优化（如首尾效应）对事实召回准确率的具体影响数值，存在来源与事实主题不匹配的风险。 | 逻辑上符合长上下文处理中‘首尾效应’（Lost in the Middle）的已知现象，但参考来源[1]仅涵盖部署与基础基准，未提供关于Prompt重排对准确率提升12-15个百分点的直接数据支持，属于经验事实且缺乏直接来源佐证。

## Search Query

Qwen 27B long context lost in middle mitigation recall improvement percentage

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072074634476909289&rut=e14e1b01b639a378ae8d7ef986fe88097d0f64a2bbbf119b0cbfae0037f1bd29', 'type': 'ddg', 'title': 'Qwen3.8-27B 实测：V100 上的部署要点与 Q4/Q8 全量基准'}
