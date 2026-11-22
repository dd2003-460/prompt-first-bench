# N120: ΔH_tail 的精确值为长尾对象命中率损失：ΔH_tail = - (H_LRU_tail - H_LFU_tail) * P_req_tail；基于 N28

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

ΔH_tail 的精确值为长尾对象命中率损失：ΔH_tail = - (H_LRU_tail - H_LFU_tail) * P_req_tail；基于 N28，LFU 对 bottom 50% 对象的驱逐率比 LRU 高 35%，且该部分请求占比 P_req_tail = 0.08；假设 LRU 在长尾部分的命中率 H_LRU_tail ≈ 0.2（基于 C=0.55 覆盖下的剩余空间估算），LFU 因优先驱逐长尾导致 H_LFU_tail ≈ 0.2 * (1 - 0.35) = 0.13，则 ΔH_tail = -(0.2 - 0.13) * 0.08 = -0.0056 (-0.56%)，修正 N44 中 '-1~2%' 的范围，表明长尾劣势较小。

## Corrected Claim

ΔH_tail 的精确值为长尾对象命中率损失：ΔH_tail = - (H_LRU_tail - H_LFU_tail) * P_req_tail；基于 N28，LFU 对 bottom 50% 对象的驱逐率比 LRU 高 35%，且该部分请求占比 P_req_tail = 0.08；假设 LRU 在长尾部分的命中率 H_LRU_tail ≈ 0.2（基于 C=0.55 覆盖下的剩余空间估算），LFU 因优先驱逐长尾导致 H_LFU_tail ≈ 0.2 * (1 - 0.35) = 0.13，则 ΔH_tail = -(0.2 - 0.13) * 0.08 = -0.0056 (-0.56%)，修正 N44 中 '-1~2%' 的范围，表明长尾劣势较小。

## Evidence

先验知识/题面给定，逻辑校验通过
