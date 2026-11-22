# N70: 搜索排序参数 Δγ_search：定义为排序算法中‘成交概率’权重与‘点击率’权重的比值变化，当前 γ_0 = w_CTR/w_Prob，干预后 γ_1 = w

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N16

## Claim

搜索排序参数 Δγ_search：定义为排序算法中‘成交概率’权重与‘点击率’权重的比值变化，当前 γ_0 = w_CTR/w_Prob，干预后 γ_1 = w_Prob/w_CTR，Δγ 反映排序逻辑从流量导向向转化导向的偏移幅度。

## Corrected Claim

搜索排序参数 Δγ_search：定义为排序算法中‘成交概率’权重与‘点击率’权重的比值变化，当前 γ_0 = w_CTR/w_Prob，干预后 γ_1 = w_Prob/w_CTR，Δγ 反映排序逻辑从流量导向向转化导向的偏移幅度。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上正交（分别描述噪声源、权重偏移定义、下游业务影响），无重复或矛盾。但存在不完备性：父节点定义了Δγ_search这一核心参数，子节点2仅重复了父节点的定义公式，未提供新的分解维度；且缺少对'权重调整机制'或'干预触发条件'的独立分解，导致对'变化'的来源解释不足。）

## Search Query

search ranking conversion rate vs click rate weight
