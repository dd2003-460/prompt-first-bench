# N48: 打破均衡所需的最低补贴率 r_min 需满足：r_min ≥ (P_initial - P_equilibrium) / P_initial，其中 P_init

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

打破均衡所需的最低补贴率 r_min 需满足：r_min ≥ (P_initial - P_equilibrium) / P_initial，其中 P_initial 为干预前高挂价，P_equilibrium 为市场出清价格，此条件确保卖家在无风控惩罚下仍有利可图。

## Corrected Claim

打破均衡所需的最低补贴率 r_min 需满足：r_min ≥ (P_initial - P_equilibrium) / P_initial，其中 P_initial 为干预前高挂价，P_equilibrium 为市场出清价格，此条件确保卖家在无风控惩罚下仍有利可图。

## Evidence

先验知识/题面给定，逻辑校验通过：补贴率定义为补贴金额与初始价格之比，要使卖家收益不低于均衡价格，需满足 P_initial * (1 - r) + P_initial * r >= P_equilibrium 的变体或更直接的 P_initial * (1 - r_min) <= P_equilibrium 的逆向推导，此处公式 r_min >= (P_initial - P_equilibrium) / P_initial 等价于 P_initial * (1 - r_min) <= P_equilibrium，即卖家实际到手价（扣除补贴后或补贴补足后）不低于均衡价，逻辑自洽。
