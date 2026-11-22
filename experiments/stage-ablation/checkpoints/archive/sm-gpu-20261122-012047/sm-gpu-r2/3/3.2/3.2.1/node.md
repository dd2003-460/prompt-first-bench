# N96: 修正 N21 错误：RTX 4090 (Ada Lovelace架构) 不支持 FP8 Tensor Core 加速，仅支持 BF16/INT8/INT4；FP

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

修正 N21 错误：RTX 4090 (Ada Lovelace架构) 不支持 FP8 Tensor Core 加速，仅支持 BF16/INT8/INT4；FP8 加速仅在 Hopper (H100/H200) 及 Blackwell (B100/B200) 架构上生效。在 RTX 4090 上加载 FP8 权重仅减少显存占用，计算速度相比 BF16 无提升（甚至因软件模拟可能略慢），因此 RTX 4090 的 FP8 vs BF16 加速比为 1.0x。

## Corrected Claim

修正 N21 错误：RTX 4090 (Ada Lovelace架构) 不支持 FP8 Tensor Core 加速，仅支持 BF16/INT8/INT4；FP8 加速仅在 Hopper (H100/H200) 及 Blackwell (B100/B200) 架构上生效。在 RTX 4090 上加载 FP8 权重仅减少显存占用，计算速度相比 BF16 无提升（甚至因软件模拟可能略慢），因此 RTX 4090 的 FP8 vs BF16 加速比为 1.0x。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 (Ada Lovelace) 确实不支持原生 FP8 Tensor Core 加速，FP8 加速需 Hopper 或 Blackwell 架构支持，逻辑自洽且符合硬件规格事实。
