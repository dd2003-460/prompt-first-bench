# N338: 信号强度敏感度 k_signal 的估计方法：通过二元Logistic回归模型 P(Q_high|δ) = 1/(1+e^(-k_signal(δ-δ_th))

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

信号强度敏感度 k_signal 的估计方法：通过二元Logistic回归模型 P(Q_high|δ) = 1/(1+e^(-k_signal(δ-δ_th))) 拟合历史成交数据，k_signal 代表溢价每增加1%对高质概率对数几率(log-odds)的边际贡献，需计算其95%置信区间以验证信号效应的统计显著性。

## Corrected Claim

信号强度敏感度 k_signal 的估计方法：通过二元Logistic回归模型 P(Q_high|δ) = 1/(1+e^(-k_signal(δ-δ_th))) 拟合历史成交数据，k_signal 代表溢价每增加1%对高质概率对数几率(log-odds)的边际贡献，需计算其95%置信区间以验证信号效应的统计显著性。

## Evidence

先验知识/题面给定，逻辑校验通过：二元Logistic回归模型中系数确实代表对数几率的边际贡献，且通过置信区间验证显著性是标准统计实践，逻辑自洽。

## Search Query

binary logistic regression slope coefficient interpretation signal strength
