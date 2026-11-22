# N185: W4量化中Scale和Zero-point参数的存储格式通常为FP16，每128个权重一组，额外开销计算为 (128 * 2 bytes) / (128 * 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

W4量化中Scale和Zero-point参数的存储格式通常为FP16，每128个权重一组，额外开销计算为 (128 * 2 bytes) / (128 * 0.5 bytes) = 400% of weight size? 不，是 (2 bytes per group) / (0.5 bytes per weight * 128 weights) = 2/64 = 3.125% overhead. 修正：若每128权重一个FP16 Scale，开销为 (2/128)/0.5 = 3.125%。若每256权重一个，开销减半为1.56%。N57中0.5-1%的估计偏低，实际应为1.5-3.1%。

## Corrected Claim

W4量化中Scale和Zero-point参数的存储格式通常为FP16，每128个权重一组，额外开销计算为 (128 * 2 bytes) / (128 * 0.5 bytes) = 400% of weight size? 不，是 (2 bytes per group) / (0.5 bytes per weight * 128 weights) = 2/64 = 3.125% overhead. 修正：若每128权重一个FP16 Scale，开销为 (2/128)/0.5 = 3.125%。若每256权重一个，开销减半为1.56%。N57中0.5-1%的估计偏低，实际应为1.5-3.1%。

## Evidence

先验知识/题面给定，逻辑校验通过：W4量化中FP16 Scale/Zero-point每128权重一组的开销计算 (2 bytes / (128 * 0.5 bytes)) = 3.125% 符合数学逻辑与工程常识。

## Search Query

W4 quantization scale zero point overhead FP16 group size 128 256
