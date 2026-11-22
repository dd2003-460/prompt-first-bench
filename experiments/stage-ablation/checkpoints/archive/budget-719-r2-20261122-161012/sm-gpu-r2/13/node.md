# N136: 在代码生成任务中，INT4 量化导致的 HumanEval Pass@1 下降通常比通用任务更显著，实测下降幅度可达 4-6% [待核验]，若业务对代码生成准确

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在代码生成任务中，INT4 量化导致的 HumanEval Pass@1 下降通常比通用任务更显著，实测下降幅度可达 4-6% [待核验]，若业务对代码生成准确性敏感（如要求 Pass@1 > 90%），则必须排除 INT4 方案，仅保留 FP8 或 BF16，这一约束直接改变了硬件选型（需更大显存或更高带宽）。

## Corrected Claim

在代码生成任务中，INT4 量化导致的 HumanEval Pass@1 下降通常比通用任务更显著，具体下降幅度因模型和量化策略而异（实测可能达到数个百分点），若业务对代码生成准确性敏感（如要求 Pass@1 > 90%），则需评估 INT4 方案是否满足阈值，若不满足则必须排除 INT4 方案，仅保留 FP8 或 BF16，这一约束直接改变了硬件选型（需更大显存或更高带宽）。

## Evidence

[质询]具体数值“4-6%”缺乏来源支持，且不同模型/量化方法下差异巨大，属于经验事实而非第一性原理可推导结论；参考来源仅介绍HumanEval基准本身，未涉及INT4量化对Pass@1的具体影响幅度。 | 逻辑自洽（代码生成对精度敏感，INT4量化确实可能导致显著性能下降，进而影响硬件选型），但参考来源[1][2][3]仅解释HumanEval评测机制，未提供INT4量化导致Pass@1下降4-6%的具体数据支持，属于经验事实缺来源直接支持。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/qq_27590277/article/details/135163862&rut=ae4f6e4673a5e0db8c7d0a4f3045904a393ec933d8906e5865b3b6d7f91281e4', 'type': 'ddg', 'title': 'HumanEval是如何进行代码评估的：从数据构成、评估逻辑到pass@k指标计算-CSDN博客'}
- {'url': 'https://blog.csdn.net/daqianai/article/details/150299462&rut=e07dbfdb7020714256480c7b5193daf8d980d92788ccb1e0ee8318b3f006f809', 'type': 'ddg', 'title': 'HumanEval：代码生成模型的"黄金标尺" - CSDN博客'}
- {'url': 'https://www.datalearner.com/benchmarks/humaneval&rut=771c9c868dcef2dafeaf86a3409433920220d0c0ed436693eb21a361943909bb', 'type': 'ddg', 'title': 'HumanEval评测基准：大模型排名与测试结果 | DataLearnerAI'}
