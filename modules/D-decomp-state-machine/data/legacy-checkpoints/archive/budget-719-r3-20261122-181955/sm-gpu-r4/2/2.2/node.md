# N15: KV Cache内存需求公式与计算：KV Cache Size = 2 * n_layers * n_kv_heads * head_dim * seq_len

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

KV Cache内存需求公式与计算：KV Cache Size = 2 * n_layers * n_kv_heads * head_dim * seq_len * dtype_size；需代入Qwen3-27B具体参数（层数、KV头数、头维度）计算32K tokens下BF16/FP8 KV Cache的内存占用（GB）。

## Corrected Claim

KV Cache内存需求仅针对16个全注意力层计算：KV Cache Size = 2 * 16 * n_kv_heads * head_dim * seq_len * dtype_size；其余48层Gated DeltaNet使用固定大小状态，不随seq_len线性增长。

## Evidence

[质询]该陈述假设所有层都使用标准全注意力机制并统一应用KV Cache公式，但参考来源明确指出Qwen3-27B（或Qwen3.8-27B）采用混合架构，仅16层使用全注意力（Full Attention），其余48层使用Gated DeltaNet（固定大小状态），因此直接套用全层数计算会严重高估内存需求。 | 来源[1]和[3]指出模型仅16层保留经典KV cache，其余48层为固定状态，与陈述中隐含的全层KV cache假设矛盾，导致具体数值计算错误，但公式本身对全注意力层是逻辑自洽的。

## Search Query

Qwen3-27B architecture layers kv heads head dimension KV cache memory 32k tokens

## Retrieval Sources

- {'url': 'https://www.aieev.com/post/qwen3-8-27b-benchmark&rut=c09bee931b9ecc6edd7643b2b3993bcc415dbc9bf5be42327678ebe390e8d39e', 'type': 'ddg', 'title': 'Qwen3.8-27B Benchmarks: Throughput, Latency and KV Cache'}
- {'url': 'https://liminalml.com/concepts/qwen-3-8-27b&rut=bbecd786dd0f8adb1e9f873a31f18e42ae64073dc67e903cfaa166c28ec76741', 'type': 'ddg', 'title': 'Qwen3.8-27B: Architecture Explained · LiminalML'}
- {'url': 'https://llmconfigurator.com/en/blog/qwen3-8-27b-which-quant-12-16-24-32gb&rut=5d8ed0e10338265520f7bee880e52e7af8da8bc5890d2cde6777edb6fb3eef95', 'type': 'ddg', 'title': 'Qwen3.8-27B: Best Quant for 12, 16, 24 and 32 GB'}
