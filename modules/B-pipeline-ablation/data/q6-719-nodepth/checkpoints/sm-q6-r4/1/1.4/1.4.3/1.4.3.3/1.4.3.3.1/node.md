# N715: 核心区域延迟 CDF F_core(x) 的解析表达式为 F_core(x) = H_pop * F_hit(x) + (1 - H_pop) * F_miss

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N238

## Claim

核心区域延迟 CDF F_core(x) 的解析表达式为 F_core(x) = H_pop * F_hit(x) + (1 - H_pop) * F_miss(x)，其中 H_pop 为 POP 缓存命中率（已知 N105），F_hit(x) 为命中时的延迟 CDF（主要取决于 RTT_user_pop，见 N189/N191），F_miss(x) 为 Miss 时的延迟 CDF（取决于 RTT_user_pop + RTT_pop_origin + T_transfer，见 N108/N129）。

## Corrected Claim

核心区域延迟 CDF F_core(x) 的解析表达式为 F_core(x) = H_pop * F_hit(x) + (1 - H_pop) * F_miss(x)，其中 H_pop 为 POP 缓存命中率（已知 N105），F_hit(x) 为命中时的延迟 CDF（主要取决于 RTT_user_pop，见 N189/N191），F_miss(x) 为 Miss 时的延迟 CDF（取决于 RTT_user_pop + RTT_pop_origin + T_transfer，见 N108/N129）。

## Evidence

先验知识/题面给定，逻辑校验通过：该表达式符合全概率公式（Total Probability Law）在延迟分布上的应用，即总延迟分布由命中路径和未命中路径按命中率加权混合而成，逻辑自洽且量纲正确。
