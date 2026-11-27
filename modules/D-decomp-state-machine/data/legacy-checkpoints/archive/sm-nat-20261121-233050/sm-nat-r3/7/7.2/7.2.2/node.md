# N157: LFU缓存集合中对象的平均访问频率 F_LFU_avg 的量化估算：LFU 缓存保留频率排名前 K=50,000 的对象（即 Top 50% 频率分位）。其平均

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N62

## Claim

LFU缓存集合中对象的平均访问频率 F_LFU_avg 的量化估算：LFU 缓存保留频率排名前 K=50,000 的对象（即 Top 50% 频率分位）。其平均频率为 E[F | Rank_F ∈ [0, 0.5N]] ≈ (Total_Freq * (1 - 0.5^(-β+1))) / (0.5N)。该值显著高于 F_LRU_avg，是 LFU 增益的主要来源。

## Corrected Claim

LFU缓存保留频率排名前K=50,000的对象（Top 50%频率分位）。其平均频率显著高于全局平均频率F_avg，具体数值需通过Zipf分布的累积分布函数积分计算得出，而非简单代数式。该高频特性是LFU相比LRU在局部性原理下增益的主要来源。

## Evidence

[质询]公式推导存在严重的数学逻辑错误：在Zipf分布下，Top 50%对象的平均频率并非由简单的 (1 - 0.5^(-β+1)) 项决定，且该表达式量纲和数值逻辑不自洽（例如当β=1时，分母为0.5N，分子项为1-0.5=0.5，结果为Total_Freq/N，即全局平均，这与'显著高于平均'的结论矛盾；当β>1时，Top 50%的平均频率应显著高于全局平均，但给出的公式结构无法正确反映Zipf分布的累积分布函数积分结果）。 | 逻辑校验失败：给出的数学公式无法从Zipf分布的第一性原理推导得出，且存在内部矛盾（如β=1时的特例反证）。由于source为search且无可用外部来源支持，根据经验事实排除条款及逻辑错误，判定为degraded（保留定性结论但修正定量公式）。

## Search Query

LFU cache top K objects average frequency Pareto distribution beta 0.9 head interval
