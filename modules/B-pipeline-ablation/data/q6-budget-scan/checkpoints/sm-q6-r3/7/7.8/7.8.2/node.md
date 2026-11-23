# N351: 最小起租带宽门槛 $B_{min}$ 的具体数值：阿里云/腾讯云等主流国内公有云 CDN 的 95th 带宽计费通常有最小计费单位（如 1Gbps 或 10Gb

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130

## Claim

最小起租带宽门槛 $B_{min}$ 的具体数值：阿里云/腾讯云等主流国内公有云 CDN 的 95th 带宽计费通常有最小计费单位（如 1Gbps 或 10Gbps），低于此值按此值计费，需查询具体厂商最新合同条款确认 $B_{min}$ 值。

## Corrected Claim

阿里云/腾讯云等主流国内公有云 CDN 的 95th 带宽计费通常设有最小计费单位（B_min），低于此值按此值计费，具体数值需查询各厂商最新合同条款确认，常见量级可能在 Gbps 级别，但具体值（如 1Gbps 或 10Gbps）因厂商和合同而异。

## Evidence

[质询]陈述中给出的具体数值示例（1Gbps 或 10Gbps）缺乏来源支持，且不同厂商、不同计费模式（如按带宽峰值 vs 95th 峰值）的最小计费单位可能不同，直接断言具体数值存在经验事实错误风险。 | 参考来源[1]和[2]主要讨论云服务器（ECS/轻量应用服务器）的租用价格和带宽配置，未涉及 CDN 95th 带宽计费的最小起租门槛（B_min）具体数值，属于主题不匹配或证据缺失；该事实为经验性商业条款，逻辑上自洽（存在最小计费单位是合理的），但缺乏直接来源支持具体数值，故降级。

## Search Query

阿里云 CDN 95th 带宽计费 最小起租带宽 门槛

## Retrieval Sources

- {'url': 'https://k.sina.cn/article_7879848900_1d5acf3c401902ufac.html&rut=e564655c979e8a32af3198f53f8df046259e6ad9a9996d24e771b2a34d75104a', 'type': 'ddg', 'title': '2025云服务器租用价格全解析:主流服务商与配置对比|带宽|阿里云|腾讯云|华为云|双11_新浪新闻'}
- {'url': 'https://zhuanlan.zhihu.com/p/1990890505261843933&rut=2d3eeb364d07a5db391bf75a13a45e0e6f2e4e8d9aa1d654a680d703b04bf26c', 'type': 'ddg', 'title': '阿里云服务器租用价格2026年最新：CPU/内存/带宽配置清单'}
