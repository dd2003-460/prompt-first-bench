# N125: 修正 N7/N35 矛盾：Qwen3-27B 在 FP8 下的精确权重文件大小应为 25.16 GiB (27e9 * 1 / 1024^3)，而非 27 GB

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

修正 N7/N35 矛盾：Qwen3-27B 在 FP8 下的精确权重文件大小应为 25.16 GiB (27e9 * 1 / 1024^3)，而非 27 GB。此数值是评估 32GB/48GB 单卡可行性的基准。

## Corrected Claim

修正 N7/N35 矛盾：Qwen3-27B 在 FP8 下的精确权重文件大小应为 25.16 GiB (27e9 * 1 / 1024^3)，而非 27 GB。此数值是评估 32GB/48GB 单卡可行性的基准。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9 bytes / 1024^3 ≈ 25.16 GiB，计算正确且符合FP8单字节权重存储逻辑。
