# N220: 混合策略长尾部分回源流量成本：长尾公有云命中率 H_tail=95%，回源流量 = 18TB * (1-0.95) = 900GB/月，按阿里云回源流量单价 ¥

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64

## Claim

混合策略长尾部分回源流量成本：长尾公有云命中率 H_tail=95%，回源流量 = 18TB * (1-0.95) = 900GB/月，按阿里云回源流量单价 ¥0.15/GB 计算，月回源成本 ≈ ¥135

## Corrected Claim

混合策略长尾部分回源流量成本：长尾公有云命中率 H_tail=95%，回源流量 = 18TB * (1-0.95) = 900GB/月，若按阿里云回源流量单价 ¥0.15/GB 估算，月回源成本约为 ¥135（具体价格需以阿里云官方实时报价为准）。

## Evidence

[质询]阿里云回源流量单价 ¥0.15/GB 属于具体商业定价（经验事实），不同区域、带宽包或协议（HTTP/HTTPS）下价格可能不同，且参考来源未提供该具体数值，存在口径混淆或价格时效性风险。 | 数学计算逻辑自洽（18TB * 5% = 900GB, 900 * 0.15 = 135），但参考来源[1][2]仅讨论CDN回源优化概念及腾讯云案例，未提供阿里云具体回源单价，属于经验事实缺来源直接支持。

## Search Query

阿里云 CDN 回源流量 价格 单价

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_28713947/article/details/165510125&rut=75da1848a78b666a27d03bd9c2b7211d221c94d1062e2f064ba635dc5e7fcf96', 'type': 'ddg', 'title': '跨云日志采集省钱实践：LoongCollector结合CDN回源中转优化流量成本-CSDN博客'}
- {'url': 'https://cloud.tencent.com/developer/article/2721250&rut=f8890bafb8fed8ba51c2c174c5c2d5111c076067dd69d828f820994b6de0da7b', 'type': 'ddg', 'title': '腾讯云国际版云服务代理商：账单异常排查与降本指南 Cdn、Gaap及ai实操-腾讯云开发者社区-腾讯云'}
