# N716: 长尾区域延迟 CDF F_tail(x) 的解析表达式取决于混合策略中长尾流量去向：若长尾走公有云，F_tail(x) = F_cloud(x)（公有云 CDF

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N238

## Claim

长尾区域延迟 CDF F_tail(x) 的解析表达式取决于混合策略中长尾流量去向：若长尾走公有云，F_tail(x) = F_cloud(x)（公有云 CDF，见 N53/N54）；若长尾走自建 POP（假设），则 F_tail(x) = F_pop_tail(x)，其 P99 值比 F_core 高 10-20ms（见 N191）。

## Corrected Claim

长尾区域延迟 CDF F_tail(x) 的解析表达式取决于混合策略中长尾流量去向：若长尾走公有云，F_tail(x) = F_cloud(x)（公有云 CDF，见 N53/N54）；若长尾走自建 POP（假设），则 F_tail(x) = F_pop_tail(x)，其 P99 值比 F_core 高 10-20ms（见 N191）。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述定义了条件分支下的CDF映射关系，逻辑自洽且量级合理（10-20ms延迟差异符合网络架构常识），无内部矛盾。
