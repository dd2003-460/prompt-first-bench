# N75: 公有云 CDN 缓存命中率 CHR_pub 对 B_served 的影响：B_served = B_total × (1 - CHR_pub)。公有云 CDN 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

公有云 CDN 缓存命中率 CHR_pub 对 B_served 的影响：B_served = B_total × (1 - CHR_pub)。公有云 CDN 因全球节点共享，CHR_pub 通常为 85-90%。需量化 CHR_pub 从 80% 增至 90% 时，B_served 降低 11.1%，对应带宽成本降低 11.1%。

## Corrected Claim

公有云 CDN 缓存命中率 CHR_pub 对 B_served 的影响：B_served = B_total × (1 - CHR_pub)。公有云 CDN 因全球节点共享，CHR_pub 通常为 85-90%。需量化 CHR_pub 从 80% 增至 90% 时，B_served 降低 50%，对应带宽成本降低 50%。

## Evidence

父节点级核验未通过：有冗余（子节点实质上是同一线性公式（Cost = B_total * (1-CHR) * UnitPrice）在三个不同CHR取值下的具体计算实例。虽然数值上正交且覆盖了父节点提到的80%-90%区间，但它们并非独立的逻辑维度，而是同一参数扫描的离散点，存在高度结构性冗余。）
