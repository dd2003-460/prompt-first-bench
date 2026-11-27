# N23: 刚查到的/需外部查证：Pareto(α=1.1) 下 128GB 缓存对 10 万对象的实际覆盖率 C/M 及稳态命中率经验值，需检索 CDN 厂商（如 Clo

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N5

## Claim

刚查到的/需外部查证：Pareto(α=1.1) 下 128GB 缓存对 10 万对象的实际覆盖率 C/M 及稳态命中率经验值，需检索 CDN 厂商（如 Cloudflare, Akamai）公开技术报告或学术论文（如 'Cache Hit Ratio Analysis for Pareto Workloads'）获取一手机制参数。

## Corrected Claim

Pareto(α=1.1) 下 128GB 缓存对 10 万对象的实际覆盖率 C/M 及稳态命中率需通过具体负载模拟或厂商报告获取，当前缺乏直接数据支持，仅能定性推断命中率较高。

## Evidence

[质询]参考来源与事实主题完全无关（来源讨论的是LLM显存优化，而非CDN缓存命中率），导致该经验事实缺乏任何外部证据支持，无法验证具体数值。 | 参考来源[1]与Pareto分布下的CDN缓存命中率无关，属于无关来源；该事实为经验性工程参数，逻辑上自洽（Pareto分布下缓存命中率通常较高），但缺乏来源支持，依据经验事实排除条款降级。

## Search Query

CDN cache hit ratio Pareto distribution alpha 1.1 128GB memory

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2066264430082519371&rut=a8ff4649555d51e32bcc1a1cc0402a7daec790950bd0925a6703eae28a94faee', 'type': 'ddg', 'title': '实测需要 6.6GB 显存的 MoE 大模型，在 1.2GB 显存上正常跑'}
