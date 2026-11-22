# N137: 在假设对象大小分布为 Pareto(α=1.1, x_min=1KB) 且无截断的理论上界工作点下，E[S] 无界，但实际受内存对齐和最大对象大小 x_max=

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

在假设对象大小分布为 Pareto(α=1.1, x_min=1KB) 且无截断的理论上界工作点下，E[S] 无界，但实际受内存对齐和最大对象大小 x_max=10GB 限制，需数值积分计算实际 N_cache，若 x_max 导致 E[S] 显著增大，N_cache 可能接近 100,000，此时 λ_(N_cache) 非零，LRU 命中率下界需重新计算。

## Corrected Claim

在假设对象大小分布为 Pareto(α=1.1, x_min=1KB) 且无截断的理论上界工作点下，E[S] 无界；实际受内存对齐和最大对象大小限制时，需数值积分计算实际 N_cache，其具体数值取决于 x_max 及系统参数，可能显著增大导致 LRU 命中率下界需重新计算。

## Evidence

[质询]该陈述包含具体的工程参数（x_max=10GB）和特定的数值结论（N_cache接近100,000），属于经验事实或特定场景下的计算结果，无法仅从Pareto分布的第一性原理直接推出，且参考来源未提供该具体场景的验证数据。 | 逻辑上Pareto(α=1.1)确实导致期望无界，引入截断后需数值积分，逻辑自洽；但具体数值（100,000）缺乏来源直接支持，且来源[1][2][3]仅涉及分布定义，未覆盖该特定工程场景的计算结果。

## Search Query

Pareto distribution truncated expectation calculation

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Normal_distribution', 'type': 'wikipedia', 'title': 'Normal distribution'}
- {'url': 'https://en.wikipedia.org/wiki/Exponential_family', 'type': 'wikipedia', 'title': 'Exponential family'}
- {'url': 'https://en.wikipedia.org/wiki/Standard_deviation', 'type': 'wikipedia', 'title': 'Standard deviation'}
