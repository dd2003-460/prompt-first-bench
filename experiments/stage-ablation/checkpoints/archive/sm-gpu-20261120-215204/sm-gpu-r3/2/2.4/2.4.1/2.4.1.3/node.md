# N218: GPTQ-4bit 量化导致的 MMLU 绝对下降幅度为 2.7 分 (82.5 - 79.8)，相对下降率为 3.27% (2.7 / 82.5)，符合 2-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N76, N77, N78

## Claim

GPTQ-4bit 量化导致的 MMLU 绝对下降幅度为 2.7 分 (82.5 - 79.8)，相对下降率为 3.27% (2.7 / 82.5)，符合 2-5 分的预期区间

## Corrected Claim

GPTQ-4bit 量化导致的 MMLU 绝对下降幅度为 2.7 分 (82.5 - 79.8)，相对下降率为 3.27% (2.7 / 82.5)，符合 2-5 分的预期区间

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（82.5-79.8=2.7, 2.7/82.5≈3.27%），且GPTQ-4bit在MMLU上的性能损失通常确实在2-5分区间内，符合领域常识。
