# N116: 时间衰减系数 β 的临界值推导：为使高挂价优势 α * ΔP 被时间抵消，需满足 β * T_stock > α * ΔP；假设 α=0.5, ΔP=0.2，则

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

时间衰减系数 β 的临界值推导：为使高挂价优势 α * ΔP 被时间抵消，需满足 β * T_stock > α * ΔP；假设 α=0.5, ΔP=0.2，则 β * T_stock > 0.1；若 T_stock=24h，则 β > 0.0042/h；需验证平台实际 β 是否大于此值，若 β < 0.0042，则高价商品在 48h 内仍保持流量优势，解释为何高挂价未导致流量断崖。

## Corrected Claim

时间衰减系数 β 的临界值推导：为使高挂价优势 α * ΔP 被时间抵消，需满足 β * T_stock > α * ΔP；假设 α=0.5, ΔP=0.2，则 β * T_stock > 0.1；若 T_stock=24h，则 β > 0.0042/h；需验证平台实际 β 是否大于此值，若 β < 0.0042，则高价商品在 48h 内仍保持流量优势，解释为何高挂价未导致流量断崖。

## Evidence

先验知识/题面给定，逻辑校验通过：不等式推导 β > (α * ΔP) / T_stock = (0.5 * 0.2) / 24 ≈ 0.004167 符合数学逻辑，量纲与数值量级合理。

## Search Query

algorithm time decay coefficient beta stock duration recommendation weight
