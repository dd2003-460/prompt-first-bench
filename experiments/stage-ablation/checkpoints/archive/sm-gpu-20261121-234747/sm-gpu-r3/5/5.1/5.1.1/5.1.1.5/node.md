# N322: BF16 精度需求下的显存可行性：权重 54GB > 24GB，RTX 3090/4080S 均不可行；若业务强制要求 BF16，最低硬件门槛为 1×L40S 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N117

## Claim

BF16 精度需求下的显存可行性：权重 54GB > 24GB，RTX 3090/4080S 均不可行；若业务强制要求 BF16，最低硬件门槛为 1×L40S 48GB（仍不足，需 Offload）或 2×RTX 3090（48GB，仍不足，需 Offload），此条件下 N117 推荐方案失效，需升级至 N118 预算区间

## Corrected Claim

BF16 精度需求下的显存可行性：权重 54GB > 24GB，RTX 3090/4080S 均不可行；若业务强制要求 BF16，最低硬件门槛为 1×L40S 48GB（仍不足，需 Offload）或 2×RTX 3090（48GB，仍不足，需 Offload），此条件下 N117 推荐方案失效，需升级至 N118 预算区间

## Evidence

先验知识/题面给定，逻辑校验通过：54GB > 24GB 且 54GB > 48GB，显存不足结论成立，需 Offload 或升级硬件的逻辑自洽。

## Search Query

BF16 27B model minimum GPU memory requirement 32K context
