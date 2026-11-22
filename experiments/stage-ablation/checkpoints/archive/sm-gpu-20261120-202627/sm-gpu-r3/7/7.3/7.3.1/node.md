# N415: 低显存卡 (如 RTX 4080 16GB) 多卡聚合至满足 Qwen3-27B 运行需求的最小卡数计算：Qwen3-27B BF16 权重约 54GB + 3

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N134

## Claim

低显存卡 (如 RTX 4080 16GB) 多卡聚合至满足 Qwen3-27B 运行需求的最小卡数计算：Qwen3-27B BF16 权重约 54GB + 32K KV Cache 约 8.6GB ≈ 62.6GB 总需求。单卡 16GB 需 4 张卡 (64GB) 才能勉强容纳，或 3 张卡 (48GB) 需配合激进量化 (INT8) 和较短上下文，但 32K 上下文下 INT8 KV Cache 仍需 ~4.3GB，3卡 (48GB) 总余量极小，风险高。

## Corrected Claim

低显存卡 (如 RTX 4080 16GB) 多卡聚合至满足 Qwen3-27B 运行需求的最小卡数计算：Qwen3-27B BF16 权重约 54GB + 32K KV Cache 约 8.6GB ≈ 62.6GB 总需求。单卡 16GB 需 4 张卡 (64GB) 才能勉强容纳，或 3 张卡 (48GB) 需配合激进量化 (INT8) 和较短上下文，但 32K 上下文下 INT8 KV Cache 仍需 ~4.3GB，3卡 (48GB) 总余量极小，风险高。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB，32K上下文KV Cache约8.6GB，总需求约62.6GB；4张16GB卡（64GB）可容纳，3张卡（48GB）需量化且余量极小，计算逻辑自洽。
