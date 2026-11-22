# N522: 消费级多卡方案 (2x RTX 4090) 的 TCO 公式：TCO_cons(T) = CapEx_4090_2x + (Power_4090_2x * T 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N160

## Claim

消费级多卡方案 (2x RTX 4090) 的 TCO 公式：TCO_cons(T) = CapEx_4090_2x + (Power_4090_2x * T / 8760)，其中 Power_4090_2x 约为 550W * 2 = 1100W (峰值) 或 300W * 2 = 600W (平均)，CapEx_4090_2x 约为 $2,000 * 2 = $4,000 [待核验：RTX 4090 当前市场价及功耗曲线]，该方案在 T < 1.5 年时 TCO 显著低于数据中心方案，但单位 Token 成本在高负载下更高

## Corrected Claim

消费级多卡方案 (2x RTX 4090) 的 TCO 估算：CapEx 约为 $4,000（基于 $2,000/卡的市场价），平均功耗约为 600W（基于 300W/卡的平均负载假设）。在短期（T < 1.5 年）内，其总拥有成本通常低于数据中心方案，但需注意高负载下的能效比及单位 Token 成本需结合具体吞吐量评估。

## Evidence

[质询]RTX 4090 的峰值功耗通常标称为 450W（部分超频或特定负载下可能略高，但 550W 并非标准峰值），且 TCO 公式中直接相加 CapEx 和电费忽略了资金的时间价值（折现率），导致在 T < 1.5 年时 TCO 对比数据可能失真；此外，'单位 Token 成本在高负载下更高'这一结论缺乏具体的吞吐量数据支持，仅凭功耗无法直接推导。 | 来源 [1] 仅提及 8 卡 4090 集群的效率，未提供单卡具体功耗数值、市场价格或 TCO 对比数据，属于间接相关但无直接支持；RTX 4090 功耗和价格属于经验事实，逻辑自洽但缺来源直接支持。

## Search Query

RTX 4090 TCO total cost of ownership electricity cost inference workload average power draw dual card

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2020458980598633680&rut=9d4124efa2f26ccd217432c035c10783059c0394a31b8b5f839fb3d61e0f9e73', 'type': 'ddg', 'title': '8卡4090集群实测：多卡并行效率能到多少？ - 知乎'}
