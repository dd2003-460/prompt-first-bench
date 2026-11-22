# N140: RTX 5090 32GB 显存下 Qwen3-27B BF16 权重的精确占用计算：Weight_Bytes = 27e9 * 2 bytes = 54 GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

RTX 5090 32GB 显存下 Qwen3-27B BF16 权重的精确占用计算：Weight_Bytes = 27e9 * 2 bytes = 54 GB，远超 32GB 显存上限，结论为 BF16 单卡推理不可行，必须采用量化（FP8/INT8）或多卡方案。

## Corrected Claim

RTX 5090 32GB 显存下 Qwen3-27B BF16 权重的精确占用计算：Weight_Bytes = 27e9 * 2 bytes = 54 GB，远超 32GB 显存上限，结论为 BF16 单卡推理不可行，必须采用量化（FP8/INT8）或多卡方案。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9参数 * 2字节/参数 = 54GB，54GB > 32GB，数学推导正确且符合硬件常识。
