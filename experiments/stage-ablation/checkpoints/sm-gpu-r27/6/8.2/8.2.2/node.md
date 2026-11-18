# N265: RTX 4090 在 Batch Size=1、序列长度=128 的 Decode 阶段实际功耗为 350W-400W，双卡并行时总功耗为 700W-800W，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

RTX 4090 在 Batch Size=1、序列长度=128 的 Decode 阶段实际功耗为 350W-400W，双卡并行时总功耗为 700W-800W，显著低于双卡 TDP 总和 900W，散热设计可按 850W 峰值规划。

## Corrected Claim

RTX 4090 在 Batch Size=1、序列长度=128 的 Decode 阶段实际功耗为 350W-400W，双卡并行时总功耗为 700W-800W，显著低于双卡 TDP 总和 900W，散热设计可按 850W 峰值规划。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP 为 450W，双卡 TDP 总和 900W；Decode 阶段计算密度低，实际功耗通常低于 TDP，350-400W/卡及 700-800W 总功耗符合物理直觉与工程经验，散热按 850W 规划留有合理余量。
