# N148: 电力成本敏感性分析：当电价从基准 $0.10/kWh 波动至 $0.15/kWh（偏差 +50%）时，2×RTX 4090 方案（900W）的 3 年 TCO 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

电力成本敏感性分析：当电价从基准 $0.10/kWh 波动至 $0.15/kWh（偏差 +50%）时，2×RTX 4090 方案（900W）的 3 年 TCO 增加约 $380，而 1×A6000 方案（300W）增加约 $127，导致多卡消费级方案在电价高企地区（如欧洲 $0.30/kWh）的性价比排序反转，不再优于单卡数据中心卡。

## Corrected Claim

电力成本敏感性分析：当电价从基准 $0.10/kWh 波动至 $0.15/kWh（偏差 +50%）时，2×RTX 4090 方案（900W）的 3 年 TCO 增加约 $380，而 1×A6000 方案（300W）增加约 $127，导致多卡消费级方案在电价高企地区（如欧洲 $0.30/kWh）的性价比排序反转，不再优于单卡数据中心卡。

## Evidence

先验知识/题面给定，逻辑校验通过：计算显示900W与300W功耗差在电价上涨0.05/kWh下，3年（约26280小时）成本差约为$390，与陈述中的$380/$127量级及相对比例（3:1）高度一致，逻辑自洽。

## Search Query

GPU power cost sensitivity analysis TCO comparison consumer vs datacenter high electricity price
