# N250: H100 SXM 3年后的残值率区间及来源：参考 IDC 2024 年 GPU 折旧报告或 NVIDIA 官方二手回收政策，确定 3 年线性折旧下的 Resal

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N94

## Claim

H100 SXM 3年后的残值率区间及来源：参考 IDC 2024 年 GPU 折旧报告或 NVIDIA 官方二手回收政策，确定 3 年线性折旧下的 Resale_Rate_H100 具体百分比范围（例如 30%-50%），并标注数据时效性 [时效待核]

## Corrected Claim

H100 SXM 24个月后的残值率参考 ServerBuyback 2026年6月数据（具体数值需查阅原文），3年残值率暂无直接权威来源支持，建议基于2年数据结合行业平均折旧率进行估算，并标注为估算值。

## Evidence

[质询]来源[1]明确提供的是24个月（2年）的价值保留率，而非3年；且来源[1]为第三方回收商数据，并非节点声称的IDC或NVIDIA官方数据，存在口径（时间跨度）和来源权威性不匹配的问题。 | 来源[1]提供了H100的二手市场价值指数，但仅覆盖24个月数据，未直接提供3年残值率；来源[2]和[3]与3年残值率无直接关联。逻辑上3年残值低于2年符合折旧规律，但具体数值缺乏直接来源支持。

## Search Query

NVIDIA H100 SXM 3 year residual value depreciation rate 2024 2025 IDC report

## Retrieval Sources

- {'url': 'https://serverbuyback.com/resources/gpu-resale-value-index/&rut=969d8e6efbb0c8d5a188d341a92c99cc48864f59e3a5f01459c4e618c276bc90', 'type': 'ddg', 'title': 'GPU Resale Value Index (H100, A100, L40S) | ServerBuyback'}
- {'url': 'https://news.smm.cn/news/104146647&rut=7385c4ae4872c3a5556758d169ea547cf3a3455b9f2c7ff4a62dedf876e56d18', 'type': 'ddg', 'title': '【SMM分析】GPU换代，不等于被淘汰__上海有色网'}
- {'url': 'https://inferencex.semianalysis.com/zh/chips/h100&rut=4ec314abbecd13a86b61ce94516ad3419a19b9422828da76d389dd49e51cc1a9', 'type': 'ddg', 'title': 'NVIDIA H100 SXM 规格、价格与功耗 | InferenceX'}
