# N320: H100 相比 A100 在 BF16 下的吞吐量提升幅度 = (H100_Bandwidth / A100_Bandwidth) * (H100_Effect

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

H100 相比 A100 在 BF16 下的吞吐量提升幅度 = (H100_Bandwidth / A100_Bandwidth) * (H100_Effective_Overhead / A100_Effective_Overhead)，假设有效带宽利用率相同，则提升比例 = 3350/2039 ≈ 1.64x (64% 提升)，主要得益于 HBM3 带宽优势

## Corrected Claim

H100 相比 A100 在 BF16 下的吞吐量提升幅度 = (H100_Bandwidth / A100_Bandwidth) * (H100_Effective_Overhead / A100_Effective_Overhead)，假设有效带宽利用率相同，则提升比例 = 3350/2039 ≈ 1.64x (64% 提升)，主要得益于 HBM3 带宽优势

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 HBM3带宽约3.35TB/s，A100 SXM4 HBM2e带宽约2.039TB/s，比值约1.64，符合物理规格与算术推导。
