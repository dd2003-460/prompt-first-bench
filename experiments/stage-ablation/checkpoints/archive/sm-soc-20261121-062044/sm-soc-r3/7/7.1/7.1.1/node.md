# N249: 单元格 n11 的具体计算：筛选条件为 P_markup > 15% 且 T_close < T_market_avg。T_market_avg 定义为同类目过

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N90

## Claim

单元格 n11 的具体计算：筛选条件为 P_markup > 15% 且 T_close < T_market_avg。T_market_avg 定义为同类目过去30天成交周期的中位数（而非均值，以抵抗极端值）。n11 的计数需排除同一卖家连续上架的重复商品，去重规则为 Seller_ID + Item_ID 唯一标识。

## Corrected Claim

单元格 n11 的具体计算：筛选条件为 P_markup > 15% 且 T_close < T_market_avg。T_market_avg 定义为同类目过去30天成交周期的中位数（而非均值，以抵抗极端值）。n11 的计数需排除同一卖家连续上架的重复商品，去重规则为 Seller_ID + Item_ID 唯一标识。

## Evidence

先验知识/题面给定，逻辑校验通过
