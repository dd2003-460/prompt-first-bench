# N321: 同源性的时间序列对齐要求：P(ShortCycle | HighPrice) 与 P(NoInquiry | PriceDrop) 的波动序列必须基于相同时间窗

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102, N103, N104

## Claim

同源性的时间序列对齐要求：P(ShortCycle | HighPrice) 与 P(NoInquiry | PriceDrop) 的波动序列必须基于相同时间窗口（如 7 天滚动平均）和相同商品类别（如手机/服装）进行计算；若时间窗口不一致（如一个用日频，一个用周频），相关系数 ρ 的计算将因频率错配产生伪相关，需先通过重采样（Resampling）统一时间粒度，再计算 Pearson 相关系数。

## Corrected Claim

同源性的时间序列对齐要求：P(ShortCycle | HighPrice) 与 P(NoInquiry | PriceDrop) 的波动序列必须基于相同时间窗口（如 7 天滚动平均）和相同商品类别（如手机/服装）进行计算；若时间窗口不一致（如一个用日频，一个用周频），相关系数 ρ 的计算将因频率错配产生伪相关，需先通过重采样（Resampling）统一时间粒度，再计算 Pearson 相关系数。

## Evidence

先验知识/题面给定，逻辑校验通过：时间序列对齐是计算相关系数的基本前提，频率错配确实会导致伪相关，重采样是标准处理方法。

## Search Query

time series alignment resampling correlation analysis
