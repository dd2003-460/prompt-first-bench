# N94: 性能基准时效性判定：对于吞吐量/延迟数据，若来源为[Memory]且未注明具体框架版本（如vLLM 0.4.0 vs 0.6.0），必须标记为[Version_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26, N27, N28

## Claim

性能基准时效性判定：对于吞吐量/延迟数据，若来源为[Memory]且未注明具体框架版本（如vLLM 0.4.0 vs 0.6.0），必须标记为[Version_Risk]；若版本差异导致性能偏差>5%，需触发实时搜索验证。

## Corrected Claim

性能基准时效性判定：对于吞吐量/延迟数据，若来源为[Memory]且未注明具体框架版本（如vLLM 0.4.0 vs 0.6.0），必须标记为[Version_Risk]；若版本差异导致性能偏差>5%，需触发实时搜索验证。

## Evidence

先验知识/题面给定，逻辑校验通过
