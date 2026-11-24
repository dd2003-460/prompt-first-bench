# N237: 工作点3（保守/高冗余）：预留带宽 B_peak_pub = 118.8 Mbps (buffer=0.5)，若采用95th百分位计费，计费带宽≈95.04 M

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

工作点3（保守/高冗余）：预留带宽 B_peak_pub = 118.8 Mbps (buffer=0.5)，若采用95th百分位计费，计费带宽≈95.04 Mbps。假设单价 2.0 元/Mbps/月，月带宽成本 ≈ 190.08 元。相比工作点2，增加23%的冗余带宽仅增加25%的成本，边际收益递减，适用于对P99延迟极度敏感且无法容忍回源拥塞的场景。

## Corrected Claim

工作点3（保守/高冗余）：预留带宽 B_peak_pub = 118.8 Mbps (buffer=0.5)，若采用95th百分位计费，计费带宽≈95.04 Mbps。假设单价 2.0 元/Mbps/月，月带宽成本 ≈ 190.08 元。相比工作点2，增加23%的冗余带宽仅增加25%的成本，边际收益递减，适用于对P99延迟极度敏感且无法容忍回源拥塞的场景。（注：具体数值基于假设参数，需结合实际合同单价验证）

## Evidence

[质询]该陈述包含具体的经验性参数（如单价2.0元/Mbps/月、具体的带宽数值118.8 Mbps、成本190.08元），这些属于市场/工程经验事实，无法从第一性原理推导，且参考来源未提供这些具体数值的支持。 | 逻辑校验通过（118.8 * 0.8 = 95.04, 95.04 * 2 = 190.08，计算无误），但参考来源[1]仅讨论CDN架构优化的通用权衡，未涉及具体计费模型或数值，属于经验事实且缺来源直接支持。

## Search Query

CDN bandwidth buffer factor cost trade-off P99 latency

## Retrieval Sources

- {'url': 'https://arxiv.org/html/2412.09474v1&rut=c882273af59b7e57f1fe7a86d5cfc0a7ec5a6e5b78422354158b8772ee7b1a2a', 'type': 'ddg', 'title': 'Optimizing CDN Architectures: Multi-Metric Algorithmic Breakthroughs ...'}
