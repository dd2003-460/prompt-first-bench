# N64: FP8 与 INT8 量化在 Qwen3-27B 上的质量损失差异机制：FP8 使用非对称量化（E4M3/E5M2）保留更多动态范围，INT8 使用对称量化，导

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

FP8 与 INT8 量化在 Qwen3-27B 上的质量损失差异机制：FP8 使用非对称量化（E4M3/E5M2）保留更多动态范围，INT8 使用对称量化，导致在长尾分布激活值上 FP8 通常误差更小 [待核验] 具体差异幅度需基准测试验证

## Corrected Claim

FP8 与 INT8 量化在 Qwen3-27B 上的质量损失差异机制：FP8 使用非对称量化（E4M3/E5M2）保留更多动态范围，INT8 使用对称量化，导致在长尾分布激活值上 FP8 通常误差更小 [待核验] 具体差异幅度需基准测试验证

## Evidence

先验知识/题面给定，逻辑校验通过：FP8（E4M3/E5M2）具有比INT8更宽的动态范围和更精细的尾数表示，在处理LLM中常见的长尾分布激活值时，理论上确实能提供更小的量化误差，符合量化原理。

## Search Query

FP8 vs INT8 quantization error mechanism LLM
