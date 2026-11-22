# N291: KL 散度对最终任务准确率（MMLU-Pro）的映射函数：即 Delta_MMLU ≈ α * Mean_KL，其中 α 为模型对分布偏差的敏感度系数，需通过线

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

KL 散度对最终任务准确率（MMLU-Pro）的映射函数：即 Delta_MMLU ≈ α * Mean_KL，其中 α 为模型对分布偏差的敏感度系数，需通过线性回归拟合不同量化精度下的 (KL, MMLU) 数据点得出

## Corrected Claim

KL 散度对最终任务准确率（MMLU-Pro）的映射函数：即 Delta_MMLU ≈ α * Mean_KL，其中 α 为模型对分布偏差的敏感度系数，需通过线性回归拟合不同量化精度下的 (KL, MMLU) 数据点得出

## Evidence

先验知识/题面给定，逻辑校验通过
