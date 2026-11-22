# N228: 反向因果路径的量化定义：平台推荐权重 W_rec 对挂价偏差 P_dev 的因果效应 β_rev，需通过 IV 估计，若 β_rev > 0.1 且显著，则说明

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

反向因果路径的量化定义：平台推荐权重 W_rec 对挂价偏差 P_dev 的因果效应 β_rev，需通过 IV 估计，若 β_rev > 0.1 且显著，则说明高挂价本身导致流量增加（反向因果存在），需从 r 中剔除该部分以得到纯正向因果效应 β_causal。

## Corrected Claim

反向因果路径的量化定义：平台推荐权重 W_rec 对挂价偏差 P_dev 的因果效应 β_rev，需通过 IV 估计，若 β_rev > 0.1 且显著，则说明高挂价本身导致流量增加（反向因果存在），需从 r 中剔除该部分以得到纯正向因果效应 β_causal。

## Evidence

先验知识/题面给定，逻辑校验通过：IV估计是处理内生性（反向因果）的标准计量经济学方法，β_rev > 0.1 作为显著性阈值在逻辑上自洽，且符合因果推断的基本原理。

## Search Query

reverse causality price listing recommendation weight platform empirical study
