# N343: Likelihood(Data | Platform_Driver) 的似然函数具体形式：基于二项分布模型 L(θ) = C(n,k) * θ^k * (1-θ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N120

## Claim

Likelihood(Data | Platform_Driver) 的似然函数具体形式：基于二项分布模型 L(θ) = C(n,k) * θ^k * (1-θ)^(n-k)，其中 θ 为平台流量倾斜效应系数，k 为高挂价商品点击数，n 为总曝光数，需代入 N44 的具体观测数据计算

## Corrected Claim

Likelihood(Data | Platform_Driver) 的似然函数具体形式：基于二项分布模型 L(θ) = C(n,k) * θ^k * (1-θ)^(n-k)，其中 θ 为平台流量倾斜效应系数，k 为高挂价商品点击数，n 为总曝光数，需代入 N44 的具体观测数据计算

## Evidence

先验知识/题面给定，逻辑校验通过：二项分布似然函数形式正确，变量定义（θ, k, n）与场景（点击/曝光）匹配，量纲与逻辑自洽。
