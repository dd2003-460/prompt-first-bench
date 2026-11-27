# N26: 精度选择与硬件特性耦合：H100/A100 支持 FP8 Tensor Core，可实现 FP8 推理加速；RTX 4090/5090 不支持 FP8 推理，仅

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

精度选择与硬件特性耦合：H100/A100 支持 FP8 Tensor Core，可实现 FP8 推理加速；RTX 4090/5090 不支持 FP8 推理，仅支持 BF16/INT8，因此消费级卡上 FP8 量化无加速收益，仅减少显存占用。

## Corrected Claim

精度选择与硬件特性耦合：H100/A100 支持 FP8 Tensor Core，可实现 FP8 推理加速；RTX 4090 不支持 FP8 推理，仅支持 BF16/INT8，因此该卡上 FP8 量化无加速收益，仅减少显存占用；而 RTX 5090 支持 FP8 计算，可获得相应加速。

## Evidence

[质询]RTX 5090 (Blackwell架构) 实际上支持 FP8 计算（包括 Tensor Core 加速），陈述中将其与 RTX 4090 并列并声称不支持 FP8 推理加速，存在事实错误。 | 先验知识/题面给定，逻辑校验发现 RTX 5090 支持 FP8，与陈述矛盾，故降级。
