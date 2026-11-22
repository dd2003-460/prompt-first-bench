# N248: 基础交易量 N_transactions 的时间序列波动性 σ_N，定义为历史日均交易量的标准差，用于量化 ε_N 估计的不确定性，若 σ_N > 0.2 * 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

基础交易量 N_transactions 的时间序列波动性 σ_N，定义为历史日均交易量的标准差，用于量化 ε_N 估计的不确定性，若 σ_N > 0.2 * N_mean，则弹性估计置信区间显著扩大，影响平台收益弹性的稳定性判断。

## Corrected Claim

基础交易量 N_transactions 的时间序列波动性 σ_N 定义为历史日均交易量的标准差，用于量化 ε_N 估计的不确定性；当 σ_N 相对于 N_mean 较大时（如超过特定阈值），弹性估计置信区间会扩大，影响平台收益弹性的稳定性判断。

## Evidence

[质询]阈值 0.2 为经验性设定，缺乏通用理论依据或行业标准支持，属于特定模型假设而非普适事实。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

transaction volume volatility second-hand marketplace daily sales standard deviation
