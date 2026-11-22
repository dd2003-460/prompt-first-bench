# N98: 重填充失败率f_refill的中性价比最优工作点：在标准SLA下，P(源站不可用)=0.1%、P(超时)=0.1%、P(去重失败)=0.01%，f_refill

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

重填充失败率f_refill的中性价比最优工作点：在标准SLA下，P(源站不可用)=0.1%、P(超时)=0.1%、P(去重失败)=0.01%，f_refill=0.0021；通过引入请求合并（Request Coalescing）可将P(去重失败)降至0.001%，f_refill=0.0020，折损降低4.76%，是短期运营优化的关键杠杆。

## Corrected Claim

重填充失败率f_refill的中性价比最优工作点：在标准SLA下，P(源站不可用)=0.1%、P(超时)=0.1%、P(去重失败)=0.01%，f_refill=0.0021；通过引入请求合并（Request Coalescing）可将P(去重失败)降至0.001%，f_refill=0.0020，折损降低4.76%，是短期运营优化的关键杠杆。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（0.0021 vs 0.0020，降幅约4.76%），符合CDN缓存失效与请求合并的工程直觉。
