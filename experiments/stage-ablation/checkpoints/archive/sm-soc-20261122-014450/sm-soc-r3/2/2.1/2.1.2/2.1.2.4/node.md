# N168: c_check (单步成本) 的量化：c_check = c_data + c_attention。c_data 为流量成本（如 0.1元/次点击），c_att

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

c_check (单步成本) 的量化：c_check = c_data + c_attention。c_data 为流量成本（如 0.1元/次点击），c_attention 为注意力机会成本（如 0.5元/次）。需计算高挂价商品的总 C_verify 是否显著低于市场价商品，以验证 ΔC_verify < 0。

## Corrected Claim

c_check (单步成本) 的量化：c_check = c_data + c_attention。c_data 为流量成本（如 0.1元/次点击），c_attention 为注意力机会成本（如 0.5元/次）。需计算高挂价商品的总 C_verify 是否显著低于市场价商品，以验证 ΔC_verify < 0。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cost of clicking and browsing online marketplace items
