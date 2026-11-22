# N62: 数值一致性检查：使用修正公式 H_corrected = H_LRU * K，其中 K = E[S_hit]/E[S_miss] ≈ 0.7（基于 N49 估算

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

数值一致性检查：使用修正公式 H_corrected = H_LRU * K，其中 K = E[S_hit]/E[S_miss] ≈ 0.7（基于 N49 估算），H_LRU ≈ 0.587，则 H_corrected ≈ 0.411。这与 N20 中 H_bytes 的预期范围一致，验证了方向修正的正确性。若使用原公式 H_LRU / K，则 H_corrected ≈ 0.839，与字节命中率下降的物理直觉矛盾。

## Corrected Claim

数值一致性检查：使用修正公式 H_corrected = H_LRU * K，其中 K = E[S_hit]/E[S_miss] ≈ 0.7（基于 N49 估算），H_LRU ≈ 0.587，则 H_corrected ≈ 0.411。这与 N20 中 H_bytes 的预期范围一致，验证了方向修正的正确性。若使用原公式 H_LRU / K，则 H_corrected ≈ 0.839，与字节命中率下降的物理直觉矛盾。

## Evidence

先验知识/题面给定，逻辑校验通过：0.587 * 0.7 ≈ 0.411 且 0.587 / 0.7 ≈ 0.839，数值计算准确，且符合命中率修正的物理直觉（命中代价低于未命中，故修正后命中率应低于原始LRU命中率）。
