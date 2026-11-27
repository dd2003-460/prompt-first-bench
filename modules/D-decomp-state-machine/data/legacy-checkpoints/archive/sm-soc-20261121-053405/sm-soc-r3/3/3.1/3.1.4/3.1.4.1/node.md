# N155: 共享随机源：定义用户行为日志中的观测噪声 $\epsilon_{log}$ 为均值为0、标准差为 $\sigma_{log}$ 的高斯分布，其中 $\sigma

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

共享随机源：定义用户行为日志中的观测噪声 $\epsilon_{log}$ 为均值为0、标准差为 $\sigma_{log}$ 的高斯分布，其中 $\sigma_{log}$ 代表咨询事件记录中的缺失值、重复点击或延迟上报导致的测量误差，该噪声直接影响偏导数 $\partial P_{consult} / \partial \tau$ 的估计精度。

## Corrected Claim

共享随机源：定义用户行为日志中的观测噪声 $\epsilon_{log}$ 为均值为0、标准差为 $\sigma_{log}$ 的高斯分布，其中 $\sigma_{log}$ 代表咨询事件记录中的缺失值、重复点击或延迟上报导致的测量误差，该噪声直接影响偏导数 $\partial P_{consult} / \partial \tau$ 的估计精度。

## Evidence

先验知识/题面给定，逻辑校验通过：高斯噪声模型是处理观测误差的标准统计假设，且噪声确实会影响基于观测数据计算的偏导数估计精度，逻辑自洽。
