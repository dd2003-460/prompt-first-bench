# N349: FP8 KV Cache 的累积误差机制分析：FP8 (E4M3) 的动态范围限制导致长序列中注意力分数 (Attention Scores) 的微小舍入误差随

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N125

## Claim

FP8 KV Cache 的累积误差机制分析：FP8 (E4M3) 的动态范围限制导致长序列中注意力分数 (Attention Scores) 的微小舍入误差随序列长度线性累积；理论模型表明，每增加 1K tokens，注意力分布的 KL 散度增加约 0.01-0.05 nats，需验证该累积是否在 32K 处超过人类感知阈值（通常对应 PPL 增加 >0.5）。[待核验]

## Corrected Claim

FP8 (E4M3) 的动态范围限制导致长序列中注意力分数的微小舍入误差随序列长度累积；理论模型表明，随着序列长度增加，注意力分布的 KL 散度会显著增加，需验证该累积是否在 32K 处超过人类感知阈值（通常对应 PPL 增加 >0.5）。

## Evidence

[质询]该陈述包含具体的经验性数值（每1K tokens KL散度增加0.01-0.05 nats），这属于特定硬件/算法配置下的经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持
