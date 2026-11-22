# N227: 异质性对均衡稳定性的影响：若 σ²_seller 较大，卖家挂价分布的尾部会更厚，导致极端高挂价商品增多，进而增加买家搜索成本 T_search，量化为 T_s

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N81

## Claim

异质性对均衡稳定性的影响：若 σ²_seller 较大，卖家挂价分布的尾部会更厚，导致极端高挂价商品增多，进而增加买家搜索成本 T_search，量化为 T_search' = T_search * (1 + κ * σ_seller)，其中 κ 为搜索摩擦系数，需验证 κ * σ_seller 是否显著。

## Corrected Claim

异质性对均衡稳定性的影响：若 σ²_seller 较大，卖家挂价分布的尾部会更厚，导致极端高挂价商品增多，进而可能增加买家搜索成本 T_search。具体量化关系需依赖特定的搜索模型假设，不能简单断定为 T_search' = T_search * (1 + κ * σ_seller)。

## Evidence

[质询]该陈述将异质性（σ²_seller）对搜索成本的影响量化为线性公式 T_search' = T_search * (1 + κ * σ_seller)，缺乏微观基础支持。在标准搜索理论中，搜索成本通常取决于匹配概率或信息获取难度，而非直接由卖家价格分布的标准差线性决定；且公式中混用了方差（σ²）描述分布特征与标准差（σ）计算成本，逻辑上不够严谨，属于缺乏实证或理论推导支持的任意设定。 | 先验知识/题面给定，逻辑校验发现公式缺乏理论依据且量纲/变量使用存在瑕疵（方差与标准差混用），无法确认为通用真理，故降级。

## Search Query

price dispersion seller heterogeneity search cost market equilibrium
