# N69: Pareto 最优剩余恢复的基准线计算：Total_Surplus_Pareto = Σ(Buyer_WTP_i - Seller_Cost_i) - Σ(Se

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

Pareto 最优剩余恢复的基准线计算：Total_Surplus_Pareto = Σ(Buyer_WTP_i - Seller_Cost_i) - Σ(Search_Cost_i)。当前均衡下的剩余损失 (Deadweight_Loss) 量化为因高挂价导致的交易摩擦成本，具体数值为 ∫_{P_market}^{P_ask} (D(P) - S(P)) dP，其中 D 和 S 分别为需求供给曲线在溢价区间的积分差。

## Corrected Claim

Pareto 最优剩余恢复的基准线计算：Total_Surplus_Pareto = Σ(Buyer_WTP_i - Seller_Cost_i) - Σ(Search_Cost_i)。当前均衡下的剩余损失 (Deadweight_Loss) 量化为因高挂价导致的交易摩擦成本，具体数值为 ∫_{P_market}^{P_ask} (D(P) - S(P)) dP，其中 D 和 S 分别为需求供给曲线在溢价区间的积分差。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto最优剩余定义为总剩余减去搜索成本，死重损失（DWL）在存在价格扭曲（如高挂价）时确实表现为供需曲线在均衡价格与扭曲价格之间围成的面积，即积分差，符合微观经济学基本原理。

## Search Query

deadweight loss from price markup in online marketplace integration
