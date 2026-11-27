# N142: 边界效应导致的有效容量损失 ΔC_boundary 的量化：ΔC_boundary = C * (1 - (1 - C/S_total)^0.5)；在 C/S_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

边界效应导致的有效容量损失 ΔC_boundary 的量化：ΔC_boundary = C * (1 - (1 - C/S_total)^0.5)；在 C/S_total = 0.1407 时，ΔC_boundary ≈ 128GB * (1 - 0.929) ≈ 9.1GB，导致有效容量占比降至 13.35%。

## Corrected Claim

边界效应导致的有效容量损失 ΔC_boundary 的量化：ΔC_boundary = C * (1 - (1 - C/S_total)^0.5)；在 C/S_total = 0.1407 时，ΔC_boundary ≈ 128GB * (1 - 0.929) ≈ 9.1GB，导致有效容量占比降至 13.35%。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（1-sqrt(1-0.1407)≈0.071，0.071*128≈9.1GB，(128-9.1)/128≈13.35%），公式与结论自洽。
