# N43: 搜索成本量化：买家完成一次有效比较（从发现商品到决定购买）的平均耗时 (T_search_avg) 及平均比较商品数量 (N_compare)。S_buyer 

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

搜索成本量化：买家完成一次有效比较（从发现商品到决定购买）的平均耗时 (T_search_avg) 及平均比较商品数量 (N_compare)。S_buyer 的分子部分即为 (ΔT_search * V_time) / (N_compare * P_avg)，其中 P_avg 为商品均价。

## Corrected Claim

搜索成本量化通常涉及买家完成有效比较的平均耗时 (T_search_avg) 及平均比较商品数量 (N_compare)。在特定模型中，S_buyer 的分子部分可表示为 (ΔT_search * V_time) / (N_compare * P_avg)，其中 P_avg 为商品均价，但具体数值需依据实际市场数据确定。

## Evidence

父节点级核验失败（LLM 错误）：Invalid control character at: line 7 column 103 (char 357)

## Search Query

online consumer search cost time spent comparing products second hand market
