# N96: 期望收益函数中等待成本 C_wait 的量化：C_wait = r_time * T_close + r_capital * P_ask * T_close /

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

期望收益函数中等待成本 C_wait 的量化：C_wait = r_time * T_close + r_capital * P_ask * T_close / 365，其中 r_time 为卖家时间机会成本（如 50-100 元/小时），r_capital 为资金成本（年化 5-10%）；对于 1000 元商品，若 T_close = 7 天，C_wait ≈ 50-100 元（时间）+ 1-2 元（资金），时间成本主导。

## Corrected Claim

期望收益函数中等待成本 C_wait 的量化：C_wait = r_time * T_close + r_capital * P_ask * T_close / 365，其中 r_time 为卖家时间机会成本（如 50-100 元/小时），r_capital 为资金成本（年化 5-10%）；对于 1000 元商品，若 T_close = 7 天，C_wait ≈ 50-100 元（时间）+ 1-2 元（资金），时间成本主导。

## Evidence

父节点级核验未通过：不完备（子节点1关注卖家个体异质性（r_time），子节点2关注商品属性导致的成本结构变化（r_capital项替换），两者维度不同，正交性良好。但父节点公式包含 r_time 和 r_capital 两个主要变量，子节点仅深入了 r_time 的异质性和 r_capital 的特定场景修正，未覆盖 r_capital 在标准场景下的通用量化逻辑或 r_time 与 r_capital 在一般情况下的具体数值推导过程，导致对父节点公式中各变量的整体量化覆盖不全。）
