# N520: 标准化基准测试的输入长度固定为32K tokens，需明确该长度对应的具体数据集或合成文本生成方法（如随机token序列、真实长文档截断），以确保不同硬件测试输

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N162

## Claim

标准化基准测试的输入长度固定为32K tokens，需明确该长度对应的具体数据集或合成文本生成方法（如随机token序列、真实长文档截断），以确保不同硬件测试输入的一致性

## Corrected Claim

标准化基准测试的输入长度固定为32K tokens，需明确该长度对应的具体数据集或合成文本生成方法（如随机token序列、真实长文档截断），以确保不同硬件测试输入的一致性

## Evidence

先验知识/题面给定，逻辑校验通过
