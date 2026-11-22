# N316: BF16 精度下 Qwen3-27B 的权重显存占用 = 27.1e9 params * 2 bytes/param = 54.2 GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

BF16 精度下 Qwen3-27B 的权重显存占用 = 27.1e9 params * 2 bytes/param = 54.2 GB

## Corrected Claim

BF16 精度下 Qwen3-27B 的权重显存占用 = 27.1e9 params * 2 bytes/param = 54.2 GB

## Evidence

先验知识/题面给定，逻辑校验通过：27.1e9 * 2 bytes = 54.2e9 bytes = 54.2 GB，计算无误且符合BF16精度定义。
