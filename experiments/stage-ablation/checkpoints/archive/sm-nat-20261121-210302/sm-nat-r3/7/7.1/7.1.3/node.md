# N202: LFU 热点对象平均大小 S_LFU_hot 在头部 10% 对象上的数值：S_LFU_hot_10% = E[S | Top 10%]，通过 Pareto(α

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75

## Claim

LFU 热点对象平均大小 S_LFU_hot 在头部 10% 对象上的数值：S_LFU_hot_10% = E[S | Top 10%]，通过 Pareto(α=1.1) 大小分布与 Pareto(β=0.9) 热度分布的联合分布计算，具体数值需通过数值积分或 Monte Carlo 模拟得到。

## Corrected Claim

LFU 热点对象平均大小 S_LFU_hot 在头部 10% 对象上的数值 S_LFU_hot_10% = E[S | Top 10%]，理论上可通过 Pareto(α=1.1) 大小分布与 Pareto(β=0.9) 热度分布的联合分布计算，具体数值需通过数值积分或 Monte Carlo 模拟得到（注：当前缺乏具体数值及外部来源验证）。

## Evidence

[质询]该陈述声称通过特定参数（Pareto α=1.1, β=0.9）的联合分布计算得出具体数值，但陈述本身未给出该数值，且参考来源中完全缺乏关于 LFU 缓存策略、特定 Pareto 参数下的热点对象大小分布或相关数值积分结果的信息，属于缺乏外部证据支持的经验性/模型推导事实。 | 逻辑上，基于给定的 Pareto 分布参数计算条件期望在数学上是自洽且可行的；但参考来源 [1][2][3] 均与 LFU 缓存或特定 Pareto 参数下的对象大小分布无关，无法提供直接支持，符合经验事实排除条款中‘逻辑自洽但缺来源支持’的情形。

## Search Query

average size top 10% popular objects Pareto distribution negative correlation

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/List_of_algorithms', 'type': 'wikipedia', 'title': 'List of algorithms'}
- {'url': 'https://en.wikipedia.org/wiki/John_von_Neumann', 'type': 'wikipedia', 'title': 'John von Neumann'}
- {'url': 'https://en.wikipedia.org/wiki/Human_impact_on_the_environment', 'type': 'wikipedia', 'title': 'Human impact on the environment'}
