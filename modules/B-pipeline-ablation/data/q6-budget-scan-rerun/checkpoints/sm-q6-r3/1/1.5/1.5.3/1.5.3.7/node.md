# N156: 二线城市用户占比的量化修正：基于CNNIC 2024报告，二线城市网民占比约为28-32%，但图片/短视频平台用户画像显示二线城市活跃用户占比可达35-40%。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N38, N39, N40

## Claim

二线城市用户占比的量化修正：基于CNNIC 2024报告，二线城市网民占比约为28-32%，但图片/短视频平台用户画像显示二线城市活跃用户占比可达35-40%。采用35%作为基准值，标准差±3%，即DAU贡献区间为171.5万-178.5万

## Corrected Claim

基于行业经验估算，二线城市网民占比约为28-32%，而图片/短视频平台在该层级的活跃用户占比可能更高（约35-40%）。若采用35%作为基准值，标准差±3%，则DAU贡献区间约为171.5万-178.5万（注：此数值基于假设的总DAU基数推算，具体需结合平台实际总DAU验证）。

## Evidence

[质询]CNNIC报告通常按地域（城市/农村）或省份统计，极少直接提供“二线城市”这一特定行政/经济层级的网民占比数据；且“图片/短视频平台用户画像”的具体数据（35-40%）缺乏公开权威来源支持，属于经验性假设而非可验证的统计事实。 | 来源[1][3]为CNNIC 2024报告，仅确认了总体网民规模，未提供二线城市具体占比数据；来源[2]为第55次报告介绍，亦无相关细分数据。该陈述中的具体数值（28-32%, 35-40%）属于经验事实，逻辑自洽但缺乏来源直接支持。

## Search Query

CNNIC 2024 report tier 2 city user percentage short video platform

## Retrieval Sources

- {'url': 'http://www3.cnnic.cn/n4/2024/0829/c88-11065.html&rut=809f1618b9504ec0b7edb9f55a39da9afc6a6cf7167b79754fd9c6da0da89359', 'type': 'ddg', 'title': '第54次《中国互联网络发展状况统计报告》--互联网发展研究'}
- {'url': 'https://www.cnnic.com.cn/IDR/ReportDownloads/202505/P020250514564119130448.pdf&rut=bdc3f13d5f1bc6dda5333b427de67a0483577e59d83fc87b912fea956517da6b', 'type': 'ddg', 'title': "PDF The 55th Statistical Report on China's Internet Development"}
- {'url': 'http://www3.cnnic.cn/NMediaFile/2024/0911/MAIN1726017626560DHICKVFSM6.pdf&rut=5c808d6973f91c99f8c7d6b7decab7e277e3f7b55a1aefc06da7e8a522732608', 'type': 'ddg', 'title': 'PDF <4d6963726f736f667420576f7264202d20a1bec9e8bcc6b8e5a1bf3534b4cebba5c1aa ...'}
