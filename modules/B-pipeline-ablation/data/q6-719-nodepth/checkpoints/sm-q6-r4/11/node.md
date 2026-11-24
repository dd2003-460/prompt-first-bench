# N141: 请求频次与对象大小的耦合效应：虽然日均下载2TB，但若平均对象大小 s_avg 较小（如1MB），则请求数 R = 2TB/1MB = 2M次/天；若 s_av

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

请求频次与对象大小的耦合效应：虽然日均下载2TB，但若平均对象大小 s_avg 较小（如1MB），则请求数 R = 2TB/1MB = 2M次/天；若 s_avg 较大（如10MB），则 R = 200k次/天。公有云CDN通常按“请求数”和“流量”双重计费，小对象高频率场景下，请求数费用占比显著上升（可达总成本的30-50%），而大对象低频率场景下流量费用占比主导。需根据实际 s_avg 分布重新加权 N67 的请求成本。

## Corrected Claim

请求频次与对象大小的耦合效应：虽然日均下载2TB，但若平均对象大小 s_avg 较小（如1MB），则请求数 R = 2TB/1MB = 2M次/天；若 s_avg 较大（如10MB），则 R = 200k次/天。公有云CDN/对象存储通常按“请求数”和“流量”双重计费，小对象高频率场景下，请求数费用占比会显著上升，而大对象低频率场景下流量费用占比主导。需根据实际 s_avg 分布重新加权 N67 的请求成本。

## Evidence

[质询]陈述中关于“小对象高频率场景下，请求数费用占比可达总成本的30-50%”属于具体的经验性数值断言。虽然逻辑上小对象确实会导致请求数激增从而增加请求费用占比，但具体的百分比范围（30-50%）高度依赖于具体的云厂商定价策略、存储量大小以及具体的对象大小分布，并非普适的物理或数学常数。参考来源仅提供了计费维度的存在性（请求数、流量），并未提供该特定场景下的成本占比统计数据，因此该具体数值缺乏直接来源支持。 | 逻辑推导成立（R=TotalTraffic/AvgSize），且来源[1]确认了对象存储成本包含请求次数和流量两个维度，支持了“双重计费”和“需重新加权”的定性结论；但来源未提供“30-50%”这一具体经验数值，故依据经验事实排除条款降级。

## Retrieval Sources

- {'url': 'https://cloud.tencent.com/developer/article/2777914&rut=085b912fb02f4251af3a61ddf33f7805a0da837d22d68f61f98e70deb0ee4822', 'type': 'ddg', 'title': 'Cos标准存储请求包与存储包：对象存储成本结构的技术视角 ——请求次数、存储量和公网流出流量三者如何相互影响'}
- {'url': 'https://help.aliyun.com/zh/oss/user-guide/metrics&rut=892378daaba6e1b1b7d7a8ae0bbadaaf38e2d25993e49fe05d1f256a4934ac28', 'type': 'ddg', 'title': 'Oss监控指标参考-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/userguide/metrics-dimensions.html&rut=5773fba6ff864f4726f48e94bea9f6a3fe36f5d63bf11b90401a353a24686672', 'type': 'ddg', 'title': '指标与维度 - Amazon Simple Storage Service'}
