# N592: B200 上 NVFP4 权重的反量化开销在 FP8 混合精度模式下可降至 3-5%，实际 Decode 吞吐上限约为理论带宽上限的 95-97%，即 549 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N181

## Claim

B200 上 NVFP4 权重的反量化开销在 FP8 混合精度模式下可降至 3-5%，实际 Decode 吞吐上限约为理论带宽上限的 95-97%，即 549 * 0.96 ≈ 527 tokens/s [待核验]

## Corrected Claim

在B200上，NVFP4权重的反量化开销在FP8混合精度模式下预计较低，实际Decode吞吐上限接近理论带宽上限，具体数值需根据实际硬件测试确定。

## Evidence

[质询]该陈述包含具体的硬件性能指标（NVFP4反量化开销3-5%、Decode吞吐效率95-97%）及特定计算结果（549 * 0.96 ≈ 527），属于经验事实。由于检索无可用来源，无法验证这些具体数值是否准确，且不同模型/配置下反量化开销和吞吐效率可能存在显著差异，存在数值量级或具体参数不准确的风险。 | 经验事实，逻辑自洽但缺来源支持。数学计算 549 * 0.96 = 527.04 ≈ 527 正确，但具体性能参数（3-5%开销、95-97%效率）无法通过第一性原理推导，且无外部来源佐证。

## Search Query

NVFP4 FP8 hybrid precision dequantization overhead B200
