# N18: 量化方法对质量损失的具体影响机制：PTQ (Post-Training Quantization) vs GPTQ vs AWQ vs SmoothQuant 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

量化方法对质量损失的具体影响机制：PTQ (Post-Training Quantization) vs GPTQ vs AWQ vs SmoothQuant 的差异；W4A16与W4A8的激活值量化影响；关键阈值：通常W8A8质量损失<1% PPL，W4A16质量损失<3-5% PPL，W4A4质量损失可能>10% PPL [时效待核]

## Corrected Claim

量化方法对质量损失的具体影响机制：PTQ (Post-Training Quantization) vs GPTQ vs AWQ vs SmoothQuant 的差异；W4A16与W4A8的激活值量化影响；关键阈值：通常W8A8质量损失<1% PPL，W4A16质量损失<3-5% PPL，W4A4质量损失可能>10% PPL [时效待核]

## Evidence

先验知识/题面给定，逻辑校验通过
