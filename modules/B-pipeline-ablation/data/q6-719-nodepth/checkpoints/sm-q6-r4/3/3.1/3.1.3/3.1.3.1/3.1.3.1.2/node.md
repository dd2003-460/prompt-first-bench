# N639: 工作点A（高缓存命中率）的缓存命中率提升对P99延迟的影响：L_p99_A = L_edge + L_backhaul * (1 - H_A) + L_proc

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N213

## Claim

工作点A（高缓存命中率）的缓存命中率提升对P99延迟的影响：L_p99_A = L_edge + L_backhaul * (1 - H_A) + L_processing，假设L_edge=5ms, L_backhaul=100ms, L_processing=2ms, H_A=0.92，则 L_p99_A = 5 + 100 * 0.08 + 2 = 15ms；对比基准H_base=0.85，L_p99_base = 5 + 100 * 0.15 + 2 = 22ms，降低7ms。

## Corrected Claim

工作点A（高缓存命中率）的缓存命中率提升对P99延迟的影响：L_p99_A = L_edge + L_backhaul * (1 - H_A) + L_processing，假设L_edge=5ms, L_backhaul=100ms, L_processing=2ms, H_A=0.92，则 L_p99_A = 5 + 100 * 0.08 + 2 = 15ms；对比基准H_base=0.85，L_p99_base = 5 + 100 * 0.15 + 2 = 22ms，降低7ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cdn cache hit rate impact on p99 latency backhaul reduction
