# N220: Qwen3-27B 架构参数核验：确认 num_layers=28, num_kv_heads=8, head_dim=128 是否为官方配置；若实际 head

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N101

## Claim

Qwen3-27B 架构参数核验：确认 num_layers=28, num_kv_heads=8, head_dim=128 是否为官方配置；若实际 head_dim 为 128 且 num_kv_heads=8，则 KV Cache 公式中的系数固定为 2*28*8*128 = 57344 bytes/token (BF16)，需验证此参数组合是否导致 N130 中 3.98GB 与 N101 中 5.2GB 的数值差异（5.2GB 可能隐含了 batch_size>1 或不同的 seq_len 假设）。

## Corrected Claim

Qwen3-27B 的架构参数需以官方 config.json 为准。若 num_layers=28, num_kv_heads=8, head_dim=128，则 KV Cache 系数为 57344 bytes/token (BF16)。但需注意来源[2]提及的 64 个分层文件可能暗示不同的层数结构，需进一步核实。

## Evidence

[质询]来源[2]明确提到模型权重文件为 layers-0 至 layers-63，暗示层数可能为 64 而非 28；且来源[1]提到 32 层 GPU 卸载，与 28 层存在潜在冲突。此外，Qwen3-27B 的具体架构参数（如 num_layers, num_kv_heads）属于经验事实，需官方配置确认，当前来源未直接提供确切的 config.json 参数值。 | 逻辑上 KV Cache 计算公式 2*layers*kv_heads*head_dim*bytes 自洽，但来源[2]暗示层数可能为 64（layers-63），与 claim 中的 28 层矛盾或至少未直接支持 28 层这一具体数值；来源[1]和[3]未提供具体架构参数。经验事实缺直接来源支持。

## Search Query

Qwen3-27B config.json num_layers num_key_value_heads head_dim

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/171039142&rut=d99578b30cc781d880df0be1816a2b2aeb89ffbe3da059c75602aa740a3193e6', 'type': 'ddg', 'title': '16G显存跑Qwen3.8-27B 256K上下文的显存极限解析-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00238/article/details/151043054&rut=a1b707d3f778903e6a13d8ab1ef649aa2d9bad4cc2a563c17e7004632a2c1cfa', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 推理性能调优 10 个技巧：采样参数、输出长度与 KV Cache 优化-CSDN博客'}
- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=014253cab1362304bedfb232983060c3a30c933f269dd0e576935f19f65c4b6e', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
