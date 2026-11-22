# N138: 均值参数 μ_R 的校准公式：μ_R = P_market * (1 + c_search/c_transaction)，其中 c_search 为平均搜索成本

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N47

## Claim

均值参数 μ_R 的校准公式：μ_R = P_market * (1 + c_search/c_transaction)，其中 c_search 为平均搜索成本（货币化），c_transaction 为平均交易成本（含佣金、时间）；若 c_search/c_transaction = 0.05，则 μ_R = 1.05 * P_market，该比值可通过平台用户行为数据（搜索时长/成交金额）估算。

## Corrected Claim

均值参数 μ_R 的校准公式：μ_R = P_market * (1 + c_search/c_transaction)，其中 c_search 为平均搜索成本（货币化），c_transaction 为平均交易成本（含佣金、时间）；若 c_search/c_transaction = 0.05，则 μ_R = 1.05 * P_market，该比值可通过平台用户行为数据（搜索时长/成交金额）估算。

## Evidence

先验知识/题面给定，逻辑校验通过
