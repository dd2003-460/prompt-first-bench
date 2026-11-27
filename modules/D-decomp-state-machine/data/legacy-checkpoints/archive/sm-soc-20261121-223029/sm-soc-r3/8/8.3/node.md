# N117: 沉默螺旋的时间窗口约束：48小时无咨询的统计显著性检验，H0: P(no_inquiry | 48h) <= 0.4；若实际观测值为 0.6，则需计算在给定买家

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

沉默螺旋的时间窗口约束：48小时无咨询的统计显著性检验，H0: P(no_inquiry | 48h) <= 0.4；若实际观测值为 0.6，则需计算在给定买家搜索频率 f_search 下，48小时内的期望咨询次数 E[Inquiries] = f_search * C_inquiry * 48，若 E[Inquiries] < 1 则‘无咨询’为高概率事件。

## Corrected Claim

沉默螺旋的时间窗口约束：48小时无咨询的统计显著性检验，H0: P(no_inquiry | 48h) <= 0.4；若实际观测值为 0.6，则需计算在给定买家搜索频率 f_search 下，48小时内的期望咨询次数 E[Inquiries] = f_search * C_inquiry * 48，若 E[Inquiries] < 1 则‘无咨询’为高概率事件。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松分布期望值公式 E[λ] = rate * time 符合基本概率论原理，且 E<1 时 P(0) 确实较高，逻辑自洽。

## Search Query

expected inquiry count in 48 hour window poisson distribution
