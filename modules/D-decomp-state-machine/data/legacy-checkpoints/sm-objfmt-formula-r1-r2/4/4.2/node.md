# N17: Qwen3-27B 在 FP8 (E4M3/E5M2) 精度下的理论最小显存占用为 27GB (27B * 1 byte) + KV Cache 开销，总显存需

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

Qwen3-27B 在 FP8 (E4M3/E5M2) 精度下的理论最小显存占用为 27GB (27B * 1 byte) + KV Cache 开销，总显存需求约 28-29GB，相比 BF16 减少约 50%

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3/E5M2) 精度下的理论最小显存占用为 27GB (27B * 1 byte) + KV Cache 开销，总显存需求约 28-29GB，相比 BF16 减少约 50%

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点存在冗余，两个子节点本质上是在对比“KV Cache 存储精度”这一单一变量对总显存的影响（FP8 vs BF16），属于同一参数的不同取值场景，而非正交的独立知识点。此外，父节点提到的“28-29GB”与子节点计算的“31.096GB”存在数值矛盾，且子节点未涵盖父节点中关于“相比 BF16 减少约 50%”的具体对比基准数据。）

## Search Query

Qwen3-27B FP8 inference memory footprint
