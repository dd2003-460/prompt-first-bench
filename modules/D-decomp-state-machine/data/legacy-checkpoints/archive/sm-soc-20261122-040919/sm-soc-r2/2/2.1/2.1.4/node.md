# N52: 平台激励约束：平台选择 T 的最优解为 T* = argmax E[r×T] - C(T)，其中 C(T) 是维持长周期的成本函数（如用户流失率 λ_churn

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N10

## Claim

平台激励约束：平台选择 T 的最优解为 T* = argmax E[r×T] - C(T)，其中 C(T) 是维持长周期的成本函数（如用户流失率 λ_churn(T)×LTV）；若 λ_churn(T) = 0.02×T/7，LTV=100，则 C(T)=0.286T；最优 T* = (E[r] - λ_churn×LTV)/0，需通过一阶条件求解 [待核验]：需实际用户流失数据

## Corrected Claim

平台选择 T 的最优解为 T* = argmax E[r×T] - C(T)。若 λ_churn(T) = 0.02×T/7，LTV=100，则 C(T) = 100 × (0.02×T/7) = (1/35)T² ≈ 0.0286T²。最优 T* 需通过一阶条件 E[r] - C'(T) = 0 求解，即 E[r] - (2/35)T = 0，得 T* = 17.5 × E[r]。

## Evidence

[质询]陈述中存在严重的数学逻辑错误：1. 成本函数推导错误，若 λ_churn(T)=0.02×T/7 且 LTV=100，则 C(T) 应为 0.2857T²（二次函数），而非 0.286T（线性函数）；2. 最优解公式错误，T* = (E[r] - λ_churn×LTV)/0 在数学上无意义（分母为零），且一阶条件求解不应出现除以零的操作。 | 逻辑校验失败：C(T) 的量纲和函数形式推导错误（线性 vs 二次），且最优解表达式存在除零错误，违背基本数学直觉。参考来源 [1][2][3] 均讨论平台定价或博弈论，未涉及此具体错误公式，无法支持该错误陈述。

## Search Query

platform incentive optimal transaction cycle cost function user churn

## Retrieval Sources

- {'url': 'https://www.sciencedirect.com/science/article/pii/S0377221724007422&rut=17ada71da183dae0001657891dafd850bf6871d56a2b10e7980e190ab9ad3f61', 'type': 'ddg', 'title': 'Optimal platform pricing with multi-sided users: A direct and indirect ...'}
- {'url': 'https://www.sciencedirect.com/science/article/pii/S0960077925013025&rut=3c7e05588c151d399f5cd2e780a45114e63e26df1eb0bfa0a202040e82c20b10', 'type': 'ddg', 'title': 'Optimal pricing and complex analysis for green e-commerce platform ...'}
- {'url': 'https://jaypilchoi.com/wp-content/uploads/2026/06/Regulating-Platform-Bias_Merged.pdf&rut=1831c4e7291eeb878a8e49b5ba763ced1b45b1b6835d022ce2a5f47ae87a88e0', 'type': 'ddg', 'title': 'PDF -preferencing and Transaction Fees'}
