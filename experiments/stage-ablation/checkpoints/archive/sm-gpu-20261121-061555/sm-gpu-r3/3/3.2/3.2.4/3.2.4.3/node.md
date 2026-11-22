# N244: W4A8 量化误差对代码生成任务（HumanEval/MBPP）Pass@1 的具体影响幅度，若 PPL 增加 1-3% 导致 Pass@1 下降超过 2%，则

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82

## Claim

W4A8 量化误差对代码生成任务（HumanEval/MBPP）Pass@1 的具体影响幅度，若 PPL 增加 1-3% 导致 Pass@1 下降超过 2%，则 W4A8 在代码场景不可接受，需查找特定于代码任务的量化敏感度数据。

## Corrected Claim

W4A8 量化误差对代码生成任务（HumanEval/MBPP）Pass@1 的具体影响幅度需通过实验测定；若观察到 PPL 显著增加且 Pass@1 下降超过可接受阈值（如 2%），则表明 W4A8 在代码场景可能不可接受，需查找特定于代码任务的量化敏感度数据。

## Evidence

[质询]该陈述包含具体的经验性阈值（PPL增加1-3%导致Pass@1下降>2%），属于特定模型和量化方案下的经验事实，无法从第一性原理推导，且缺乏来源支持其具体数值的有效性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

W4A8 quantization impact on code generation accuracy HumanEval MBPP pass@1 drop
