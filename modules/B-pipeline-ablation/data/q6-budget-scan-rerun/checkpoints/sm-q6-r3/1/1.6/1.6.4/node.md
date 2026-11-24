# N42: 四线及以下城市用户占比15%（75万DAU），该部分用户完全依赖公有云CDN或回源中心机房，平均延迟贡献权重15%，P99延迟约300-500ms；该比例基于C

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

四线及以下城市用户占比15%（75万DAU），该部分用户完全依赖公有云CDN或回源中心机房，平均延迟贡献权重15%，P99延迟约300-500ms；该比例基于CNNIC 2024报告及抖音/快手用户画像数据校准

## Corrected Claim

四线及以下城市用户占比约15%（基于行业报告定性趋势估算），该部分用户依赖公有云CDN或回源，P99延迟较高（具体数值需实测校准）。

## Evidence

[质询]来源未提供具体的15%占比数值及75万DAU数据，且未提及抖音/快手用户画像校准细节，仅定性描述三线及以下城市占比下滑，无法直接支持具体数值。 | 来源[1]和[2]确认了三线及以下城市网络环境差异及占比趋势，但未提供具体15%占比及延迟数据，属于间接支持；经验事实（具体占比、延迟值）缺直接来源支持。

## Search Query

CNNIC 2024 China internet users fourth tier and below cities percentage

## Retrieval Sources

- {'url': 'https://www.sohu.com/a/1007808452_121649707&rut=9047a29d706fb6520b6bfa57f8933a5d9a1a47d892209b55997db6f1440826c0', 'type': 'ddg', 'title': '2025用户网络洞察报告（2026.04.02）_应用_移动_人群 - 搜狐'}
- {'url': 'https://www.sohu.com/a/1011185299_121924045&rut=f3ec20d23fad9aabd1d9bdaf00f76eaf106012a7457bacaac506ce86651d105c', 'type': 'ddg', 'title': '2025用户网络洞察报告_应用_占比_移动 - 搜狐'}
