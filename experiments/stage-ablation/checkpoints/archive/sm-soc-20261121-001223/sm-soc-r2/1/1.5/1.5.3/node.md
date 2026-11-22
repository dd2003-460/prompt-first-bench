# N44: 成交周期T_deal的计算：T_deal = 1 / (k_consult * k_deal)，其中k_deal为咨询到成交的转化率（基准值0.3-0.5），用

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

成交周期T_deal的计算：T_deal = 1 / (k_consult * k_deal)，其中k_deal为咨询到成交的转化率（基准值0.3-0.5），用于量化高挂价通过提升k_consult缩短成交周期的机制。

## Corrected Claim

成交周期T_deal的计算：T_deal = 1 / (k_consult * k_deal)，其中k_deal为咨询到成交的转化率（基准值0.3-0.5），用于量化高挂价通过提升k_consult缩短成交周期的机制。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 T_deal = 1/(k_consult * k_deal) 符合概率论中独立事件串联成功率的倒数定义（期望等待时间），且 k_deal 取值 0.3-0.5 符合常规商业转化率量级，逻辑自洽。
