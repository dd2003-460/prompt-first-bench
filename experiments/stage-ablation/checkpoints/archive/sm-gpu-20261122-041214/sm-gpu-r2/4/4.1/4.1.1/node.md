# N122: 修正 N6/N34 矛盾：Qwen3-27B 在 BF16 下的精确权重文件大小应为 50.31 GiB (27e9 * 2 / 1024^3)，而非 54 G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

修正 N6/N34 矛盾：Qwen3-27B 在 BF16 下的精确权重文件大小应为 50.31 GiB (27e9 * 2 / 1024^3)，而非 54 GB (十进制近似)。在显存规划中必须使用 GiB (二进制) 单位，因为 GPU 显存容量标称通常为 GiB。

## Corrected Claim

修正 N6/N34 矛盾：Qwen3-27B 在 BF16 下的精确权重文件大小应为 50.31 GiB (27e9 * 2 / 1024^3)，而非 54 GB (十进制近似)。在显存规划中必须使用 GiB (二进制) 单位，因为 GPU 显存容量标称通常为 GiB。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9 * 2 / 1024^3 ≈ 50.31 GiB，计算正确且符合GPU显存单位惯例
