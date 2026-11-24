# N235: 工作点1（激进/高利用率）：预留带宽 B_peak_pub = 79.2 Mbps (buffer=0)，对应阿里云CDN月成本 ≈ 4,752 元 (79.2

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

工作点1（激进/高利用率）：预留带宽 B_peak_pub = 79.2 Mbps (buffer=0)，对应阿里云CDN月成本 ≈ 4,752 元 (79.2 × 0.06 × 1000? 注：阿里云通常按GB计费，若按峰值带宽计费假设0.06元/Mbps/月则为475.2元/月，此处采用更常见的按量/包年混合估算，假设峰值带宽包月成本约为 0.06元/Mbps/天 * 30 = 1.8元/Mbps/月，则 79.2 * 1.8 ≈ 142.56元/月? 需澄清计费单位。通常CDN按流量GB计费。若按N120的0.18元/GB估算，峰值带宽对应的月流量上限成本需转换。此处修正为：基于N122的归一化逻辑，若采用峰值带宽预留模式，假设单价为0.5元/Mbps/月(行业典型)，则79.2Mbps月成本≈39.6元，此数值偏低，可能不适用。重新校准：公有云CDN通常不卖'峰值带宽预留'，而是按流量或95th百分位计费。若按95th百分位计费，假设95th=0.8*Peak，则计费带宽≈63.4Mbps。若单价为2元/Mbps/月(典型95计费)，月成本≈126.8元。此值远低于N122的10800元，说明N122是按纯流量包计费。为保持一致，本节点假设采用'流量包+超额'模式，预留带宽仅为容量上限，成本仍由N122决定，但此节点旨在分析'若改为按峰值带宽预留'的边际成本差异。假设按峰值带宽计费，单价5元/Mbps/月，B_peak=79.2，月成本=396元。

## Corrected Claim

工作点1（激进/高利用率）：预留带宽 B_peak_pub = 79.2 Mbps (buffer=0)。若采用阿里云CDN按峰值带宽计费模式，具体月成本需依据阿里云官方实时单价计算，此处无法给出确切数值，但通常远高于按流量计费的边际成本。

## Evidence

[质询]该陈述内部逻辑混乱，包含大量自我否定的假设（如“此数值偏低，可能不适用”、“重新校准”），最终得出的“396元/月”基于一个未经验证的假设单价（5元/Mbps/月），且与阿里云CDN实际计费模式（通常按流量或95th百分位，而非简单的峰值带宽包月）存在偏差，缺乏可靠来源支持该具体数值。 | 来源[2]确认阿里云CDN支持按峰值带宽计费，但未提供具体单价；陈述中的成本计算基于假设单价，属于经验事实且缺乏直接来源支持，逻辑上虽自洽但数值不可靠。

## Search Query

Alibaba Cloud CDN pricing 95th percentile bandwidth cost per Mbps

## Retrieval Sources

- {'url': 'https://www.alibabacloud.com/en/product/content-delivery-network/pricing?_p_lc=1&rut=ece8122a9f0c982a83e62096f403e46fef8fb30d9af2397f37f5ff3aec2fa0ad', 'type': 'ddg', 'title': 'Alibaba Cloud CDN'}
- {'url': 'https://help.aliyun.com/en/cdn/product-overview/billing-rules-of-basic-services&rut=3c61bc15e6750c575e1f9aa4d4336035b83fb2b422168878f4dd7d1620c696dd', 'type': 'ddg', 'title': 'Billing of basic services-CDN (CDN)-阿里云帮助中心'}
- {'url': 'https://support.huaweicloud.com/intl/en-us/price-cdn/cdn_01_0160.html&rut=da5ef64f6c3c8c26b08cf7584792c349eefff2309622a1f6a0029977d23eafe8', 'type': 'ddg', 'title': 'Billing by 95th Percentile Bandwidth - 华为云'}
