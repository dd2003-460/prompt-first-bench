# N7: 演化定向压力投影2：买家搜索成本递减效应导致成交周期 T_deal = T_search_base / (1 + α·N_active_listings)，其中

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

演化定向压力投影2：买家搜索成本递减效应导致成交周期 T_deal = T_search_base / (1 + α·N_active_listings)，其中 α 为网络效应系数（平台数据隐含 α≈0.1-0.3），高挂价未降低 N_active_listings（因卖家不撤单），故 T_deal 缩短与高挂价无负相关，反而因‘高可见性’提升被搜索到的概率。

## Corrected Claim

演化定向压力投影2：买家搜索成本受活跃挂牌数量影响，通常表现为边际递减效应。高挂价若未导致卖家撤单，则维持了 N_active_listings 的规模，避免了因供给减少导致的搜索成本上升；同时，高挂价可能通过‘高可见性’或‘锚定效应’增加被搜索到的概率，从而对成交周期 T_deal 产生复杂影响，而非简单的无负相关或线性缩短。

## Evidence

[质询]公式 T_deal = T_search_base / (1 + α·N_active_listings) 存在严重的量纲和逻辑缺陷：N_active_listings 是绝对数量（无量纲或计数），直接乘以系数 α 并加 1 在数学上缺乏物理意义（除非 N 被归一化，但文中未说明）；此外，‘高挂价未降低 N_active_listings’ 的假设过于简化，忽略了高挂价可能导致买家点击后跳出率增加，从而间接影响有效搜索效率，且‘高可见性’提升被搜索概率与成交周期缩短之间的因果链条缺乏严谨的经济学或算法机制支撑。 | source=knowledge，但公式量纲不自洽（绝对数量直接参与除法运算缺乏归一化说明），且因果逻辑链条存在跳跃，无法从第一性原理严格推出该特定函数形式，故降级。

## Search Query

online marketplace search cost network effect listing duration
