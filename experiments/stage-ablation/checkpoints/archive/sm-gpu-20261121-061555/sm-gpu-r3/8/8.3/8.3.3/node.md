# N356: 线性注意力层的状态更新机制（如 Delta Rule）在推理时是否需要保留完整历史状态还是仅保留压缩状态（如 SSM 状态）需确认；若仅保留压缩状态，显存占用进

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125

## Claim

线性注意力层的状态更新机制（如 Delta Rule）在推理时是否需要保留完整历史状态还是仅保留压缩状态（如 SSM 状态）需确认；若仅保留压缩状态，显存占用进一步降低，但精度损失需通过 PPL 增量量化评估。

## Corrected Claim

线性注意力层的状态更新机制（如 Delta Rule）在推理时是否需要保留完整历史状态还是仅保留压缩状态（如 SSM 状态）需确认；若仅保留压缩状态，显存占用进一步降低，但精度损失需通过 PPL 增量量化评估。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Gated DeltaNet inference state compression memory footprint
