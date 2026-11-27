# N294: ΔPPL_32K = PPL_FP8_32K - PPL_BF16_32K，需基于 N134 和 N135 的具体数值计算得出，以量化 FP8 在长上下文下的累

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N97

## Claim

ΔPPL_32K = PPL_FP8_32K - PPL_BF16_32K，需基于 N134 和 N135 的具体数值计算得出，以量化 FP8 在长上下文下的累积误差。

## Corrected Claim

ΔPPL_32K = PPL_FP8_32K - PPL_BF16_32K，需基于 N134 和 N135 的具体数值计算得出，以量化 FP8 在长上下文下的累积误差。

## Evidence

先验知识/题面给定，逻辑校验通过
