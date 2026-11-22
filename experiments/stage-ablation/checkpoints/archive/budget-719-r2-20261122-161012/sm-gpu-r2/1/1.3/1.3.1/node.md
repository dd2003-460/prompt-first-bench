# N41: 消费级主板 (如 Z790/X670) 通常仅提供 1 个物理 PCIe x16 插槽直连 CPU，其余插槽通过 PCH 提供且带宽受限 (通常为 x4 或 x

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

消费级主板 (如 Z790/X670) 通常仅提供 1 个物理 PCIe x16 插槽直连 CPU，其余插槽通过 PCH 提供且带宽受限 (通常为 x4 或 x8)，这限制了多卡并行推理时的数据吞吐，尤其是大 Batch 下的 All-Reduce 通信效率。

## Corrected Claim

消费级主板 (如 Z790/X670) 通常仅提供 1 个物理 PCIe x16 插槽直连 CPU，其余插槽通过 PCH 提供且带宽受限 (通常为 x4 或 x8)，这限制了多卡并行推理时的数据吞吐，尤其是大 Batch 下的 All-Reduce 通信效率。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Consumer motherboard PCIe lane allocation PCH bandwidth limit multi-GPU inference
