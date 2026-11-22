# N125: 工作点1（高噪声低精度）：$\sigma_{algo} = 0.3$ 对应算法排序完全随机化阶段（如冷启动或A/B测试对照组），此时同一商品曝光排名波动系数 $

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N41

## Claim

工作点1（高噪声低精度）：$\sigma_{algo} = 0.3$ 对应算法排序完全随机化阶段（如冷启动或A/B测试对照组），此时同一商品曝光排名波动系数 $CV_{rank} \approx 0.5$，导致基于曝光数据的权重估计 $\hat{w}_{price}$ 置信区间宽度 $> 50\%$，无法区分 $w_{price}$ 与 $w_{freshness}$ 的相对大小。

## Corrected Claim

工作点1（高噪声低精度）：$\sigma_{algo} = 0.3$ 对应算法排序完全随机化阶段（如冷启动或A/B测试对照组），此时同一商品曝光排名波动系数 $CV_{rank} \approx 0.5$，导致基于曝光数据的权重估计 $\hat{w}_{price}$ 置信区间宽度 $> 50\%$，无法区分 $w_{price}$ 与 $w_{freshness}$ 的相对大小。

## Evidence

先验知识/题面给定，逻辑校验通过：高噪声（σ=0.3）导致排序随机化，进而使基于曝光的统计估计方差增大，置信区间变宽，符合统计学基本原理。
