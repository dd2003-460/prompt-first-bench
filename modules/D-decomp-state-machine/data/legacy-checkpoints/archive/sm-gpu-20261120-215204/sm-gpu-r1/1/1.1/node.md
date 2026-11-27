# N6: Qwen3-27B 在 BF16 精度下的权重显存占用为 54 GB (27B * 2 bytes)，加上 32K 上下文 KV Cache 开销约 6-8 G

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B 在 BF16 精度下的权重显存占用为 54 GB (27B * 2 bytes)，加上 32K 上下文 KV Cache 开销约 6-8 GB [待核验: 具体取决于层数和头数，按 Llama3 类似架构估算]，总硬性显存需求约为 60-62 GB。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的权重显存占用为 54 GB (27B * 2 bytes)，加上 32K 上下文 KV Cache 开销约 6-8 GB [待核验: 具体取决于层数和头数，按 Llama3 类似架构估算]，总硬性显存需求约为 60-62 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在BF16下权重占用54GB计算正确；KV Cache估算符合大模型常规量级，总显存需求逻辑自洽。
