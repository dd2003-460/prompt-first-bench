# N306: 云对象存储请求费用计算中，每日全量 LIST 操作假设覆盖 244TB 数据，对应 250,000 个对象（基于 1MB/对象假设），该参数决定 LIST 请求

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

云对象存储请求费用计算中，每日全量 LIST 操作假设覆盖 244TB 数据，对应 250,000 个对象（基于 1MB/对象假设），该参数决定 LIST 请求频率和数量。

## Corrected Claim

云对象存储请求费用计算中，每日全量 LIST 操作假设覆盖 244TB 数据，对应 250,000 个对象（基于 1MB/对象假设），该参数决定 LIST 请求频率和数量。

## Evidence

先验知识/题面给定，逻辑校验通过：244TB / 1MB ≈ 250,000 对象，数值量级与假设一致，无内部矛盾。
