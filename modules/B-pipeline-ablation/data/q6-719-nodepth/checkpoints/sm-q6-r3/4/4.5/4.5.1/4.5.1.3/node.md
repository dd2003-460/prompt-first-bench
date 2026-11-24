# N295: Spare_Part_Inventory_CapEx = Σ(POP_i × Critical_Components_i × Component_Price_i

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

Spare_Part_Inventory_CapEx = Σ(POP_i × Critical_Components_i × Component_Price_i × Safety_Stock_Factor)，其中 Critical_Components 包括硬盘、内存、网卡，Safety_Stock_Factor 通常为 1-2 倍（基于 MTTR 与供货周期），此项为固定持有成本，需计入隐性运维总成本。

## Corrected Claim

Spare_Part_Inventory_CapEx = Σ(POP_i × Critical_Components_i × Component_Price_i × Safety_Stock_Factor)，其中 Critical_Components 包括硬盘、内存、网卡，Safety_Stock_Factor 通常为 1-2 倍（基于 MTTR 与供货周期），此项为固定持有成本，需计入隐性运维总成本。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

spare parts inventory cost calculation for distributed edge nodes
