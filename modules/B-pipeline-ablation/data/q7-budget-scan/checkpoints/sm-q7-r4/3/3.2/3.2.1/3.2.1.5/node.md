# N257: HDD+SSD分层方案修正后总功耗 P_total = P_HDD + P_SSD + P_Controller + P_Fans = 240W + 411.6

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

HDD+SSD分层方案修正后总功耗 P_total = P_HDD + P_SSD + P_Controller + P_Fans = 240W + 411.6W + 60W + 150W = 861.6W；对比原N88估算的1570W，主要差异在于原估算可能高估了SSD活跃功耗占比或包含了未分摊的整机功耗，修正后年电费成本将显著降低。

## Corrected Claim

HDD+SSD分层方案修正后总功耗 P_total = P_HDD + P_SSD + P_Controller + P_Fans = 240W + 411.6W + 60W + 150W = 861.6W；对比原N88估算的1570W，主要差异在于原估算可能高估了SSD活跃功耗占比或包含了未分摊的整机功耗，修正后年电费成本将显著降低。

## Evidence

父节点级核验未通过：非正交, 不完备（存在严重的事实矛盾与数据不一致：1. 子节点1计算的总功耗为946.6W（其中控制器功耗突变为145W，与父节点的60W矛盾），而父节点明确陈述总功耗为861.6W且控制器为60W，两者直接冲突。2. 子节点2基于错误的946.6W进行计算，导致结论偏离父节点描述的“修正后”状态。3. 父节点提到的“原N88估算1570W”在子节点中仅作为对比背景，未形成独立的逻辑分支，但核心矛盾在于数值不自洽。）
