# N7: 长上下文注意力衰减阈值：Qwen3.8-27b在262k上下文长度下，第10k-20k token位置的信息召回准确率（Recall@K）及首尾一致性偏差率，决

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

长上下文注意力衰减阈值：Qwen3.8-27b在262k上下文长度下，第10k-20k token位置的信息召回准确率（Recall@K）及首尾一致性偏差率，决定单次实验设计是否需分块处理。

## Corrected Claim

Qwen3.8-27B采用混合线性注意力架构以支撑262K长上下文，理论上能缓解注意力衰减，但第10k-20k token位置的具体信息召回准确率（Recall@K）及首尾一致性偏差率需通过实际基准测试确定，现有资料未提供确切数值以直接决定分块策略。

## Evidence

[质询]陈述中提到的具体指标（第10k-20k token位置的Recall@K及首尾一致性偏差率）属于具体的经验性能数据，参考来源仅讨论了架构原理（混合注意力、线性注意力）和显存/速度估算，并未提供该特定位置区间的精确召回率数值或偏差率统计，存在‘有架构支撑’不等于‘已知具体衰减阈值数值’的逻辑跳跃风险。 | 来源[1][2][3]证实了Qwen3.8-27B具备262K上下文能力及混合注意力架构以优化长上下文性能，但未提供第10k-20k token位置的具体Recall@K数值或偏差率，属于经验事实且缺乏直接数据支持。

## Search Query

Qwen3 27b long context attention decay benchmark recall rate 262k tokens

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00990/article/details/171490764&rut=0cf92ccfdbe3ba914c450bd1fd21a957ee4f5c63acbf9c45a5686c7e4fe35eec', 'type': 'ddg', 'title': 'Qwen3.8-27B-NVFP4-QAD完整拆解：64层混合线性注意力如何支撑262K长上下文-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29051193/article/details/163968270&rut=ec0c0d97f8c6b7ca6c2268aad6c2b292e7a9db128767a7588f3fc5e0e352374f', 'type': 'ddg', 'title': 'Qwen3.8 27B架构解析：MoE与线性注意力如何实现百万上下文-CSDN博客'}
- {'url': 'https://post.smzdm.com/p/al3xlppo/&rut=64f47eacde6ca523b71d82496df132268446f71fe5b650475fe432d11addbe40', 'type': 'ddg', 'title': 'Qwen3.8-27B，别让它停在 8K 上下文：262K 长上下文的显存账和速度账，16G/24G/48G 三档算清'}
