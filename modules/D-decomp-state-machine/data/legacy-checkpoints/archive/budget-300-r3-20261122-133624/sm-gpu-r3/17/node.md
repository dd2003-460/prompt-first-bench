# N469: 推荐方案的条件性边界条件 1：若用户主要工作负载为长上下文推理（>32K tokens）且对延迟不敏感，推荐 1× RTX 6000 Ada (48GB) 或 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

推荐方案的条件性边界条件 1：若用户主要工作负载为长上下文推理（>32K tokens）且对延迟不敏感，推荐 1× RTX 6000 Ada (48GB) 或 1× A100 80GB；若工作负载为短上下文高并发（<4K tokens）且追求极致性价比，推荐 2× RTX 3090 (48GB) 或 1× RTX 5090 (32GB, FP8)。此条件性表述避免了无条件排名，强调了场景对硬件选择的决定性影响。

## Corrected Claim

推荐方案的条件性边界条件 1：若用户主要工作负载为长上下文推理（>32K tokens）且对延迟不敏感，推荐 1× RTX 6000 Ada (48GB) 或 1× A100 80GB；若工作负载为短上下文高并发（<4K tokens）且追求极致性价比，推荐 2× RTX 3090 (48GB) 或 1× RTX 5090 (32GB, FP8)。此条件性表述避免了无条件排名，强调了场景对硬件选择的决定性影响。

## Evidence

检索失败: no sources from any channel (all 5 failed)
