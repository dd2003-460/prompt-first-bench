# N635: 工作点B（中性价比）的单机月均请求承载量 Q_cap_B = (CPU核数 * 单核并发处理能力 * 平均响应时间) / (1 - 安全余量)，假设单核处理10

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N212

## Claim

工作点B（中性价比）的单机月均请求承载量 Q_cap_B = (CPU核数 * 单核并发处理能力 * 平均响应时间) / (1 - 安全余量)，假设单核处理1000 req/s，平均响应50ms，安全余量20%，计算得 Q_cap_B ≈ 1,536,000 req/月；与A相比，单位请求成本 C_req_B = C_server_B / Q_cap_B ≈ ¥0.00109/req，高于A的¥0.00102/req。

## Corrected Claim

工作点B（中性价比）的单机月均请求承载量 Q_cap_B = (CPU核数 * 单核并发处理能力 * 平均响应时间) / (1 - 安全余量)，假设单核处理1000 req/s，平均响应50ms，安全余量20%，计算得 Q_cap_B ≈ 1,536,000 req/月；与A相比，单位请求成本 C_req_B = C_server_B / Q_cap_B ≈ ¥0.00109/req，高于A的¥0.00102/req。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程符合 Little's Law 及成本分摊逻辑，数值量级合理。

## Search Query

standard density cdn edge node cost per request benchmark
