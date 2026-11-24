# N698: SSD功耗对总TCO的占比分析：修正后SSD年电费为 ¥274.71（基准）或 ¥384.59（含PUE），占HDD+SSD方案总TCO的 0.03%-0.05

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N258, N259, N260

## Claim

SSD功耗对总TCO的占比分析：修正后SSD年电费为 ¥274.71（基准）或 ¥384.59（含PUE），占HDD+SSD方案总TCO的 0.03%-0.05%，远低于HDD层功耗占比（0.3%）；因此SSD层功耗优化（如降低空闲功耗至4W）对总成本影响可忽略，无需作为独立优化维度。

## Corrected Claim

SSD功耗对总TCO的占比分析：修正后SSD年电费为 ¥274.71（基准）或 ¥384.59（含PUE），占HDD+SSD方案总TCO的 0.03%-0.05%，远低于HDD层功耗占比（0.3%）；因此SSD层功耗优化（如降低空闲功耗至4W）对总成本影响可忽略，无需作为独立优化维度。

## Evidence

先验知识/题面给定，逻辑校验通过：SSD功耗（~5-10W）远低于HDD（~7-10W/盘且数量多），且电费在TCO中占比极小，0.03%-0.05%的量级符合工程常识，结论逻辑自洽。
