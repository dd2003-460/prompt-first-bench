# N408: BGP多线接入溢价系数 Multiplier_BGP = 1.3 ± 0.1，即实际带宽成本 = 单线价格 × Multiplier_BGP，若10个POP均需

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N142

## Claim

BGP多线接入溢价系数 Multiplier_BGP = 1.3 ± 0.1，即实际带宽成本 = 单线价格 × Multiplier_BGP，若10个POP均需BGP多线，总带宽成本上升至 ¥160,000 × 1.3 = ¥208,000/月，进一步拉大与公有云的成本差距

## Corrected Claim

BGP多线接入通常存在成本溢价，具体系数需依据运营商报价确定；若假设溢价系数为1.3，则总带宽成本约为 ¥208,000/月。

## Evidence

[质询]该陈述包含具体的商业定价参数（溢价系数1.3±0.1）和特定场景下的成本计算（¥160,000基数），属于经验事实。参考来源仅涉及BGP协议的技术原理和配置，完全未涉及带宽成本、溢价系数或具体价格数据，无法提供外部支持。 | 逻辑上乘法运算自洽（160,000 * 1.3 = 208,000），但作为经验事实（具体价格系数），参考来源[1][2][3]均为BGP技术文档，与成本估算无关，缺乏直接来源支持，故降级。

## Search Query

BGP multi-line internet access premium ratio China IDC 2024

## Retrieval Sources

- {'url': 'https://blog.csdn.net/Lxyand1/article/details/144424707&rut=6644ebc064f1d20b05289f4b07d62a9f33284de487e81783426c54d0a14bde85', 'type': 'ddg', 'title': 'BGP 全网最详解（理论及配置）_bgp详解-CSDN博客'}
- {'url': 'https://www.cisco.com/c/zh_cn/support/docs/ip/border-gateway-protocol-bgp/217964-configure-sample-for-bgp-with-two-differ.html&rut=160bc785a83d9dc6016d61a4022a298c11780d3464561d06e9ab9cf171837977', 'type': 'ddg', 'title': '配置 BGP 使用两个不同的服务提供商 - Cisco'}
- {'url': 'https://www.h3c.com/cn/d_202511/2693821_30005_0.htm&rut=ee599589dfabcb634cd496183e7780a62d6bf2e2eda7991058cf3a4954c4ee9e', 'type': 'ddg', 'title': '06-bgp基础配置-新华三集团-h3c'}
