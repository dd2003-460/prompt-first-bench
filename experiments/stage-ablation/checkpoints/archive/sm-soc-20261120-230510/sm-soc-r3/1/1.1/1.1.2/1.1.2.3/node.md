# N122: 卖家侧搜索成本偏差投影：C_search_cost 导致的样本选择偏差量化为 Bias_search = (1 - N_observed/N_total) * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N36

## Claim

卖家侧搜索成本偏差投影：C_search_cost 导致的样本选择偏差量化为 Bias_search = (1 - N_observed/N_total) * μ_ε，其中 N_observed 为卖家实际观测到的成交样本数，N_total 为市场总成交量，μ_ε 为未观测样本的平均偏差

## Corrected Claim

卖家侧搜索成本偏差投影：C_search_cost 导致的样本选择偏差量化为 Bias_search = (1 - N_observed/N_total) * μ_ε，其中 N_observed 为卖家实际观测到的成交样本数，N_total 为市场总成交量，μ_ε 为未观测样本的平均偏差

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

sample selection bias seller pricing limited observation online marketplace
