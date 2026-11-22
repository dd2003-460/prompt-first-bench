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

父节点级核验通过：正交+完备+无冗余（子节点B1、B2、B3分别对应父节点中的基准线计算、损失量化公式、以及基于前两者的恢复率评估，逻辑上层层递进且无重叠。B2对B1中定义的变量进行了具体的线性假设推导，属于细化而非重复；B3利用B1和B2的结果定义新指标，符合正交性要求。三者共同完整覆盖了父节点描述的‘基准线计算’、‘损失量化’及隐含的‘恢复评估’需求。）

## Search Query

deadweight loss from price markup in online marketplace integration
