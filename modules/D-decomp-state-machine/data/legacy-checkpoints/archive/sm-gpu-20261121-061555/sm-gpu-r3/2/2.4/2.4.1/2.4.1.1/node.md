# N196: Qwen3-27B 在 BF16 精度下的模型权重显存占用精确值：Bytes = 27,000,000,000 * 2 = 54,000,000,000 byt

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

Qwen3-27B 在 BF16 精度下的模型权重显存占用精确值：Bytes = 27,000,000,000 * 2 = 54,000,000,000 bytes ≈ 50.29 GiB (54.0 GB)。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的模型权重显存占用精确值：Bytes = 27,000,000,000 * 2 = 54,000,000,000 bytes ≈ 50.29 GiB (54.0 GB)。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在BF16（2字节/参数）下占用54GB，换算为GiB约为50.29GiB，计算准确且符合硬件常识。
