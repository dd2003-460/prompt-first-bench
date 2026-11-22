# N163: 在 Pareto(β=0.9) 热度分布下，σ_f_crit 的解析推导：σ_f_crit 定义为 LFU 频率计数器置信区间宽度超过第 K 名与第 K+1 名

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N58, N59, N60

## Claim

在 Pareto(β=0.9) 热度分布下，σ_f_crit 的解析推导：σ_f_crit 定义为 LFU 频率计数器置信区间宽度超过第 K 名与第 K+1 名对象频率差 ΔR_K 的阈值，即 σ_f_crit = ΔR_K / (R_K * √(T_obs/T_life))，需计算 T_obs/T_life 的具体比值以验证 σ_f=2.0 是否超标。

## Corrected Claim

在 Pareto(β=0.9) 热度分布下，σ_f_crit 的解析推导涉及 LFU 频率计数器置信区间宽度与频率差 ΔR_K 的关系，具体公式 σ_f_crit = ΔR_K / (R_K * √(T_obs/T_life)) 需结合特定统计假设验证，当前缺乏直接来源支持该精确形式。

## Evidence

[质询]该陈述包含具体的解析公式 σ_f_crit = ΔR_K / (R_K * √(T_obs/T_life))，这是一个经验性的工程/统计推导结论，无法从第一性原理或数学公理直接推出，且参考来源仅提供了 Pareto 分布的一般定义，未涉及 LFU 缓存策略或该特定置信区间阈值的推导，存在来源缺失风险。 | 逻辑上量纲自洽（频率差/频率为无量纲，除以时间比值的平方根符合统计误差随观测时间增加而减小的直觉），但参考来源 [1][2] 仅描述 Pareto 分布基础，与该特定 LFU 阈值公式无关，属于经验事实且缺乏直接来源支持。

## Search Query

LFU frequency counter confidence interval Pareto distribution critical sigma threshold derivation

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Pareto_distribution&rut=3541c8b3f71fd194fb160deaa36ef23bcf3225d4a84bcccff152370e666d69b5', 'type': 'ddg', 'title': 'Pareto distribution - Wikipedia'}
- {'url': 'https://zhuanlan.zhihu.com/p/27173875583&rut=c28be11bc9a983317f8edde3b6df4480ac059f02a3bf2babd869f10ca3cde565', 'type': 'ddg', 'title': '帕累托分布 - 知乎 - 知乎专栏'}
