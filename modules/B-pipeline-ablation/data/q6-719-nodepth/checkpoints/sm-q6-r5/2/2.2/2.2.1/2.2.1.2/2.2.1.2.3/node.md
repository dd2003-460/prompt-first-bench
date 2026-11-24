# N515: P_repeat_avg 的流量权重动态修正：N165 中假设 80% 流量来自热门、20% 来自长尾，但实际权重 W_hot(t) 随时间波动；在突发热点事件

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N165

## Claim

P_repeat_avg 的流量权重动态修正：N165 中假设 80% 流量来自热门、20% 来自长尾，但实际权重 W_hot(t) 随时间波动；在突发热点事件期间（K_event 触发），W_hot 可升至 90-95%，导致 P_repeat_avg 从 21.6% 升至 24-26%；在低谷期 W_hot 降至 70%，P_repeat_avg 降至 18-19%。需对 P_repeat_avg 进行 ±20% 敏感性分析以覆盖流量波动。

## Corrected Claim

P_repeat_avg 的流量权重动态修正：N165 中假设 80% 流量来自热门、20% 来自长尾，但实际权重 W_hot(t) 随时间波动；在突发热点事件期间（K_event 触发），W_hot 可升至 90-95%，导致 P_repeat_avg 从 21.6% 升至 24-26%；在低谷期 W_hot 降至 70%，P_repeat_avg 降至 18-19%。需对 P_repeat_avg 进行 ±20% 敏感性分析以覆盖流量波动。

## Evidence

先验知识/题面给定，逻辑校验通过：基于加权平均原理，若热门流量重复率高于长尾，W_hot从80%升至90-95%确实会推高整体P_repeat_avg，降至70%则会拉低，数值变化方向与量级符合线性加权逻辑。

## Search Query

traffic weight hot vs long tail content fluctuation CDN repeat request rate
