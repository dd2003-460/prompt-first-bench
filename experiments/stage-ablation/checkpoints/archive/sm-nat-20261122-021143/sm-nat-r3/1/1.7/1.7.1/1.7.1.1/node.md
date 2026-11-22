# N100: 修正 N38 的 H_LRU 基线：根据 N58 推导，LRU 稳态字节命中率 H_LRU = 0.92（而非 0.85），代入 LFU 增益公式 Δ_max 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

修正 N38 的 H_LRU 基线：根据 N58 推导，LRU 稳态字节命中率 H_LRU = 0.92（而非 0.85），代入 LFU 增益公式 Δ_max ≈ (1 - H_LRU) * (1 - β/α) * |ρ| 得 Δ_max = 0.08 * 0.182 * 0.3 ≈ 0.0044，即 LFU 最多提升 0.44 个百分点

## Corrected Claim

修正 N38 的 H_LRU 基线：根据 N58 推导，LRU 稳态字节命中率 H_LRU = 0.92（而非 0.85），代入 LFU 增益公式 Δ_max ≈ (1 - H_LRU) * (1 - β/α) * |ρ| 得 Δ_max = 0.08 * 0.182 * 0.3 ≈ 0.0044，即 LFU 最多提升 0.44 个百分点

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 0.08 * 0.182 * 0.3 = 0.004368 ≈ 0.0044 正确，且 0.0044 对应 0.44 个百分点，量纲与数值自洽。
