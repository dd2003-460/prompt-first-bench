# N134: 计算利用率(MFU)修正：实际Prefill速度受MFU (Model FLOPs Utilization) 限制，通常大型LLM在优化框架下MFU为40%-6

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

计算利用率(MFU)修正：实际Prefill速度受MFU (Model FLOPs Utilization) 限制，通常大型LLM在优化框架下MFU为40%-60%。若MFU=50%，RTX 4090实际Prefill耗时 ≈ 34.0s / 0.5 = 68.0s; H100 ≈ 2.84s / 0.5 = 5.68s。

## Corrected Claim

计算利用率(MFU)修正：实际Prefill速度受MFU (Model FLOPs Utilization) 限制，通常大型LLM在优化框架下MFU为40%-60%。若MFU=50%，RTX 4090实际Prefill耗时 ≈ 34.0s / 0.5 = 68.0s; H100 ≈ 2.84s / 0.5 = 5.68s。

## Evidence

先验知识/题面给定，逻辑校验通过：MFU定义及40%-60%的典型范围符合工程常识，算术推导（34.0/0.5=68.0, 2.84/0.5=5.68）正确。
