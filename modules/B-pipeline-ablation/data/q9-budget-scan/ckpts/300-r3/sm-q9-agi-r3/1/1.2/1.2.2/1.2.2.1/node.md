# N139: Qwen3.8-27B 的架构参数确认为 num_layers=64, num_kv_heads=8 (GQA), head_dim=128，总参数量约 27B

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

Qwen3.8-27B 的架构参数确认为 num_layers=64, num_kv_heads=8 (GQA), head_dim=128，总参数量约 27B，KV Cache 占比约 0.5% 的模型权重

## Corrected Claim

Qwen3.8-27B 的架构参数确认为 num_layers=64，总参数量约 27B；num_kv_heads=8 (GQA)、head_dim=128 及 KV Cache 占比约 0.5% 为推测或未经当前来源直接证实的参数。

## Evidence

[质询]参考来源仅确认了 num_layers=64 和总参数量 27B，但未提供 num_kv_heads=8、head_dim=128 的具体数值，也未提及 KV Cache 占比约 0.5% 这一具体比例，存在关键参数缺失和潜在的经验事实无据风险。 | 来源 [2] 直接支持 num_layers=64，来源 [1][3] 支持 27B 参数量；但 num_kv_heads、head_dim 及 KV Cache 占比缺乏直接来源支持，属于经验事实且逻辑自洽但缺来源直接覆盖。

## Search Query

Qwen3.8-27B model architecture num_layers num_kv_heads head_dim configuration.json

## Retrieval Sources

- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=24c9807de7f70da9f46218badaf35c18091a4c13296dd9331327324cafe58715', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
- {'url': 'https://blog.csdn.net/gitblog_00936/article/details/168246892&rut=177fa12ef31558d31d13ff07eebc70da4eccb6fc183df72c88c2e4cc015a5849', 'type': 'ddg', 'title': '如何读懂Qwen3.8-27B ONNX模型：64层混合注意力与256K长上下文架构完整指南-CSDN博客'}
- {'url': 'https://blog.csdn.net/2401_85375151/article/details/164094490&rut=eab245b2413e7fac7026852e4ccee1873e51cd48f619f08e824dc3e251986272', 'type': 'ddg', 'title': 'Qwen3.8-27B本地部署教程（全网最详细版）-CSDN博客'}
