# N105: 在 Pareto(α=1.1) 且截断于 x_max=100MB 的条件下，前 1% 对象（Top 1000）的总字节量占比约为 4.5%，总请求量占比约为 1

- **status**: pending
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

父节点级核验未通过：有冗余（子节点1和3仅参数不同（1% vs 10%），子节点2和4同理，存在明显的结构冗余；且父节点中的'Top 1000'与'1%'、'Top 10,000'与'10%'的对应关系暗示总对象数为100,000，但子节点未明确声明此前提，导致逻辑链条隐含假设过多。）

## Search Query

Pareto distribution alpha 1.1 top 1% objects byte share
