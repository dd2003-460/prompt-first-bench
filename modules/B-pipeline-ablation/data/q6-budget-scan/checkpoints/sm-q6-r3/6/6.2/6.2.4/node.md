# N124: 混合策略在日均请求数R ∈ [10,000,000, 50,000,000]时的P99合规风险成本：假设核心区域P99=120ms，长尾区域P99=250ms，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

混合策略在日均请求数R ∈ [10,000,000, 50,000,000]时的P99合规风险成本：假设核心区域P99=120ms，长尾区域P99=250ms，加权平均P99=172ms，低于T=200ms，安全边际28ms，预期惩罚成本接近于0，但需监控长尾区域波动，预留¥0.01/1000req作为风险缓冲

## Corrected Claim

混合策略在日均请求数R ∈ [10,000,000, 50,000,000]时的P99合规风险成本：假设核心区域P99=120ms，长尾区域P99=250ms，加权平均P99=172ms，低于T=200ms，安全边际28ms，预期惩罚成本接近于0，但需监控长尾区域波动，预留¥0.01/1000req作为风险缓冲

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算正确（假设权重合理），172ms < 200ms 符合安全边际描述，风险缓冲设定符合工程直觉。

## Search Query

Hybrid CDN P99 latency weighted average calculation
