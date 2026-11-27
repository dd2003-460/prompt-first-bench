# N105: 在 Pareto(α=1.1) 且截断于 x_max=100MB 的条件下，前 1% 对象（Top 1000）的总字节量占比约为 4.5%，总请求量占比约为 1

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 Pareto(α=1.1) 且截断于 x_max=100MB 的条件下，前 1% 对象（Top 1000）的总字节量占比约为 4.5%，总请求量占比约为 1.1%；前 10% 对象（Top 10,000）的总字节量占比约为 14.3%，总请求量占比约为 10.0%。

## Corrected Claim

在 Pareto(α=1.1) 且截断于 x_max=100MB 的条件下，前 1% 对象（Top 1000）的总字节量占比约为 4.5%，总请求量占比约为 1.1%；前 10% 对象（Top 10,000）的总字节量占比约为 14.3%，总请求量占比约为 10.0%。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Pareto distribution alpha 1.1 top 1% objects byte share
