# N349: B200 在 32K 上下文下的单请求 Decode 阶段理论 TPS 上限：T_min = 54GB / 8TB/s = 6.75ms，即理论最大 148 t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

B200 在 32K 上下文下的单请求 Decode 阶段理论 TPS 上限：T_min = 54GB / 8TB/s = 6.75ms，即理论最大 148 tokens/s；考虑 70% 带宽利用率，实际理论峰值约 104 tokens/s，远高于 H100 (3.35TB/s) 的 44 tokens/s (理论) / 30 tokens/s (实际)。

## Corrected Claim

B200 在 32K 上下文下的单请求 Decode 阶段理论 TPS 上限：T_min = 54GB / 8TB/s = 6.75ms，即理论最大 148 tokens/s；考虑 70% 带宽利用率，实际理论峰值约 104 tokens/s，远高于 H100 (3.35TB/s) 的 44 tokens/s (理论) / 30 tokens/s (实际)。

## Evidence

先验知识/题面给定，逻辑校验通过：B200 HBM3e带宽约8TB/s，H100 HBM3带宽约3.35TB/s，数值量级符合硬件规格常识；计算逻辑（54GB/8TB/s=6.75ms -> 148 TPS）自洽。
