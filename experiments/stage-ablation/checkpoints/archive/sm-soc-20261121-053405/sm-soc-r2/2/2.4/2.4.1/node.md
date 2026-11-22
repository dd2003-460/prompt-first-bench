# N44: 共享随机源：定义数据观测误差 $\epsilon_{data}$ 为均值为0、标准差为 $\sigma_{data}$ 的高斯分布，其中 $\sigma_{da

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

共享随机源：定义数据观测误差 $\epsilon_{data}$ 为均值为0、标准差为 $\sigma_{data}$ 的高斯分布，其中 $\sigma_{data}$ 代表平台日志数据中关于成交周期、咨询量等关键变量的测量噪声，该噪声直接影响贝叶斯后验概率的精度。

## Corrected Claim

共享随机源：定义数据观测误差 $\epsilon_{data}$ 为均值为0、标准差为 $\sigma_{data}$ 的高斯分布，其中 $\sigma_{data}$ 代表平台日志数据中关于成交周期、咨询量等关键变量的测量噪声，该噪声直接影响贝叶斯后验概率的精度。

## Evidence

先验知识/题面给定，逻辑校验通过：高斯噪声模型是处理测量误差的标准假设，且噪声确实通过影响似然函数进而影响贝叶斯后验精度，逻辑自洽。
