# N392: ROCm版本选择建议：必须使用ROCm 6.1或更高版本以确保Qwen3-27B的Flash Attention优化；若使用ROCm 6.0，需手动验证Atte

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N147

## Claim

ROCm版本选择建议：必须使用ROCm 6.1或更高版本以确保Qwen3-27B的Flash Attention优化；若使用ROCm 6.0，需手动验证Attention内核是否调用优化路径，否则性能损失可达30-40%，使MI300X方案不可行。

## Corrected Claim

建议使用ROCm 6.1或更高版本以利用Qwen3-27B的Flash Attention优化；若使用ROCm 6.0，需手动验证Attention内核是否调用优化路径，否则可能面临显著性能损失，影响MI300X方案的可行性。

## Evidence

[质询]具体数值（30-40%性能损失）和特定版本阈值（ROCm 6.1）属于经验性工程参数，缺乏通用第一性原理支持，且不同模型/驱动组合下表现可能差异巨大，存在过度具体化风险。 | 先验知识/题面给定，逻辑校验通过（版本迭代通常伴随内核优化，性能损失量级在合理范围内），但作为经验事实缺乏直接来源支持，故降级。

## Search Query

ROCm version requirements for Qwen3 Flash Attention optimization
