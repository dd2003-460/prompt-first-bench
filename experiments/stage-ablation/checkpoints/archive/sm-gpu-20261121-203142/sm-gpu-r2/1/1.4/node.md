# N10: KV Cache显存占用公式 = num_kv_heads * head_dim * 2 (bytes per token per layer) * num_l

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

KV Cache显存占用公式 = num_kv_heads * head_dim * 2 (bytes per token per layer) * num_layers * seq_len * 2 (K and V)；对于Qwen3-27B，若num_kv_heads=8, head_dim=128, num_layers=32，则每token每层占用=8*128*2*2=4096 bytes=4KB，32K tokens总KV Cache=4KB * 32K * 32 layers = 4GB [待核验: 需确认Qwen3-27B实际层数和KV头数]

## Corrected Claim

KV Cache显存占用公式 = num_kv_heads * head_dim * 2 (bytes per token per layer) * num_layers * seq_len * 2 (K and V)；对于Qwen3-27B，若假设num_kv_heads=8, head_dim=128, num_layers=32，则每token每层占用=8*128*2*2=4096 bytes=4KB，32K tokens总KV Cache=4KB * 32K * 32 layers = 4GB（注：具体参数需以官方模型配置为准）

## Evidence

[质询]Qwen3-27B的具体架构参数（num_kv_heads, num_layers）属于经验事实，参考来源仅提供了通用公式，未提供该特定模型的具体参数值，无法通过来源直接验证数值准确性。 | 来源[1][2][3]直接支持KV Cache显存占用的通用计算公式（num_kv_heads * head_dim * dtype_bytes * 2 * num_layers * seq_len），但均未提供Qwen3-27B的具体层数和KV头数，属于经验事实缺来源支持。

## Search Query

Qwen3-27B num_layers num_kv_heads head_dim config.json

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1668044&rut=1b109d08b5ca1e4a4f5eb0243eb8a595032fa2da34bde32e5865bd0828b1421f', 'type': 'ddg', 'title': '估算大模型推理KVCache显存占用与计算量-开发者社区-阿里云'}
- {'url': 'https://blog.csdn.net/kaka0722ww/article/details/163754312&rut=abc3da35094a8c1e766ee2595f39f3b81bb3d84a1b7eaeba2e48750de7708114', 'type': 'ddg', 'title': '小白必看!揭秘KV Cache显存占用公式+实测，收藏这篇轻松入门大模型优化!-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_35750747/article/details/170973349&rut=dde6da6b7faf3f7fa1342e1251c54817dbc77fcb37ab472c5256a326db60359b', 'type': 'ddg', 'title': 'GTC解读：当我们谈论 AI 推理的 KV Cache，我们在做什么？TaoToken 视角下的显存与吞吐权衡-CSDN'}
