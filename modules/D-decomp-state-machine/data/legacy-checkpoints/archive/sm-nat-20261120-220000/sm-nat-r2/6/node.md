# N15: Pareto(β=0.9)热度分布下，前1%的热门对象承载了约90%的请求流量（基于Zipf定律近似 log10(1/0.01)/log10(e^β) 或 1/

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Pareto(β=0.9)热度分布下，前1%的热门对象承载了约90%的请求流量（基于Zipf定律近似 log10(1/0.01)/log10(e^β) 或 1/0.9 * log(100)），日均请求5000万次意味着热门对象集（约1000个）需处理4500万次/天，对LRU缓存的稳定性构成主要压力。

## Corrected Claim

Pareto(β=0.9)热度分布下，前1%的热门对象承载了约98%的请求流量（基于Zipf定律近似 1-(1/100)^0.9），日均请求5000万次意味着热门对象集（约1000个）需处理约4900万次/天，对LRU缓存的稳定性构成主要压力。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 658)

## Retrieval Sources

- {'url': 'https://shifter.io/cn/atlas/guides/proxy-latency-explained&rut=7a6a6a9de55fc30ef69a71d745ec79a1496fb8284f9123a7749d2bca8ce7bd50', 'type': 'ddg', 'title': '代理延迟：如何读懂 p50 到 p99 图表'}
- {'url': 'https://www.csdn.net/detail/weixin_34221654/165497&rut=7cfcfd6b649eb01dc2714626b245ef9d61e5952b0934442cd5ddacd90a7da9fd', 'type': 'ddg', 'title': '压测参数决定结论：benchmark三层参数与调参实践 - CSDN'}
