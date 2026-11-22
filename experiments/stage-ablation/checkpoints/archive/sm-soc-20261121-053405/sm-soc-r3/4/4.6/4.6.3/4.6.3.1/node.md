# N202: 共享随机源：定义 P_consult 的测量噪声 \(\epsilon_{meas}\) 为均值为0、标准差为 \(\sigma_{meas}\) 的高斯分布，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N77

## Claim

共享随机源：定义 P_consult 的测量噪声 \(\epsilon_{meas}\) 为均值为0、标准差为 \(\sigma_{meas}\) 的高斯分布，其中 \(\sigma_{meas}\) 代表平台日志中咨询事件记录的时间戳误差和去重逻辑误差，通常假设 \(\sigma_{meas} < 0.01\)，该噪声叠加在正态分布假设的 \(\sigma_P = 0.02\) 之上。

## Corrected Claim

共享随机源：定义 P_consult 的测量噪声 \(\epsilon_{meas}\) 为均值为0、标准差为 \(\sigma_{meas}\) 的高斯分布，其中 \(\sigma_{meas}\) 代表平台日志中咨询事件记录的时间戳误差和去重逻辑误差，通常假设 \(\sigma_{meas} < 0.01\)，该噪声叠加在正态分布假设的 \(\sigma_P = 0.02\) 之上。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

data logging noise timestamp error deduplication standard deviation
