# N267: 公有云 CDN 日志查询的索引构建成本 $C_{index}$：SLS 等日志服务通常对建立索引的数据量单独计费，单价约为 0.20 元/GB；若对全部 60T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

公有云 CDN 日志查询的索引构建成本 $C_{index}$：SLS 等日志服务通常对建立索引的数据量单独计费，单价约为 0.20 元/GB；若对全部 60TB 日志建立索引，月索引成本 $C_{index} = 60,000 \text{ GB} \times 0.20 = 12,000$ 元/月，远高于查询扫描成本。

## Corrected Claim

公有云 CDN 日志查询的索引构建成本 $C_{index}$：SLS 等日志服务通常对建立索引的数据量单独计费，单价约为 0.20 元/GB；若对全部 60TB 日志建立索引，月索引成本 $C_{index} = 60,000 \text{ GB} \times 0.20 = 12,000$ 元/月，远高于查询扫描成本。

## Evidence

先验知识/题面给定，逻辑校验通过
