# N69: Cloudflare 2023 技术报告指出，在 Pareto(α≈1.1) 工作负载下，128GB 边缘节点对 10 万对象的稳态字节命中率中位数为 85-9

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

Cloudflare 2023 技术报告指出，在 Pareto(α≈1.1) 工作负载下，128GB 边缘节点对 10 万对象的稳态字节命中率中位数为 85-92%，95 分位数为 95%，需检索该报告获取具体分布参数 [search: 一手数据]

## Corrected Claim

在Pareto(α≈1.1)工作负载下，128GB边缘节点对10万对象的稳态字节命中率通常较高（具体数值需查阅Cloudflare 2023技术报告原文确认，常见范围可能在85%-95%之间）。

## Evidence

[质询]该陈述包含具体的经验性数据（命中率中位数85-92%、95分位数95%）和特定的报告引用，属于经验事实。由于检索失败，无法验证Cloudflare 2023技术报告是否真实存在该具体数据，且Pareto(α≈1.1)下的具体命中率分布高度依赖缓存策略、对象大小分布等未提及的细节，存在数据捏造或张冠李戴的风险。 | 经验事实，逻辑自洽（高α值Pareto分布确实会导致高命中率，量级合理），但缺来源支持（检索无可用来源）。

## Search Query

Cloudflare technical report 2023 cache hit ratio Pareto workload 128GB edge node
