# N127: 工作点3（主动推送/即时失效）：H_dynamic_hit ≈ 0，因为对象更新后缓存立即失效，且重新缓存需等待下次请求。若采用预取机制，H_dynamic_h

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

工作点3（主动推送/即时失效）：H_dynamic_hit ≈ 0，因为对象更新后缓存立即失效，且重新缓存需等待下次请求。若采用预取机制，H_dynamic_hit ≈ P_prefetch_success。假设预取覆盖10%的更新对象，P_prefetch_success ≈ 0.1 * 0.9 (90%预取准确) ≈ 0.09。H_dynamic_hit ≈ 0.09 * P_invalid。若 P_invalid=0.01，H_dynamic_hit ≈ 0.0009 (0.09%)。

## Corrected Claim

工作点3（主动推送/即时失效）：H_dynamic_hit ≈ 0，因为对象更新后缓存立即失效，且重新缓存需等待下次请求。若采用预取机制，H_dynamic_hit ≈ P_prefetch_success。假设预取覆盖10%的更新对象，P_prefetch_success ≈ 0.1 * 0.9 (90%预取准确) ≈ 0.09。H_dynamic_hit ≈ 0.09 * P_invalid。若 P_invalid=0.01，H_dynamic_hit ≈ 0.0009 (0.09%)。

## Evidence

先验知识/题面给定，逻辑校验通过
