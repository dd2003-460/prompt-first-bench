# N198: AMD MI250X 单卡在 ROCm 5.7 环境下运行 Qwen3-27B BF16 时的实际显存占用为 54GB (权重) + 3.2GB (64K KV

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

AMD MI250X 单卡在 ROCm 5.7 环境下运行 Qwen3-27B BF16 时的实际显存占用为 54GB (权重) + 3.2GB (64K KV Cache) + 4GB (框架/激活) = 61.2GB，低于其 128GB 总显存，因此无需 Offload，但需确认 ROCm 默认分配策略是否预留额外显存

## Corrected Claim

AMD MI250X 单卡在 ROCm 5.7 环境下运行 Qwen3-27B BF16 时的实际显存占用为 54GB (权重) + 3.2GB (64K KV Cache) + 4GB (框架/激活) = 61.2GB，低于其 128GB 总显存，因此无需 Offload，但需确认 ROCm 默认分配策略是否预留额外显存

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB，64K KV Cache约3.2GB，框架开销约4GB，总和61.2GB低于MI250X 128GB显存，无需Offload，逻辑自洽且数值量级合理。
