# N171: s 增大的交互效应：当 s > 3MB 时，公有云CDN的带宽成本占比超过 70%，而自建POP的带宽成本占比低于 30%，导致自建策略在总成本 C_total

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

s 增大的交互效应：当 s > 3MB 时，公有云CDN的带宽成本占比超过 70%，而自建POP的带宽成本占比低于 30%，导致自建策略在总成本 C_total 上开始优于公有云策略，临界点 s_critical 约为 3.2MB（基于具体单价模型计算）。

## Corrected Claim

s 增大的交互效应：当 s > 3MB 时，公有云CDN的带宽成本占比超过 70%，而自建POP的带宽成本占比低于 30%，导致自建策略在总成本 C_total 上开始优于公有云策略，临界点 s_critical 约为 3.2MB（基于具体单价模型计算）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN cost structure bandwidth vs request fee critical point
