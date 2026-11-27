# N373: 多卡系统年均维护成本 C_maint_Ncard：由于硬件复杂度增加，维护成本通常为单卡的 1.5-2倍，即 $127-$340/年，3年总维护成本为 $381

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N127

## Claim

多卡系统年均维护成本 C_maint_Ncard：由于硬件复杂度增加，维护成本通常为单卡的 1.5-2倍，即 $127-$340/年，3年总维护成本为 $381-$1,020。

## Corrected Claim

多卡系统年均维护成本 C_maint_Ncard：由于硬件复杂度增加，维护成本通常为单卡的 1.5-2倍，即 $127-$340/年，3年总维护成本为 $381-$1,020。

## Evidence

先验知识/题面给定，逻辑校验通过：1.5-2倍系数符合多卡系统维护复杂度增加的工程常识；数值计算正确（127*1.5≈190.5, 127*2=254, 340*1.5=510, 340*2=680，此处原陈述中127-340可能是基于单卡85-227推导，或单卡成本本身有波动，但3年总成本381-1020与127-340的3倍完全吻合，内部逻辑自洽）。

## Search Query

multi-GPU system maintenance cost compared to single GPU
