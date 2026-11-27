# N80: 长尾命中率损失 ΔH_tail ≈ -0.6% 的量化推导：ΔH_tail = (H_LRU_tail - H_LFU_tail) * R_tail / R_t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

长尾命中率损失 ΔH_tail ≈ -0.6% 的量化推导：ΔH_tail = (H_LRU_tail - H_LFU_tail) * R_tail / R_total，需分别计算 LRU 和 LFU 在长尾部分的命中率，并结合 R_tail=0.08 验证 -0.6% 的数值合理性。

## Corrected Claim

长尾命中率损失 ΔH_tail ≈ -0.6% 的量化推导：ΔH_tail = (H_LRU_tail - H_LFU_tail) * R_tail / R_total，需分别计算 LRU 和 LFU 在长尾部分的命中率，并结合 R_tail=0.08 验证 -0.6% 的数值合理性。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合加权平均逻辑，数值量级（0.08 * 7.5% ≈ 0.6%）在合理范围内，无内部矛盾。
