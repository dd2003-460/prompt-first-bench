# N113: 混合策略双系统协调切换延迟：需同时操作自建DNS/BGP和公有云CDN控制台API，切换时间 = $\max(T_{self\_switch}, T_{clou

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

混合策略双系统协调切换延迟：需同时操作自建DNS/BGP和公有云CDN控制台API，切换时间 = $\max(T_{self\_switch}, T_{cloud\_switch}) + T_{coordination}$，其中 $T_{coordination}$ 为人工协调或自动化脚本执行时间，需量化两套系统并行切换的同步误差

## Corrected Claim

混合策略双系统协调切换延迟：需同时操作自建DNS/BGP和公有云CDN控制台API，切换时间 = $\max(T_{self\_switch}, T_{cloud\_switch}) + T_{coordination}$，其中 $T_{coordination}$ 为人工协调或自动化脚本执行时间，需量化两套系统并行切换的同步误差

## Evidence

先验知识/题面给定，逻辑校验通过：并行操作系统的总耗时确实由最长路径决定，加上协调开销符合基本逻辑，且作为架构设计中的定性/半定量描述，量级和逻辑自洽。
