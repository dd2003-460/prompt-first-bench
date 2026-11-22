# N236: 共享随机源 R_commission：主流二手平台（如闲鱼、eBay、Mercari）的佣金率 f 服从混合分布，其核心驱动变量为商品类目（Category）与

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N70

## Claim

共享随机源 R_commission：主流二手平台（如闲鱼、eBay、Mercari）的佣金率 f 服从混合分布，其核心驱动变量为商品类目（Category）与卖家等级（Seller_Tier），f = f_base(Category) + δ_tier(Seller_Tier) + ε，其中 ε ~ N(0, 0.005²) 为市场波动噪声。

## Corrected Claim

主流二手平台（如闲鱼、eBay、Mercari）的佣金率 f 主要受商品类目（Category）与卖家等级（Seller_Tier）影响，通常表现为基于类目的基础费率加上针对特定卖家等级的调整项，具体数值因平台政策而异，且存在市场波动。

## Evidence

[质询]该陈述将复杂的平台佣金机制简化为线性加性模型（f = f_base + δ_tier + ε），并指定噪声服从正态分布 N(0, 0.005²)。实际上，主流二手平台（如闲鱼、eBay）的佣金结构通常是非线性的、阶梯式的或基于固定比例加固定费用的，且不同平台的费率结构差异巨大，无法用一个统一的混合分布和简单的正态噪声项来准确描述。此外，0.005的标准差（即0.5%的波动）对于佣金率而言可能过于理想化，缺乏实证数据支持。 | 先验知识/题面给定，逻辑校验通过，但模型假设过于简化，缺乏实证支持，降级为定性表述。

## Search Query

average commission rate second hand marketplace eBay Mercari by category
