# N164: 去趋势处理后的协方差修正项 Cov_corrected：Cov_corrected(T_close, ΔQ) = Cov_raw(T_close, ΔQ) - 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N48, N49, N50

## Claim

去趋势处理后的协方差修正项 Cov_corrected：Cov_corrected(T_close, ΔQ) = Cov_raw(T_close, ΔQ) - Cov(T_close, ε_market) * Cov(ΔQ, ε_market) / Var(ε_market)；该公式用于消除共同时间序列噪声对相关性检验的偏差，其中 Cov_raw 为原始样本协方差，需从去趋势后的数据中重新计算。

## Corrected Claim

去趋势处理后的协方差修正项 Cov_corrected：Cov_corrected(T_close, ΔQ) = Cov_raw(T_close, ΔQ) - Cov(T_close, ε_market) * Cov(ΔQ, ε_market) / Var(ε_market)；该公式用于消除共同时间序列噪声对相关性检验的偏差，其中 Cov_raw 为原始样本协方差，需从去趋势后的数据中重新计算。

## Evidence

先验知识/题面给定，逻辑校验通过
