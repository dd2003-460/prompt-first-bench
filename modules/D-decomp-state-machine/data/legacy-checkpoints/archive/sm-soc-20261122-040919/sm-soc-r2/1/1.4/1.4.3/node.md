# N43: 方差投影：买家期望效用方差 Var[U_buyer] = (1-k)²×σ²_buyer_valuation + k²×σ²_signal_noise，其中 σ

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N8

## Claim

方差投影：买家期望效用方差 Var[U_buyer] = (1-k)²×σ²_buyer_valuation + k²×σ²_signal_noise，其中 σ²_signal_noise 是'快速成交'信号的噪声方差；当 σ²_noise 增大时，Var[U_buyer] 以 k²=0.36 的权重放大，导致效用分布尾部风险增加

## Corrected Claim

方差投影：买家期望效用方差 Var[U_buyer] = (1-k)²×σ²_buyer_valuation + k²×σ²_signal_noise，其中 σ²_signal_noise 是'快速成交'信号的噪声方差；当 σ²_noise 增大时，Var[U_buyer] 以 k²=0.36 的权重放大，导致效用分布尾部风险增加

## Evidence

先验知识/题面给定，逻辑校验通过：方差公式符合线性组合的方差性质（假设估值与噪声独立），k=0.6时k²=0.36计算正确，噪声方差增大导致总方差增加符合数学直觉。
