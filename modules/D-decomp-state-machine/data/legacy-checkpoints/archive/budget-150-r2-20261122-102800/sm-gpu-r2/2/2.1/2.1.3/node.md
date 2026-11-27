# N77: 修正后的 INT8 显存占用：若 Embedding (0.68B params) 保持 BF16 (1.36 GB)，其余 26.5B params 为 IN

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

修正后的 INT8 显存占用：若 Embedding (0.68B params) 保持 BF16 (1.36 GB)，其余 26.5B params 为 INT8 (26.5 GB)，总权重显存 ≈ 27.86 GB (略高于 N13 的 27 GB 估算)。

## Corrected Claim

修正后的 INT8 显存占用：若 Embedding (0.68B params) 保持 BF16 (1.36 GB)，其余 26.5B params 为 INT8 (26.5 GB)，总权重显存 ≈ 27.86 GB (略高于 N13 的 27 GB 估算)。

## Evidence

先验知识/题面给定，逻辑校验通过：0.68B * 2 bytes = 1.36 GB，26.5B * 1 byte = 26.5 GB，总和 27.86 GB，计算无误且量级合理。
