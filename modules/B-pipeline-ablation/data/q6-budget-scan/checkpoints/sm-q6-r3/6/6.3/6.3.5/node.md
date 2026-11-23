# N129: 纯自建10个POP点在日均请求数R > 50,000,000时的P99合规风险成本：假设P99=300ms，超过T=200ms，违反SLA，预期惩罚成本 = (

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

纯自建10个POP点在日均请求数R > 50,000,000时的P99合规风险成本：假设P99=300ms，超过T=200ms，违反SLA，预期惩罚成本 = (300-200)/100 × 3% × ¥10 / 1000req = ¥0.03/1000req，但需额外投入¥0.05/1000req进行节点扩容或缓存优化以达标，总风险成本¥0.08/1000req

## Corrected Claim

纯自建10个POP点在日均请求数R > 50,000,000时的P99合规风险成本：假设P99=300ms，超过T=200ms，违反SLA，预期惩罚成本 = (300-200)/100 × 3% × ¥10 / 1000req = ¥0.03/1000req，但需额外投入¥0.05/1000req进行节点扩容或缓存优化以达标，总风险成本¥0.08/1000req

## Evidence

先验知识/题面给定，逻辑校验通过：惩罚成本计算 (100/100)*0.03*10 = 0.03 正确，总成本 0.03+0.05=0.08 正确，量纲与数值自洽。

## Search Query

CDN SLA violation penalty cost per 100ms latency
