# N509: 在纯 Decode 阶段，RTX 5090 的实际吞吐量相对于 H100 的理论效率比为 87.88% (66.37/75.52)，该比值完全由显存带宽比决定，

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N156

## Claim

在纯 Decode 阶段，RTX 5090 的实际吞吐量相对于 H100 的理论效率比为 87.88% (66.37/75.52)，该比值完全由显存带宽比决定，与计算单元数量无关。

## Corrected Claim

在纯 Decode 阶段，RTX 5090 的实际吞吐量相对于 H100 的理论效率比为 87.88% (66.37/75.52)，该比值完全由显存带宽比决定，与计算单元数量无关。

## Evidence

先验知识/题面给定，逻辑校验通过：纯Decode阶段为显存带宽受限（Memory-Bound），吞吐量与显存带宽成正比，与计算单元无关；数值计算 66.37/75.52 ≈ 0.8788 准确无误。
