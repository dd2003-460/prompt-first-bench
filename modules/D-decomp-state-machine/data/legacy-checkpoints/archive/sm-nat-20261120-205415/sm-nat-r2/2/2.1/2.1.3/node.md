# N42: 分母（总请求字节数）Total_Bytes = Q_req * E[S|request]，其中 Q_req=50,000,000 为日请求次数，E[S|requ

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

分母（总请求字节数）Total_Bytes = Q_req * E[S|request]，其中 Q_req=50,000,000 为日请求次数，E[S|request] 为按热度加权的平均对象大小；由于热度与大小负相关，E[S|request] < E[S]=1MB。

## Corrected Claim

分母（总请求字节数）Total_Bytes = Q_req * E[S|request]，其中 Q_req=50,000,000 为日请求次数，E[S|request] 为按热度加权的平均对象大小；由于热度与大小负相关，E[S|request] < E[S]=1MB。

## Evidence

先验知识/题面给定，逻辑校验通过：总字节数等于请求次数乘以平均每次请求的字节数，且热度与大小负相关导致加权平均小于总体平均，符合统计学原理。

## Search Query

weighted average size based on request frequency distribution
