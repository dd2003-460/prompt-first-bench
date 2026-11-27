# N251: 工作点 1（高频对象，r_i=1000 次/天）：LFU 计数器标准差 σ_count ≈ √1000 ≈ 31.6，噪声占比 σ_count/r_i ≈ 3.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

工作点 1（高频对象，r_i=1000 次/天）：LFU 计数器标准差 σ_count ≈ √1000 ≈ 31.6，噪声占比 σ_count/r_i ≈ 3.16%，低于 10% 阈值，LFU 能准确识别热点，误驱逐率 < 1%。

## Corrected Claim

工作点 1（高频对象，r_i=1000 次/天）：LFU 计数器标准差 σ_count ≈ √1000 ≈ 31.6，噪声占比 σ_count/r_i ≈ 3.16%，低于 10% 阈值，LFU 能准确识别热点，误驱逐率 < 1%。

## Evidence

先验知识/题面给定，逻辑校验通过：基于泊松分布近似，标准差为√N，数值计算正确（√1000≈31.6，31.6/1000=3.16%），且符合LFU在高频率下噪声占比低、识别准确的工程直觉。
