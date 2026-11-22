# N316: 推荐方案的敏感性边界示例：若用户接受 MMLU 损失 > 3% (允许 W4 量化)，则 2x RTX 4090 成为首选；若用户要求 MMLU 损失 < 1%

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

推荐方案的敏感性边界示例：若用户接受 MMLU 损失 > 3% (允许 W4 量化)，则 2x RTX 4090 成为首选；若用户要求 MMLU 损失 < 1% (仅允许 INT8/BF16)，则 1x A100 或 RTX 6000 Ada 成为首选。此边界条件需明确列出以避免无条件排名。

## Corrected Claim

推荐方案的敏感性边界示例：若用户接受 MMLU 损失 > 3% (允许 W4 量化)，则 2x RTX 4090 成为首选；若用户要求 MMLU 损失 < 1% (仅允许 INT8/BF16)，则 1x A100 或 RTX 6000 Ada 成为首选。此边界条件需明确列出以避免无条件排名。

## Evidence

检索失败: no sources from any channel (all 5 failed)
