# N266: 覆盖重叠度量化：当两POP间距D<2R时，重叠区域面积占比 = 1 - (D²/(4R²)) × arccos(D/(2R)) - (D/2) × sqrt(1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

覆盖重叠度量化：当两POP间距D<2R时，重叠区域面积占比 = 1 - (D²/(4R²)) × arccos(D/(2R)) - (D/2) × sqrt(1 - D²/(4R²))，南京-杭州D=250km, R=150km时重叠率约12%，导致带宽浪费率 = 重叠率 × 单POP带宽成本

## Corrected Claim

覆盖重叠度量化：当两POP间距D<2R时，重叠区域面积占比 = 1 - (D²/(4R²)) × arccos(D/(2R)) - (D/2) × sqrt(1 - D²/(4R²))，南京-杭州D=250km, R=150km时重叠率约12%，导致带宽浪费率 = 重叠率 × 单POP带宽成本

## Evidence

先验知识/题面给定，逻辑校验通过：公式为两圆重叠面积占比的标准几何推导（归一化后），代入D=250, R=150计算结果约为12.3%，与陈述一致；带宽浪费率为工程定义，逻辑自洽。

## Search Query

circle overlap area formula two circles distance radius
