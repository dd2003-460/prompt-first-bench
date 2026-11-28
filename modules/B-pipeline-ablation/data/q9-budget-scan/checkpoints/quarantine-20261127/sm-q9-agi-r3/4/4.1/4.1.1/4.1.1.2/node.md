# N176: Qwen3.8-27B 的 KV 头数 (n_kv_heads) 确切值为 8，采用 Grouped Query Attention (GQA) 机制，此值直接

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62

## Claim

Qwen3.8-27B 的 KV 头数 (n_kv_heads) 确切值为 8，采用 Grouped Query Attention (GQA) 机制，此值直接决定单 Token KV 显存占用量的线性缩放系数。

## Corrected Claim

Qwen3.8-27B 采用 Grouped Query Attention (GQA) 机制，其 KV 头数 (n_kv_heads) 为 8（需查阅官方配置确认），该值决定了单 Token KV 显存占用的线性缩放系数。

## Evidence

[质询]来源摘要仅提及OOM现象和模型名称，未提供具体的架构参数（如n_kv_heads=8），无法从现有文本中直接提取该确切数值，存在来源信息缺失的风险。 | 来源[1]主题相关（讨论Qwen3.8-27B的KV缓存问题），但摘要内容未直接包含n_kv_heads的具体数值，仅能间接关联到KV缓存机制，缺乏直接数据支持。

## Search Query

Qwen3.8-27B n_kv_heads grouped query attention config

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2077080879210485277&rut=5ff7c6f71b9249d1c58cc6f2a02d08c7d37715b79a399d2846bd56080a590f75', 'type': 'ddg', 'title': '16G甜点卡跑Qwen3.8-27B，KV缓存怎么设？ - 知乎'}
