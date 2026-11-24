# N261: 对象访问请求量服从Zipf分布，参数α=1.0（互联网媒体常见值），Top K对象的累计访问比例 P_topK = 1 - (1/K)^α，当K=1000时P_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N96

## Claim

对象访问请求量服从Zipf分布，参数α=1.0（互联网媒体常见值），Top K对象的累计访问比例 P_topK = 1 - (1/K)^α，当K=1000时P_topK≈0.999，当K=100时P_topK≈0.99，需根据平台实际日志校验α值

## Corrected Claim

对象访问请求量服从Zipf分布，参数α=1.0（互联网媒体常见值），Top K对象的累计访问比例 P_topK = 1 - (1/K)^α，当K=1000时P_topK≈0.999，当K=100时P_topK≈0.99，需根据平台实际日志校验α值

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P_topK = 1 - (1/K)^α 在 α=1.0 时，K=1000 对应 0.999，K=100 对应 0.99，数值计算准确且符合 Zipf 分布累积概率的数学性质。

## Search Query

Zipf distribution alpha parameter web traffic media platform
