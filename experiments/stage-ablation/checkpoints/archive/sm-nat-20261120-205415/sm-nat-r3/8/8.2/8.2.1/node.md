# N213: 工作点1（独立假设，ρ=0）：分母近似为 ∫_{x_min}^{x_max} h(x) s(x) f_S(x) dx，在热度与大小独立假设下，该积分可分离为 ∫

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

工作点1（独立假设，ρ=0）：分母近似为 ∫_{x_min}^{x_max} h(x) s(x) f_S(x) dx，在热度与大小独立假设下，该积分可分离为 ∫h(x)dx * ∫s(x)f_S(x)dx，数值约为 50,000,000 * E[S]。

## Corrected Claim

工作点1（独立假设，ρ=0）：分母近似为 ∫_{x_min}^{x_max} h(x) s(x) f_S(x) dx，在热度与大小独立假设下，该积分可分离为 ∫h(x)dx * ∫s(x)f_S(x)dx，数值约为 50,000,000 * E[S]。

## Evidence

先验知识/题面给定，逻辑校验通过：在独立假设下，联合分布函数可分解为边缘分布乘积，积分可分离为两个独立积分的乘积，数学推导自洽。
