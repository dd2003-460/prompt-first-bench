# N21: 在负相关系数 ρ=-0.3 的约束下，对象大小 S 与请求频率 F 的联合概率密度函数 f(S,F) 可通过 copula 函数建模：f(S,F) = f_S(

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

在负相关系数 ρ=-0.3 的约束下，对象大小 S 与请求频率 F 的联合概率密度函数 f(S,F) 可通过 copula 函数建模：f(S,F) = f_S(S) * f_F(F) * C(u_S, u_F; ρ)，其中 u_S, u_F 为边缘分布的累积分布函数值。具体地，若采用高斯 Copula，相关系数直接取 ρ=-0.3，这将导致热门对象（高 F）倾向于较小尺寸，从而在固定缓存容量下提升字节命中率。

## Corrected Claim

在负相关系数 ρ=-0.3 的约束下，对象大小 S 与请求频率 F 的联合概率密度函数 f(S,F) 可通过 copula 函数建模：f(S,F) = f_S(S) * f_F(F) * C(u_S, u_F; ρ)，其中 u_S, u_F 为边缘分布的累积分布函数值。具体地，若采用高斯 Copula，相关系数直接取 ρ=-0.3，这将导致热门对象（高 F）倾向于较小尺寸，从而在固定缓存容量下提升字节命中率。

## Evidence

公式/推导类，逻辑校验通过，来源未直接覆盖

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'http://arxiv.org/abs/2609.20512v4', 'type': 'arxiv', 'title': 'Copula Operad and Copula Entropy'}
