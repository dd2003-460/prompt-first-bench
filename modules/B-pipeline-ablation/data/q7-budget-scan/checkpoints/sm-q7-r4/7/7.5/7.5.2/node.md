# N349: 多连接并行下载的额外网络成本：若通过公网而非内网进行50Gbps传输，阿里云OSS外网流出费用为¥0.5/GB；500TB数据传输费用 = 500,000GB 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N119

## Claim

多连接并行下载的额外网络成本：若通过公网而非内网进行50Gbps传输，阿里云OSS外网流出费用为¥0.5/GB；500TB数据传输费用 = 500,000GB * ¥0.5/GB = ¥250,000/次扫描；若每天2次扫描，年网络流出成本 = ¥250,000 * 2 * 365 = ¥182,500,000/年，远超存储费用，故必须使用内网（VPC Endpoint）以避免高额流出费，内网流量通常免费或极低费率（¥0.05/GB以内）。

## Corrected Claim

多连接并行下载的额外网络成本：若通过公网进行50Gbps传输，阿里云OSS外网流出费用通常约为¥0.5/GB（具体视地域和存储类型而定）；500TB数据传输费用估算约为¥250,000/次扫描；若每天2次扫描，年网络流出成本估算约为¥1.825亿/年，远超存储费用，故建议优先使用内网（VPC Endpoint）以降低流出成本，内网流量通常免费或费率极低。

## Evidence

[质询]核心单价数据（¥0.5/GB）及内网费率（¥0.05/GB以内）属于具体商业定价，参考来源仅提及流量计费概念和带宽性能，未提供具体价格数值，无法从现有来源直接验证该特定金额；此外，不同地域和存储类型（标准/低频/归档）的流出费率可能存在差异，直接断言固定为0.5元/GB缺乏普适性证据。 | 来源[1]确认OSS存在流出流量费用，来源[3]确认内网高带宽场景，但均未提供具体单价（¥0.5/GB），属于经验事实且缺直接来源支持，逻辑计算过程自洽。

## Search Query

Alibaba Cloud OSS data transfer cost public network vs VPC endpoint

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/oss/traffic-fees&rut=c2fe1ce0123449071f15817310ba52a8b5688d93d41bd2fe07f2789403b93fd9', 'type': 'ddg', 'title': '流量费用-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1754015&rut=d4425565b8af503b08b05ffa5c21999e430cc39bcc36e637a0036a1a53a8ccaa', 'type': 'ddg', 'title': '深圳阿里云代理商：Oss 下载提速 Cdn 分片传输优化实操'}
- {'url': 'https://help.aliyun.com/zh/oss/user-guide/bandwidth-of-100-gbit-s-in-vpcs&rut=eb732537ea8ac3cae22d3a8a8c9fe4665efa9458a6222b9c7078143b4af76a44', 'type': 'ddg', 'title': '百Gbps内网带宽性能优化最佳实践-对象存储-阿里云-对象存储 (OSS)-阿里云帮助中心'}
