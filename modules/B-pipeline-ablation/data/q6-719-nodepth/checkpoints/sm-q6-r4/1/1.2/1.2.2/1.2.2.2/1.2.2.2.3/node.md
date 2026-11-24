# N469: P99 延迟修正项：实际 P99 需叠加源站回源概率 (1-Hit_Rate) 的影响，修正公式为 P99_actual = Hit_Rate * P99_ca

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N157

## Claim

P99 延迟修正项：实际 P99 需叠加源站回源概率 (1-Hit_Rate) 的影响，修正公式为 P99_actual = Hit_Rate * P99_cache + (1-Hit_Rate) * P99_origin，其中 P99_origin 由 N47 定义。

## Corrected Claim

P99 延迟修正项：实际 P99 需叠加源站回源概率 (1-Hit_Rate) 的影响，修正公式为 P99_actual = Hit_Rate * P99_cache + (1-Hit_Rate) * P99_origin，其中 P99_origin 由 N47 定义。

## Evidence

先验知识/题面给定，逻辑校验通过
