# N98: Quality_Score 的归一化计算：以 BF16 精度下的 MMLU 分数为基准 1.0，其他精度（FP8, INT8, W4）的 MMLU 分数除以 B

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N37

## Claim

Quality_Score 的归一化计算：以 BF16 精度下的 MMLU 分数为基准 1.0，其他精度（FP8, INT8, W4）的 MMLU 分数除以 BF16 分数得到归一化值。例如，若 BF16 MMLU=0.85, FP8 MMLU=0.84, 则 Quality_Score_FP8 = 0.84/0.85 ≈ 0.988

## Corrected Claim

Quality_Score 的一种常见归一化计算方式是：以 BF16 精度下的 MMLU 分数为基准 1.0，其他精度的 MMLU 分数除以 BF16 分数得到归一化值。

## Evidence

[质询]该陈述描述了一种特定的归一化计算方法（以BF16为基准1.0），属于方法论或特定实验设定的定义，而非通用的物理或数学定律。参考来源[1]和[2]主要讨论量化对MMLU分数的影响及格式对比，并未明确提及或支持这种特定的'除以BF16分数'的归一化公式。此外，来源[1]指出INT8分数可能因噪声高于BF16，若按此公式计算，归一化值可能大于1，这与通常'量化导致质量下降'的直觉（隐含归一化值<1）可能存在语境上的冲突，但逻辑上公式本身是自洽的。主要问题在于缺乏来源直接支持该特定计算口径。 | 逻辑自洽（除法归一化是标准做法），但参考来源[1][2]仅讨论量化对MMLU的影响，未直接支持该特定归一化公式的定义，属于经验/方法论事实且缺直接来源支持。

## Search Query

Qwen3-27B MMLU benchmark BF16 FP8 INT8 W4 quantization accuracy drop

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_01163/article/details/167791372&rut=9b68af2079d1314816a9fb9266ffaa7c1a5a57286eeafad9cf0ad71e369d4e1e', 'type': 'ddg', 'title': '量化损失有多大？Qwen3-1.7B MMLU质量评测与端侧部署取舍完全指南-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00128/article/details/150962085&rut=e75cd52c9e3f93065c251dcde434138e965aba6c0a00391bb673f5140d6b427f', 'type': 'ddg', 'title': 'llama.cpp数据格式：BF16/F16/Q8_0量化对比 - CSDN博客'}
