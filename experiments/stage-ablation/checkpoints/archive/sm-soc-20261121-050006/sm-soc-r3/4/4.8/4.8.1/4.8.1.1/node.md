# N290: C_CPM 的动态定价机制：C_CPM 并非固定值，而是随竞价强度 B_bidding 变化，C_CPM = C_CPM_base * (1 + γ_biddi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N92

## Claim

C_CPM 的动态定价机制：C_CPM 并非固定值，而是随竞价强度 B_bidding 变化，C_CPM = C_CPM_base * (1 + γ_bidding * B_bidding)，其中 γ_bidding ∈ [0.1, 0.3] 为竞价敏感度系数，B_bidding 为当日竞价指数（基于历史 CPM 波动率标准化）；需通过时间序列模型估计 γ_bidding。

## Corrected Claim

C_CPM 的动态定价机制：C_CPM 并非固定值，而是随竞价强度 B_bidding 变化，C_CPM = C_CPM_base * (1 + γ_bidding * B_bidding)，其中 γ_bidding ∈ [0.1, 0.3] 为竞价敏感度系数，B_bidding 为当日竞价指数（基于历史 CPM 波动率标准化）；需通过时间序列模型估计 γ_bidding。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合线性定价模型直觉，参数范围[0.1, 0.3]在广告竞价领域属于合理量级，无内部矛盾。

## Search Query

dynamic CPM pricing model in online advertising
