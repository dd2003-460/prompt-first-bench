# N41: 三线城市用户占比25%（125万DAU），该部分用户主要使用公有云CDN，平均延迟贡献权重25%，P99延迟约200-300ms；该比例基于CNNIC 2024

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

三线城市用户占比25%（125万DAU），该部分用户主要使用公有云CDN，平均延迟贡献权重25%，P99延迟约200-300ms；该比例基于CNNIC 2024报告及抖音/快手用户画像数据校准

## Corrected Claim

三线城市用户主要使用公有云CDN，平均延迟贡献权重约25%，P99延迟可能在200-300ms区间（具体占比及延迟数值需依据CNNIC 2024报告及抖音/快手用户画像数据进一步校准，当前来源未提供直接数值支持）。

## Evidence

[质询]来源未直接支持“三线城市用户占比25%”及“P99延迟200-300ms”的具体数值，且来源[2]仅提及三线城市WiFi占比，未提供用户总量占比或延迟数据，存在数据缺失风险。 | 来源[1]和[2]为2025年用户网络洞察报告，主题相关但摘要中未包含“三线城市用户占比25%”或“P99延迟”的具体数值支持，仅能间接确认报告存在及涉及三线城市网络环境分析，无法直接验证具体参数。

## Search Query

CNNIC 2024 China internet users third tier cities percentage

## Retrieval Sources

- {'url': 'https://www.sohu.com/a/1011185299_121924045&rut=f3ec20d23fad9aabd1d9bdaf00f76eaf106012a7457bacaac506ce86651d105c', 'type': 'ddg', 'title': '2025用户网络洞察报告_应用_占比_移动 - 搜狐'}
- {'url': 'https://www.sohu.com/a/1008548291_120855974&rut=80ff504aa7a0de19d9378ba229e1e9cecd6685c6b97e9135f3e10aecc835f396', 'type': 'ddg', 'title': '2025用户网络洞察报告_占比_应用_人群 - 搜狐'}
