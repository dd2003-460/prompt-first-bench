# N335: 缓存预热时间 T_warmup 的影响：POP故障后恢复时，缓存命中率 H(t) 从0%逐步恢复至85%，平均预热时间 T_warmup≈2-4小时（取决于对象

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

缓存预热时间 T_warmup 的影响：POP故障后恢复时，缓存命中率 H(t) 从0%逐步恢复至85%，平均预热时间 T_warmup≈2-4小时（取决于对象访问频率）；在 T_warmup 期间，回源率高于稳态值，需额外计算预热期间的回源带宽成本和延迟惩罚。

## Corrected Claim

缓存预热时间 T_warmup 的影响：POP故障后恢复时，缓存命中率 H(t) 从0%逐步恢复至85%，平均预热时间 T_warmup≈2-4小时（取决于对象访问频率）；在 T_warmup 期间，回源率高于稳态值，需额外计算预热期间的回源带宽成本和延迟惩罚。

## Evidence

先验知识/题面给定，逻辑校验通过
