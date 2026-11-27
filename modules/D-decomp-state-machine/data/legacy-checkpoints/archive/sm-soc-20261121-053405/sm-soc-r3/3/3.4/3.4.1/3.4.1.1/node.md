# N159: 短期GMV冲击的随机传播路径：$\epsilon_{mkt}$ 通过乘性项影响成交量 $Q_t$ 和均价 $P_t$，即 $\Delta GMV_t = GMV

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N59

## Claim

短期GMV冲击的随机传播路径：$\epsilon_{mkt}$ 通过乘性项影响成交量 $Q_t$ 和均价 $P_t$，即 $\Delta GMV_t = GMV_{old} \times (\Delta Q_t + \Delta P_t + \epsilon_{mkt,t})$；其中 $\epsilon_{mkt,t}$ 服从 $N(0, \sigma_{mkt}^2)$，且假设各期 $\epsilon_{mkt,t}$ 独立同分布；需计算 $\epsilon_{mkt}$ 对 $\Delta GMV_t$ 方差的贡献率，即 $Var(\epsilon_{mkt}) / Var(\Delta GMV_t)$，以量化宏观噪声在短期GMV波动中的占比。

## Corrected Claim

短期GMV冲击的随机传播路径：$\epsilon_{mkt}$ 通过乘性项影响成交量 $Q_t$ 和均价 $P_t$，即 $\Delta GMV_t = GMV_{old} \times (\Delta Q_t + \Delta P_t + \epsilon_{mkt,t})$；其中 $\epsilon_{mkt,t}$ 服从 $N(0, \sigma_{mkt}^2)$，且假设各期 $\epsilon_{mkt,t}$ 独立同分布；需计算 $\epsilon_{mkt}$ 对 $\Delta GMV_t$ 方差的贡献率，即 $Var(\epsilon_{mkt}) / Var(\Delta GMV_t)$，以量化宏观噪声在短期GMV波动中的占比。

## Evidence

先验知识/题面给定，逻辑校验通过
