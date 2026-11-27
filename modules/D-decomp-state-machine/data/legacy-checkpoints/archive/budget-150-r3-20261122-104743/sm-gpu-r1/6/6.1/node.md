# N30: 价格波动敏感性：GPU价格在过去6个月内波动范围为±15%（如RTX 4090从$1600涨至$1800），数据中心GPU价格波动较小（±5%），价格波动对TC

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

价格波动敏感性：GPU价格在过去6个月内波动范围为±15%（如RTX 4090从$1600涨至$1800），数据中心GPU价格波动较小（±5%），价格波动对TCO的影响在3年周期内约为±10-15%

## Corrected Claim

GPU价格在过去6个月内存在一定波动（如RTX 4090价格有所上涨），数据中心GPU价格波动相对较小，价格波动对3年周期TCO有显著影响。

## Evidence

[质询]具体数值（±15%、±5%、±10-15%）及具体价格区间（$1600-$1800）属于经验事实，缺乏多源一致支持，且单一来源仅为可视化仪表盘，未提供明确的统计结论或数据表格直接证实这些精确的波动范围。 | 来源[1]主题相关（NVIDIA GPU价格趋势），但仅提供了可视化仪表盘的链接和标题，未直接陈述具体的波动百分比或价格区间，属于间接支持；经验事实缺直接来源支持，降级为定性表述。

## Search Query

GPU price volatility 2024 RTX 4090 H100 price change

## Retrieval Sources

- {'url': 'https://github.com/kikulmj/nvidia-gpu-price-dashboard/blob/master/%E5%9F%BA%E4%BA%8ENAVIDA%E6%98%BE%E5%8D%A1%E4%BB%B7%E6%A0%BC%E7%9A%84%E6%80%BB%E7%BB%93.md&rut=e06e5319591ac2d2c3c7c102472d2430aa50f3f46a4684af9d73dc0e99f5a144', 'type': 'ddg', 'title': 'nvidia-gpu-price-dashboard/基于NAVIDA显卡价格的总结.md at master · kikulmj ...'}
