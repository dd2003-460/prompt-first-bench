# N38: 共享随机源：买家决策噪声源。买家在搜索停止时的随机扰动 ε_buyer 来源于对‘继续搜索期望效用’的不确定性，其分布假设为 ε_buyer ~ N(0, σ_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N8

## Claim

共享随机源：买家决策噪声源。买家在搜索停止时的随机扰动 ε_buyer 来源于对‘继续搜索期望效用’的不确定性，其分布假设为 ε_buyer ~ N(0, σ_buyer²)，其中 σ_buyer 与买家搜索历史长度负相关（搜索越久，噪声越小）。

## Corrected Claim

买家决策噪声源 ε_buyer 通常被建模为均值为零的随机变量，其方差 σ_buyer² 随买家搜索历史长度增加而减小（即搜索越久，决策不确定性越低）。

## Evidence

[质询]该陈述包含具体的模型假设（正态分布、噪声与搜索历史长度的负相关性），属于经验性或特定模型设定，无法从第一性原理严格推导，且缺乏外部来源支持其具体参数形式（如为何是正态分布而非其他分布，负相关的具体函数形式）。 | 逻辑自洽（搜索越久信息越多，不确定性/噪声越小符合直觉），但作为经验事实/模型假设，缺乏来源直接支持，且检索无可用来源，依据经验事实排除条款降级。

## Search Query

buyer search stopping rule noise reduction search history
