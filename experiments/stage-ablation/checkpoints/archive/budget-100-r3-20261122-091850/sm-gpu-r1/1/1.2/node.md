# N8: 32K 上下文窗口下，KV Cache 显存占用量（GB）的计算公式：KV_Cache = 2 × num_layers × hidden_dim × num_

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

32K 上下文窗口下，KV Cache 显存占用量（GB）的计算公式：KV_Cache = 2 × num_layers × hidden_dim × num_kv_heads × bytes_per_element × seq_len。对于 Qwen3-27B，需确认 num_layers, hidden_dim, num_kv_heads 的具体值以计算单 token KV 大小及 32K 总量。

## Corrected Claim

32K 上下文窗口下，KV Cache 显存占用量（GB）的计算公式：KV_Cache = 2 × num_layers × hidden_dim × num_kv_heads × bytes_per_element × seq_len。对于 Qwen3-27B，需确认 num_layers, hidden_dim, num_kv_heads 的具体值以计算单 token KV 大小及 32K 总量。

## Evidence

公式逻辑自洽（2代表K和V，其余参数符合Transformer架构定义），来源[1]直接支持该KV Cache计算公式及32K上下文下的显存计算逻辑。

## Search Query

Qwen3-27B model config num_layers hidden_dim num_kv_heads

## Retrieval Sources

- {'url': 'https://bigolab.com/zh-hk/guides/5620-llm-kv-cache-vram-formula-32k-context-16gb-oom-guide&rut=5e3edd4e924e1419f0fbb9b70767309c1803c1ece5ce19806fef8d7109df2ca2', 'type': 'ddg', 'title': '大模型上下文 KV Cache 顯存計算公式詳解：為什麼 32K 上下文一開 16GB 顯卡就 OOM'}
- {'url': 'https://blog.csdn.net/weixin_29029995/article/details/169486381&rut=25fed840c3a0ade46cc17f3f4dd34ea6f054db26a1a79e0aa206dfffa3e06e9a', 'type': 'ddg', 'title': '24G显存跑四路32K上下文：KV Cache与模型权重显存占用深度解析-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_31458015/article/details/166875414&rut=419646d9e02620364295774813f2e5e1879400b633834b0d846d9b6856d5ff49', 'type': 'ddg', 'title': '四路24GiB显卡跑32K上下文：显存账本与KV Cache优化-CSDN博客'}
