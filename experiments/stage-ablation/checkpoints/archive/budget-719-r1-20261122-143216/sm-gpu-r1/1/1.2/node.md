# N7: 32K 上下文窗口的 KV Cache 显存占用量，计算公式为 2 × num_layers × num_kv_heads × head_dim × seq_l

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

32K 上下文窗口的 KV Cache 显存占用量，计算公式为 2 × num_layers × num_kv_heads × head_dim × seq_len × bytes_per_elem，需基于 Qwen3-27B 具体架构参数（层数、KV头数、头维度）计算得出具体 GB 值

## Corrected Claim

32K 上下文窗口的 KV Cache 显存占用量，计算公式为 2 × num_layers × num_kv_heads × head_dim × seq_len × bytes_per_elem，需基于 Qwen3-27B 具体架构参数（层数、KV头数、头维度）计算得出具体 GB 值（具体数值需查阅Qwen3-27B模型配置文件或技术报告详细章节）。

## Evidence

[质询]参考来源仅提供了Qwen3系列的总体介绍，未包含Qwen3-27B的具体架构参数（如层数、KV头数、头维度），因此无法从给定来源直接验证具体的GB数值计算结果，属于经验事实且缺乏直接数据支持。 | 公式逻辑自洽，但来源[1]未提供Qwen3-27B的具体架构参数，无法直接支持具体数值计算，属于经验事实缺来源支持。

## Search Query

Qwen3-27B architecture parameters num_layers num_kv_heads head_dim

## Retrieval Sources

- {'url': 'https://arxiv.org/pdf/2505.09388&rut=b2e4a11e75f738eaa7a2cbc209370eb0ea2a37600ec7cdaf0735ca8fc1f9204f', 'type': 'ddg', 'title': 'Qwen3 Technical Report - arXiv.org'}
