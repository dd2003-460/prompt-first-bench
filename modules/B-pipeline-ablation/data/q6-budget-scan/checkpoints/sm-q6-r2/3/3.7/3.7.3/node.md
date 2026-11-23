# N120: ΔL_cache 的具体数值：若 H_cache=0.85，T_origin_P99=30ms，则 ΔL_cache = (1-0.85)*30ms = 4.5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32

## Claim

ΔL_cache 的具体数值：若 H_cache=0.85，T_origin_P99=30ms，则 ΔL_cache = (1-0.85)*30ms = 4.5ms；若 H_cache=0.90，T_origin_P99=30ms，则 ΔL_cache = 3.0ms；缓存命中率每提高1%，P99延迟降低约0.3ms [待核验]

## Corrected Claim

ΔL_cache 的具体数值：若 H_cache=0.85，T_origin_P99=30ms，则 ΔL_cache = (1-0.85)*30ms = 4.5ms；若 H_cache=0.90，T_origin_P99=30ms，则 ΔL_cache = 3.0ms；缓存命中率每提高1%，P99延迟降低约0.3ms [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：公式 ΔL = (1-H)*T 符合缓存延迟模型的基本定义，数值计算 (1-0.85)*30=4.5 和 (1-0.90)*30=3.0 准确无误，且 1% 命中率提升对应 0.3ms 延迟降低（30ms * 0.01 = 0.3ms）在逻辑上自洽。
