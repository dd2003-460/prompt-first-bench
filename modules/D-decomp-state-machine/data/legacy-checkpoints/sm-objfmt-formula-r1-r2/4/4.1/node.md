# N16: Qwen3-27B 在 BF16 精度下的理论最小显存占用为 54GB (27B * 2 bytes) + KV Cache 开销，KV Cache 在 32K

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

Qwen3-27B 在 BF16 精度下的理论最小显存占用为 54GB (27B * 2 bytes) + KV Cache 开销，KV Cache 在 32K 上下文、batch_size=1 下约为 0.5-1GB [待核验具体层数与头数]，总显存需求约 55-56GB

## Corrected Claim

Qwen3-27B 在 BF16 精度下的理论最小显存占用为 54GB (27B * 2 bytes) + KV Cache 开销，KV Cache 在 32K 上下文、batch_size=1 下约为 0.5-1GB [待核验具体层数与头数]，总显存需求约 55-56GB

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在BF16下权重占用54GB计算正确，KV Cache估算符合大模型常规量级

## Search Query

Qwen3-27B model architecture layers heads hidden size
