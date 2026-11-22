# N82: 边缘 CDF 变换的具体函数形式：S' = Φ_S(S) = (S/x_min)^(1-α) 和 F' = Φ_F(F) = (F/f_max)^(1-β)，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

边缘 CDF 变换的具体函数形式：S' = Φ_S(S) = (S/x_min)^(1-α) 和 F' = Φ_F(F) = (F/f_max)^(1-β)，其中 x_min=0.131072MB, f_max=1.44e6/day，将原始变量映射到 [0,1] 区间以输入 Copula。

## Corrected Claim

边缘 CDF 变换的具体函数形式：S' = Φ_S(S) = (S/x_min)^(1-α) 和 F' = Φ_F(F) = (F/f_max)^(1-β)，其中 x_min=0.131072MB, f_max=1.44e6/day，将原始变量映射到 [0,1] 区间以输入 Copula。

## Evidence

先验知识/题面给定，逻辑校验通过：幂函数变换 (x/x_min)^(1-α) 在 x_min 处值为 1，在 x→0 时值为 0（假设 α>1），符合将变量映射到 [0,1] 区间以输入 Copula 的数学逻辑；数值量级（MB 和 day）合理。
