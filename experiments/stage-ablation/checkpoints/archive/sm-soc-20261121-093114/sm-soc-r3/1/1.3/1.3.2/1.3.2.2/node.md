# N109: 信号解读的二值化波动率：P(signal|P_ask) 的方差 Var(P) = Φ'((P_ask - P_market - 15% + ε_buyer) /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N34

## Claim

信号解读的二值化波动率：P(signal|P_ask) 的方差 Var(P) = Φ'((P_ask - P_market - 15% + ε_buyer) / σ_threshold)^2 * (σ_perception / σ_threshold)^2，其中 Φ' 为标准正态PDF，量化了随机噪声对信号解读概率的边际影响。

## Corrected Claim

信号解读的二值化波动率：P(signal|P_ask) 的方差 Var(P) = Φ'((P_ask - P_market - 15% + ε_buyer) / σ_threshold)^2 * (σ_perception / σ_threshold)^2，其中 Φ' 为标准正态PDF，量化了随机噪声对信号解读概率的边际影响。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合概率密度函数（PDF）在阈值模型下对参数扰动的敏感度（方差）推导逻辑，量纲与数学结构自洽。

## Search Query

binary signal interpretation variance normal CDF derivative
