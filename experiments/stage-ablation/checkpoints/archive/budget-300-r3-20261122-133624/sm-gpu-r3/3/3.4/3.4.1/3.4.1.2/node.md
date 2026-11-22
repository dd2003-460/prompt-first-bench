# N276: C4 数据集前 5% 作为校准集时，其 token 频率分布与 MMLU 测试集的 KL 散度值约为 0.15-0.25 bits/token，对应长尾 tok

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N87

## Claim

C4 数据集前 5% 作为校准集时，其 token 频率分布与 MMLU 测试集的 KL 散度值约为 0.15-0.25 bits/token，对应长尾 token（频率 < 1e-4）的覆盖率为 85%-90%；而 WikiText-103 的 KL 散度约为 0.35-0.45 bits/token，长尾覆盖率为 60%-70%。

## Corrected Claim

C4 数据集前 5% 作为校准集时，其 token 频率分布与 MMLU 测试集的 KL 散度通常低于 WikiText-103，且对长尾 token 的覆盖率更高。

## Evidence

[质询]具体数值（KL散度0.15-0.25 vs 0.35-0.45，覆盖率85-90% vs 60-70%）属于特定实验条件下的经验测量值，无法从第一性原理推导，且缺乏来源支持以确认其精确量级和对比关系。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

C4 vs WikiText-103 token distribution KL divergence MMLU coverage
