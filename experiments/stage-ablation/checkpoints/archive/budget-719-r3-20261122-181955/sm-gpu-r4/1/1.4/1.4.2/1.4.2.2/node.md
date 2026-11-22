# N192: Intel Max 1550 48GB 运行 Qwen3-27B 的显存余量分析：48GB 显存中，BF16 权重占 54GB（超出容量），因此必须使用 INT

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N59

## Claim

Intel Max 1550 48GB 运行 Qwen3-27B 的显存余量分析：48GB 显存中，BF16 权重占 54GB（超出容量），因此必须使用 INT8（27GB）或 INT4（13.5GB）量化；若使用 INT8，剩余 21GB 可用于 KV Cache，在 32K 上下文下可支持约 21GB / (KV per token) 个并发请求，具体并发数取决于 KV Cache 每 token 大小 [待核验]

## Corrected Claim

Intel Max 1550 48GB 运行 Qwen3-27B：BF16 权重约 54GB 超出容量，需使用 INT8（约 27GB）或 INT4（约 13.5GB）量化。若使用 INT8，剩余约 21GB 可用于 KV Cache。具体可支持的并发请求数或最大上下文长度，需结合 Qwen3-27B 的具体 KV Cache 每 token 大小（取决于层数、头数、GQA 比例等）进行计算，原陈述中'21GB / (KV per token) 个并发请求'的表述不严谨，应明确为'可存储的总 token 数'，再根据业务场景分配给并发请求。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应INT8和INT4两种量化场景，逻辑上互斥且互补，覆盖了父节点提出的两种主要方案；虽然计算结构相似，但属于不同参数配置下的独立结论，不构成冗余。）
