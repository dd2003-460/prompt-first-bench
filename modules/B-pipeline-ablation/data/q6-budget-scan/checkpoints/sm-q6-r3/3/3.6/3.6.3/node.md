# N115: 自建边缘节点下载带宽单价 p_download_self 的具体数值：自建节点通常通过BGP多线接入，带宽成本约为 ¥0.05-0.15/Mbps/月，需转换为

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N31

## Claim

自建边缘节点下载带宽单价 p_download_self 的具体数值：自建节点通常通过BGP多线接入，带宽成本约为 ¥0.05-0.15/Mbps/月，需转换为每GB价格：假设月峰值带宽 B_peak，则 p_download_self ≈ (B_peak * p_mbps) / V_month，典型值约为 ¥0.02-0.05/GB [时效待核]

## Corrected Claim

自建边缘节点下载带宽单价 p_download_self 的具体数值：自建节点通常通过BGP多线接入，带宽成本约为 ¥0.05-0.15/Mbps/月，需转换为每GB价格：假设月峰值带宽 B_peak，则 p_download_self ≈ (B_peak * p_mbps) / V_month，典型值约为 ¥0.02-0.05/GB [时效待核，需结合最新市场行情验证]

## Evidence

[质询]该陈述包含具体的经验性价格参数（¥0.05-0.15/Mbps/月 和 ¥0.02-0.05/GB），属于市场波动较大的经验事实，无法从第一性原理推导，且参考来源未提供直接数据支持。 | 经验事实，逻辑自洽但缺来源支持（来源[1]仅涉及PCDN概念，未提供具体带宽单价数据）

## Search Query

China BGP bandwidth cost per Mbps self-hosted edge node 2024

## Retrieval Sources

- {'url': 'https://www.toutiao.com/article/7626626090300719658/&rut=2b3366b2011a8554341bc0a5bdc2bd38b3cae58a5a3a6635690e4c2abddfab6a', 'type': 'ddg', 'title': '手把手教你搭建pcdn节点，把上行带宽变成零花钱 - 今日头条'}
