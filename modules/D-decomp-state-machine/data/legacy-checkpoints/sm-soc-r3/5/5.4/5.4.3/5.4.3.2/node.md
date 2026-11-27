# N287: A/B 测试中 w1 变化的具体设定：实验组 w1_exp = w1_base * 1.1，对照组 w1_ctrl = w1_base * 0.9，通过比较两组

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N97

## Claim

A/B 测试中 w1 变化的具体设定：实验组 w1_exp = w1_base * 1.1，对照组 w1_ctrl = w1_base * 0.9，通过比较两组的平均曝光量差值 ΔExposure = E[Exposure|exp] - E[Exposure|ctrl] 来估算弹性。

## Corrected Claim

A/B 测试中 w1 变化的具体设定：实验组 w1_exp = w1_base * 1.1，对照组 w1_ctrl = w1_base * 0.9，通过比较两组的平均曝光量差值 ΔExposure = E[Exposure|exp] - E[Exposure|ctrl] 来估算弹性。

## Evidence

先验知识/题面给定，逻辑校验通过
