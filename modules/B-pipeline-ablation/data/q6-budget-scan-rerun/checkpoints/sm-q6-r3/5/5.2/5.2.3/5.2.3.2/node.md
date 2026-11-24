# N262: 对象i在TTL时间窗口内的本地缓存命中率 C_i 取决于该对象在TTL内的独立请求次数 N_i，若请求间隔服从指数分布，则 C_i = 1 - e^(-N_i 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N96

## Claim

对象i在TTL时间窗口内的本地缓存命中率 C_i 取决于该对象在TTL内的独立请求次数 N_i，若请求间隔服从指数分布，则 C_i = 1 - e^(-N_i / T_avg_interval)，其中T_avg_interval为对象i的平均请求间隔，Top100对象T_avg_interval≈1s，长尾对象T_avg_interval≈3600s

## Corrected Claim

对象i在TTL时间窗口T内的本地缓存命中率 C_i 取决于该对象在TTL内的请求到达过程。若请求间隔服从均值为 T_avg_interval 的指数分布，则 C_i = 1 - e^(-T / T_avg_interval)。典型场景下，Top100对象 T_avg_interval 约为 1s，长尾对象约为 3600s。

## Evidence

[质询]公式推导存在逻辑瑕疵：若请求间隔服从指数分布，则单位时间内的请求数服从泊松分布，命中率（至少一次请求的概率）应为 1 - e^(-λT)，其中 λ=1/T_avg_interval。原公式 1 - e^(-N_i / T_avg_interval) 中 N_i 若为总请求次数，则量纲和逻辑均不成立；若 N_i 指代时间窗口 T，则符号使用混淆。此外，Top100 对象平均间隔 1s 和长尾 3600s 为经验估计值，缺乏通用性。 | 先验知识/题面给定，但公式推导逻辑不自洽（指数分布间隔对应泊松过程，命中率公式应为 1-e^(-T/T_avg) 或类似形式，原式变量定义模糊且量纲存疑），且经验参数缺乏来源支持。

## Search Query

cache hit rate exponential request interval TTL model
