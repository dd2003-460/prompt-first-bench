# N168: 社区实测（如 HuggingFace 社区 GitHub Issue 或 Reddit 帖子）通常基于特定量化精度（如 INT8/FP8）和特定框架（如 vLL

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

社区实测（如 HuggingFace 社区 GitHub Issue 或 Reddit 帖子）通常基于特定量化精度（如 INT8/FP8）和特定框架（如 vLLM），其数据波动范围大（±30%），需取中位数并标注具体配置（如 batch size、序列长度）。

## Corrected Claim

社区实测（如 HuggingFace 社区 GitHub Issue 或 Reddit 帖子）通常基于特定量化精度（如 INT8/FP8）和特定框架（如 vLLM），其数据波动范围大（±30%），需取中位数并标注具体配置（如 batch size、序列长度）。

## Evidence

先验知识/题面给定，逻辑校验通过
