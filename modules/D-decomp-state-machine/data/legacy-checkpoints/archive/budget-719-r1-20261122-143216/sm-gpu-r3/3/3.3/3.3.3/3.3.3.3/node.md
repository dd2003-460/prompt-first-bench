# N251: 决策边界条件：2×RTX 4090 方案仅在 Batch Size > 8 且需要 >48GB 显存容量（无法被单卡满足）时才可能优于单卡大显存卡；在 Batc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N88

## Claim

决策边界条件：2×RTX 4090 方案仅在 Batch Size > 8 且需要 >48GB 显存容量（无法被单卡满足）时才可能优于单卡大显存卡；在 Batch=1 单用户场景下，其性价比始终低于单卡 RTX 5090 或 RTX 4090 (若显存足够)，因此不应作为首选推荐。

## Corrected Claim

决策边界条件：2×RTX 4090 方案仅在 Batch Size > 8 且需要 >48GB 显存容量（无法被单卡满足）时才可能优于单卡大显存卡；在 Batch=1 单用户场景下，其性价比始终低于单卡 RTX 5090 或 RTX 4090 (若显存足够)，因此不应作为首选推荐。

## Evidence

先验知识/题面给定，逻辑校验通过：2x4090 (48GB) 在 Batch=1 时受限于 PCIe 带宽和驱动开销，且成本高于单卡 5090/4090，仅在显存需求超过单卡上限且 Batch 较大时才有优势，符合硬件工程常识。

## Search Query

multi-GPU vs single-GPU inference cost efficiency batch size threshold
