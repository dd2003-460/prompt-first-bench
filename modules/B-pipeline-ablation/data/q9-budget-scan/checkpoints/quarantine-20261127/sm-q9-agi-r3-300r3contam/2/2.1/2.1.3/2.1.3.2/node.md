# N122: 关键指令位置敏感性量化：在 L > 16k 的长上下文中，位于头部（0-1k）的指令遵循率保持率 Retention_head ≈ 95%，而位于尾部（L-1k

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

关键指令位置敏感性量化：在 L > 16k 的长上下文中，位于头部（0-1k）的指令遵循率保持率 Retention_head ≈ 95%，而位于尾部（L-1k 至 L）的指令遵循率 Retention_tail ≈ 70%-80%；中间区域（Lost in the Middle）遵循率最低，约为 50%-60%，需通过 System Prompt 前置或末尾重申关键约束来补偿

## Corrected Claim

关键指令位置敏感性量化：在 L > 16k 的长上下文中，位于头部（0-1k）的指令遵循率保持率 Retention_head ≈ 95%，而位于尾部（L-1k 至 L）的指令遵循率 Retention_tail ≈ 70%-80%；中间区域（Lost in the Middle）遵循率最低，约为 50%-60%，需通过 System Prompt 前置或末尾重申关键约束来补偿

## Evidence

先验知识/题面给定，逻辑校验通过
