# N662: API 可用率 99.9% 对应的失败率 λ_fail = 0.001，日均调用 N_calls=100 次时，期望失败次数 E[Fails] = N_call

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N242

## Claim

API 可用率 99.9% 对应的失败率 λ_fail = 0.001，日均调用 N_calls=100 次时，期望失败次数 E[Fails] = N_calls * λ_fail = 0.1 次/天

## Corrected Claim

API 可用率 99.9% 对应的失败率 λ_fail = 0.001，日均调用 N_calls=100 次时，期望失败次数 E[Fails] = N_calls * λ_fail = 0.1 次/天

## Evidence

先验知识/题面给定，逻辑校验通过：可用率99.9%对应失败率0.001，期望失败次数=100*0.001=0.1，计算无误。
