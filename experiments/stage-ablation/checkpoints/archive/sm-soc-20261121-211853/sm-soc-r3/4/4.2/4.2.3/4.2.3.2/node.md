# N94: 信号方差参数 $\sigma_p^2$ 的估计方法：基于历史成交数据，计算高溢价组（D>15%）成交价与挂价之差的方差，即 $\sigma_p^2 \appro

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N42

## Claim

信号方差参数 $\sigma_p^2$ 的估计方法：基于历史成交数据，计算高溢价组（D>15%）成交价与挂价之差的方差，即 $\sigma_p^2 \approx \text{Var}(P_{deal} - P_{ask}) | D > 15\%$，该值越大表示卖家挂价信号越不可信，买家对挂价的权重越低。

## Corrected Claim

信号方差参数 $\sigma_p^2$ 的估计方法：基于历史成交数据，计算高溢价组（D>15%）成交价与挂价之差的方差，即 $\sigma_p^2 \approx \text{Var}(P_{deal} - P_{ask}) | D > 15\%$，该值越大表示卖家挂价信号越不可信，买家对挂价的权重越低。

## Evidence

先验知识/题面给定，逻辑校验通过：基于历史数据计算特定条件下价差方差以估计信号噪声水平，符合统计估计与信号处理的基本逻辑，且量纲与业务直觉一致。

## Search Query

variance of asking price vs deal price premium items
