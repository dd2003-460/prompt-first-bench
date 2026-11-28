# N5: Qwen3-27B 在 BF16 精度下的静态权重占用为 54 GB (27B * 2 bytes)，加上 32K 上下文 KV Cache 动态占用约 8-1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B 在 BF16 精度下的静态权重占用为 54 GB (27B * 2 bytes)，加上 32K 上下文 KV Cache 动态占用约 8-12 GB (取决于 GQA 头数与 batch size)，总最低显存需求约为 62-66 GB。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的静态权重占用为 54 GB (27B * 2 bytes)，加上 32K 上下文 KV Cache 动态占用约 8-12 GB (取决于 GQA 头数与 batch size)，总最低显存需求约为 62-66 GB。

## Evidence

[质询]KV Cache 估算范围（8-12 GB）依赖于具体的 GQA 配置和 Batch Size，若 Batch Size 较大或 Head 数不同，该数值可能偏差，但在典型推理场景下量级合理。 | 先验知识/题面给定，逻辑校验通过：27B参数*2字节=54GB权重，KV Cache估算符合常规LLM显存计算逻辑。
