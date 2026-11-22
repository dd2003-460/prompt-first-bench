# N145: 投影1：敏感度系数 α 的校准：α 可通过回归 P_list ~ λ * (1 - β * σ²_noise) 估计。若 α=1.0，则溢价率 π 与 λ 呈线

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N36

## Claim

投影1：敏感度系数 α 的校准：α 可通过回归 P_list ~ λ * (1 - β * σ²_noise) 估计。若 α=1.0，则溢价率 π 与 λ 呈线性关系，但受噪声抑制修正。

## Corrected Claim

投影1：敏感度系数 α 的校准：α 可通过回归 P_list ~ λ * (1 - β * σ²_noise) 估计。若 α=1.0，则溢价率 π 与 λ 呈线性关系，但受噪声抑制修正。（注：此为特定模型假设，缺乏通用来源支持）

## Evidence

[质询]该陈述描述了一个特定的、非标准的经验性校准模型（P_list ~ λ * (1 - β * σ²_noise)），属于具体的实证设定或假设，而非通用的第一性原理或数学公理。参考来源[1]讨论的是现代投资组合理论中的CAPM回归（Alpha/Beta），与陈述中的敏感度系数α及噪声抑制修正模型在定义和语境上完全不同；来源[2]讨论复制危机，完全无关。因此，该陈述缺乏外部来源支持，且无法从第一性原理严格推出。 | 经验事实/特定模型设定，逻辑自洽但参考来源[1][2]均与该特定校准公式无关，无法提供直接支持。

## Search Query

sensitivity coefficient alpha loss aversion pricing regression

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Modern_portfolio_theory', 'type': 'wikipedia', 'title': 'Modern portfolio theory'}
- {'url': 'https://en.wikipedia.org/wiki/Replication_crisis', 'type': 'wikipedia', 'title': 'Replication crisis'}
