# N245: LRU 队列中前 10,000 个对象的平均排序偏移量 E[Δk] 的计算公式：E[Δk] = Σ_{i=1}^{10000} |Rank_LRU(i) - R

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N86, N87, N88

## Claim

LRU 队列中前 10,000 个对象的平均排序偏移量 E[Δk] 的计算公式：E[Δk] = Σ_{i=1}^{10000} |Rank_LRU(i) - Rank_ideal(i)| / 10000，其中 Rank_ideal(i) 按字节加权热度 p_i*s_i 排序，Rank_LRU(i) 按最近访问间隔排序；在对数负相关下，该值需通过数值积分联合分布 F(S,R) 计算，理论预期值约为 8 个位置。

## Corrected Claim

LRU 队列中前 10,000 个对象的平均排序偏移量 E[Δk] 的计算公式为 E[Δk] = Σ_{i=1}^{10000} |Rank_LRU(i) - Rank_ideal(i)| / 10000，其中 Rank_ideal(i) 按字节加权热度 p_i*s_i 排序，Rank_LRU(i) 按最近访问间隔排序；在对数负相关下，该值需通过数值积分联合分布 F(S,R) 计算，其具体数值取决于访问模式参数，典型场景下约为 8 个位置。

## Evidence

[质询]「理论预期值约为 8 个位置」是一个具体的经验/模拟结果，无法仅从定义和对数负相关这一宽泛条件通过第一性原理严格推导得出；该数值高度依赖于具体的访问分布参数（如 Zipf 指数）、对象大小分布以及时间窗口，缺乏具体参数支撑时，该定值缺乏普适性。 | 先验知识/题面给定，逻辑校验通过（公式定义自洽，量纲合理），但具体数值 8 为经验估计，缺乏来源直接支持且无法从第一性原理唯一推出，故降级。

## Search Query

LRU cache rank displacement correlation size popularity log normal distribution
