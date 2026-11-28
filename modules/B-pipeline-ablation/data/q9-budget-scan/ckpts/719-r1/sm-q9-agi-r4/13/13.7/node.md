# N334: LLM-as-a-Judge 的评分方差（Score Variance）随温度（Temperature）设置增加而增大：Temperature=0.0 时方差 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N104, N105, N106

## Claim

LLM-as-a-Judge 的评分方差（Score Variance）随温度（Temperature）设置增加而增大：Temperature=0.0 时方差 < 0.05，Temperature=0.7 时方差 > 0.20；为确保评分稳定性，必须锁定 Temperature=0.0 并启用 Best-of-N（N=5）投票机制，以将评分标准差控制在 < 0.10。

## Corrected Claim

LLM-as-a-Judge 的评分方差通常随温度设置增加而增大；为确保评分稳定性，建议降低温度（如设为0.0）并结合多次采样投票机制（如Best-of-N）以降低评分波动。

## Evidence

[质询]具体数值阈值（如方差<0.05, >0.20, 标准差<0.10）及特定配置（Best-of-N N=5）缺乏通用性，不同LLM模型、评分任务及评分量表下数值差异巨大，属于特定实验条件下的经验数据而非普适规律。 | 先验知识/题面给定，逻辑校验通过（温度升高导致采样随机性增加从而增大方差符合基本概率原理），但具体数值阈值缺乏通用来源支持，属经验事实。
