# N63: C_add_pop 的构成：C_add_pop = C_infra_pop + C_bw_pop + C_ops_pop + C_deployment_pop；

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

C_add_pop 的构成：C_add_pop = C_infra_pop + C_bw_pop + C_ops_pop + C_deployment_pop；其中 C_deployment_pop 为一次性部署成本（¥50k-100k/POP），需年化分摊；C_bw_pop 为带宽租赁费（¥10k-50k/月/POP，取决于带宽大小）。

## Corrected Claim

C_add_pop 的构成通常包括基础设施、带宽、运维及一次性部署成本；具体数值（如 ¥50k-100k/POP 部署费，¥10k-50k/月/POP 带宽费）为经验估算值，缺乏当前参考来源的直接支持，需结合具体供应商报价核实。

## Evidence

[质询]参考来源均为英文 CDN 服务（Edge Network, Costbench）的定价信息，与陈述中具体的人民币（¥）成本构成及数值范围（如 ¥50k-100k/POP 部署费）完全无关，无法提供外部支持；且该陈述属于特定场景下的经验性成本估算，非第一性原理可推导事实。 | 逻辑上成本构成项（基础设施、带宽、运维、部署）自洽，但参考来源 [1][2][3] 均涉及美元计价的国际 CDN 服务，与人民币计价的特定 POP 成本估算主题不匹配，无可用外部证据支持具体数值。

## Search Query

CDN edge node deployment cost monthly bandwidth lease China CNY

## Retrieval Sources

- {'url': 'https://edge.network/cdn/pricing&rut=53b0a4618e9f0c1e14ddff66977bebef9d14583e89208182bf3756777e8c9f28', 'type': 'ddg', 'title': 'CDN Pricing | Edge'}
- {'url': 'https://edge.network/cdn&rut=4f8db4494ff2bf5a9f62f16c9fe3b4819fc9d1bc57357d15bd52abcbad18bbcd', 'type': 'ddg', 'title': 'Edge CDN | Global content delivery, zero egress'}
- {'url': 'https://costbench.com/stats/cdn-edge-pricing-2026/&rut=414668be8e3e21757754955a9d2f95dfaa89ba6fe6a6e57f354af1f07a998ffb', 'type': 'ddg', 'title': 'CDN & Edge Pricing Benchmarks 2026: 11 Products Compared'}
