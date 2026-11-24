# N341: 回源请求对源站处理延迟的冲击：源站 QPS 增加 ΔQPS_back = R_daily * (1-H_fault) - R_daily * (1-H_stea

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

回源请求对源站处理延迟的冲击：源站 QPS 增加 ΔQPS_back = R_daily * (1-H_fault) - R_daily * (1-H_steady) = 1.34e9 * 0.085 ≈ 1.14e8 req/day ≈ 1319 req/s；若源站单节点处理能力为 1000 req/s，则需增加 2 个源站节点，对应基础设施成本增量 ΔC_infra_source = 2 * ¥3000/月 ≈ ¥6000/月。

## Corrected Claim

回源请求对源站处理延迟的冲击：源站 QPS 增加 ΔQPS_back = R_daily * (1-H_fault) - R_daily * (1-H_steady) = 1.34e9 * 0.085 ≈ 1.14e8 req/day ≈ 1319 req/s；若源站单节点处理能力为 1000 req/s，则需增加 2 个源站节点，对应基础设施成本增量 ΔC_infra_source = 2 * ¥3000/月 ≈ ¥6000/月。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1.34e9 * 0.085 ≈ 1.139e8 req/day，换算为秒级 QPS 约为 1318.5 req/s，与陈述中的 1319 req/s 一致；基于单节点 1000 req/s 的处理能力，需增加 2 个节点（1319/1000 向上取整），成本计算 2 * 3000 = 6000 元/月，逻辑自洽且数值量级合理。
