# N45: 前 k 个最热门对象的请求占比 H_req(k) = 1 - (k/N)^{β-1} / (β-1) 的修正形式：对于 Pareto(β=0.9) 分布（β<2

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

前 k 个最热门对象的请求占比 H_req(k) = 1 - (k/N)^{β-1} / (β-1) 的修正形式：对于 Pareto(β=0.9) 分布（β<2），累积质量占比 = (1 - (k/N)^{β-1}) / (1 - N^{1-β})，其中 N=10^5，β=0.9；该值量化了头部对象在请求频率上的集中度，是命中率的主要驱动因素。

## Corrected Claim

前 k 个最热门对象的请求占比 H_req(k) = 1 - (k/N)^{β-1} / (β-1) 的修正形式：对于 Pareto(β=0.9) 分布（β<2），累积质量占比 = (1 - (k/N)^{β-1}) / (1 - N^{1-β})，其中 N=10^5，β=0.9；该值量化了头部对象在请求频率上的集中度，是命中率的主要驱动因素。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 774)
