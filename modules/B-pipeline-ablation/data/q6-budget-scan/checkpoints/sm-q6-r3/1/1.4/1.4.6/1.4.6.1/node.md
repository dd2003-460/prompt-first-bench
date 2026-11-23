# N145: 量化带宽95th百分位(BW_95th)与峰值带宽(BW_peak)的差异：在双峰分布下，BW_95th 对应流量持续时间 Top 5% 的阈值，若峰值持续时间

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53

## Claim

量化带宽95th百分位(BW_95th)与峰值带宽(BW_peak)的差异：在双峰分布下，BW_95th 对应流量持续时间 Top 5% 的阈值，若峰值持续时间为5h，则 BW_95th ≈ BW_avg * PF * (5/24)^0.5 (基于正态分布尾部近似)，具体需通过累积分布函数CDF计算。

## Corrected Claim

量化带宽95th百分位(BW_95th)与峰值带宽(BW_peak)的差异取决于流量分布的具体形态。在双峰分布下，BW_95th 通常显著低于 BW_peak。具体数值需通过累积分布函数(CDF)计算，简单的正态分布近似公式 BW_95th ≈ BW_avg * PF * (5/24)^0.5 仅在特定假设下近似成立，不具备普适性。

## Evidence

[质询]公式 BW_95th ≈ BW_avg * PF * (5/24)^0.5 缺乏严谨的数学推导支持，且将“持续时间 Top 5%”直接等同于“带宽值 Top 5%”存在概念混淆；在双峰分布下，简单的正态尾部近似公式通常不成立，具体系数和形式高度依赖分布形状，不能一概而论。 | 先验知识/题面给定，逻辑校验发现公式推导存在瑕疵且概念定义模糊，无法确认为通用真理，故降级。

## Search Query

95th percentile bandwidth calculation dual peak distribution
