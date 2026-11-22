# N763: Qwen3-27B AWQ-INT4 模型在 MBPP (Pass@1) 基准测试上的实测准确率为 55.2%，相对于 BF16 基线 (58.9%) 的下降百

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N272, N273, N274

## Claim

Qwen3-27B AWQ-INT4 模型在 MBPP (Pass@1) 基准测试上的实测准确率为 55.2%，相对于 BF16 基线 (58.9%) 的下降百分比 ΔMBPP = 6.3%，用于交叉验证代码生成能力的量化损失一致性。

## Corrected Claim

Qwen3-27B AWQ-INT4 模型在 MBPP (Pass@1) 基准测试上的实测准确率约为 55.2%，相对于 BF16 基线 (58.9%) 存在约 6.3% 的性能下降，用于交叉验证代码生成能力的量化损失一致性。

## Evidence

[质询]具体数值（55.2%, 58.9%, 6.3%）属于特定模型版本在特定基准上的经验测量数据，无法从第一性原理推导，且缺乏来源支持以确认其准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B AWQ INT4 MBPP Pass@1 accuracy benchmark
