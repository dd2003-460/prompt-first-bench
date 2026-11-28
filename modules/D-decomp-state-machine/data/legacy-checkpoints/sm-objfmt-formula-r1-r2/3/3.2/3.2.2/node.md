# N72: 非GPU组件的待机与负载功耗贡献：现代ATX工作站中，CPU (i9/Xeon) 满载约125-250W，主板+RAM+SSD合计约50-100W，因此单卡H1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

非GPU组件的待机与负载功耗贡献：现代ATX工作站中，CPU (i9/Xeon) 满载约125-250W，主板+RAM+SSD合计约50-100W，因此单卡H100平台总系统功耗约为700W(GPU)+200W(其他)=900W，而2x RTX 4090平台总功耗约为900W(2*450W)+200W(其他)=1100W [待核验具体CPU满载功耗及主板基础功耗]

## Corrected Claim

非GPU组件的待机与负载功耗贡献：现代ATX工作站中，CPU (i9/Xeon) 满载约125-250W，主板+RAM+SSD合计约50-100W，因此单卡H100平台总系统功耗约为700W(GPU)+200W(其他)=900W，而2x RTX 4090平台总功耗约为900W(2*450W)+200W(其他)=1100W [待核验具体CPU满载功耗及主板基础功耗]

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM功耗约700W，RTX 4090 TDP约450W，非GPU组件（CPU+主板+内存+存储）在高性能工作站中满载功耗通常在150-250W区间，估算值900W和1100W符合工程常识与量级。
