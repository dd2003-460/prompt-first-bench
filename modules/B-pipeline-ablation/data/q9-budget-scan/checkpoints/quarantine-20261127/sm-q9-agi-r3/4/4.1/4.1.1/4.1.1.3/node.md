# N177: Qwen3.8-27B 的单头维度 (head_dim) 确切值为 128，结合 hidden_size=4096 和 n_attention_heads=32

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62

## Claim

Qwen3.8-27B 的单头维度 (head_dim) 确切值为 128，结合 hidden_size=4096 和 n_attention_heads=32 计算得出 (4096/32=128)，用于确定每个 KV 头的存储字节数基础。

## Corrected Claim

Qwen3.8-27B 的单头维度 (head_dim) 确切值为 256，结合 hidden_size=6144 (24*256) 和 n_attention_heads=24 计算得出，用于确定每个 KV 头的存储字节数基础。

## Evidence

[质询]数值错误：参考来源 [3] 明确指出 Qwen3.8-27B 的 head_dim 为 256，且采用 GQA 结构（24 个 Q 头，4 个 KV 头），这与陈述中声称的 head_dim=128 及 n_attention_heads=32 直接矛盾。 | 来源 [3] 直接指出 head_dim 是 256，且 Q 头数为 24，与陈述中的 128 和 32 不符。

## Search Query

Qwen3.8-27B head_dim hidden_size attention heads configuration

## Retrieval Sources

- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=5f69e53cf37790b6e21cecf0865561f9a7b73267f9067ba9d47d24b7bad8b5fa', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
- {'url': 'https://blog.csdn.net/gitblog_00214/article/details/151452981&rut=73231565708a767b39eb096768ea4ab41a110326a890c98fd5d985f41a15720a', 'type': 'ddg', 'title': 'vLLM 部署 Qwen3.8-27B：高吞吐推理的显存优化与参数配置最佳实践-CSDN博客'}
- {'url': 'https://iqilian.com/learn/qwen38-gated-attention-24-4/&rut=3a957b4eb8c672c292d495868c6c604965706905085ebcd2f772ab7f3a4e6c52', 'type': 'ddg', 'title': 'Qwen3.8-27B 的 GQA：24 个 Q 头配 4 个 KV 头、head_dim 是 256'}
