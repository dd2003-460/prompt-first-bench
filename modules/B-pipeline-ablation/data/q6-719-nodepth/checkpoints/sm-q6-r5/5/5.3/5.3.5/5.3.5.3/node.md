# N304: 自建回源延迟 L_backhaul_self = L_line + L_processing_origin，其中 L_line 为骨干网专线延迟（同城 <10m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99, N100, N101

## Claim

自建回源延迟 L_backhaul_self = L_line + L_processing_origin，其中 L_line 为骨干网专线延迟（同城 <10ms，跨城 20-50ms，跨省 30-80ms），L_processing_origin 为源站处理延迟（5-20ms）；需根据 10 个 POP 的地理分布加权计算平均 L_backhaul_self，并识别 P99 对应的最坏路径延迟。

## Corrected Claim

自建回源延迟 L_backhaul_self = L_line + L_processing_origin，其中 L_line 为骨干网专线延迟（同城 <10ms，跨城 20-50ms，跨省 30-80ms），L_processing_origin 为源站处理延迟（5-20ms）；需根据 10 个 POP 的地理分布加权计算平均 L_backhaul_self，并识别 P99 对应的最坏路径延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：骨干网专线延迟量级（同城<10ms，跨城/省20-80ms）及源站处理延迟（5-20ms）符合网络工程常识，加权平均与P99最坏路径的分析方法逻辑自洽。
