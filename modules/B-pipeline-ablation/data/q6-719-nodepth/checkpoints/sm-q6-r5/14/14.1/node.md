# N406: 运营商专线（Leased Line）10Gbps 月租价格区间为 ¥8,000-15,000，而同等带宽的公网 BGP 流量成本约为 ¥30,000-50,00

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N135

## Claim

运营商专线（Leased Line）10Gbps 月租价格区间为 ¥8,000-15,000，而同等带宽的公网 BGP 流量成本约为 ¥30,000-50,000（按 0.2-0.3 CNY/GB 估算月 12PB 流量），专线成本仅为公网的 1/3 至 1/5，差异主要源于带宽独占与 QoS 保障。

## Corrected Claim

运营商专线（Leased Line）10Gbps 月租价格因地区和供应商差异较大，通常高于¥8,000-15,000；同等带宽的公网 BGP 流量成本需根据实际流量和定价模型估算，专线成本通常低于公网流量成本，差异源于带宽独占与 QoS 保障。

## Evidence

[质询]数值量级与来源严重不符：参考来源[1]指出10Gbps专线月费通常在£200-£600（100M-1G）基础上上升，但未给出具体10G数值，且通常10G专线价格远高于¥8,000-15,000（约$1,000-$2,000+），该陈述中的低价区间可能仅适用于特定促销或极低带宽，且公网BGP流量成本估算（0.2-0.3 CNY/GB）缺乏来源支持，属于经验事实且数值存疑。 | 来源[1]主题相关但仅覆盖100M-1G价格区间，未直接支持10Gbps的¥8,000-15,000区间，且公网流量成本无来源支持，属经验事实缺直接证据。

## Search Query

China telecom leased line 10Gbps monthly price vs BGP internet traffic cost

## Retrieval Sources

- {'url': 'https://www.purple.ai/zh-cn/blogs/leased-line-cost&rut=4a5f4677ffde8d6b366b14666793edaff475b326a3bdbd14a4ab36e90b8da083', 'type': 'ddg', 'title': '企业专线成本：100Mb、1Gb和10Gb价格指南 | Purple'}
