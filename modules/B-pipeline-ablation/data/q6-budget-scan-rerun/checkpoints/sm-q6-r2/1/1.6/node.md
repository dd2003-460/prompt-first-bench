# N8: 用户地理分布假设：中国 C 端用户 500 万日活，地理分布为：一线 25%、二线 35%、三线 25%、四线及以下 15%（基于 CNNIC 2024 报告及

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

用户地理分布假设：中国 C 端用户 500 万日活，地理分布为：一线 25%、二线 35%、三线 25%、四线及以下 15%（基于 CNNIC 2024 报告及抖音/快手用户画像数据）

## Corrected Claim

用户地理分布假设：中国 C 端用户 500 万日活，地理分布大致符合中国互联网用户下沉趋势（如一线约20-30%，二线约30-40%，三线及以下约40-50%），具体比例需依据最新CNNIC报告及目标平台（抖音/快手）实际用户画像数据校准。

## Evidence

[质询]具体数值（一线25%、二线35%等）属于经验事实，参考来源未提供CNNIC 2024报告或抖音/快手的具体用户画像数据，无法验证这些精确百分比的准确性，且不同平台（如抖音vs快手）的下沉市场占比差异较大，直接套用单一分布假设存在口径混淆风险。 | 逻辑自洽（总和100%，符合中国互联网用户下沉趋势的大致量级），但参考来源[1][2]仅涉及地理数据分析技术或特定在线教育案例，未提供CNNIC 2024或短视频平台的具体地理分布数据，属于经验事实缺来源直接支持。

## Search Query

China mobile user geographic distribution tier1 tier2 tier3 2024 CNNIC

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_42554162/article/details/160574003&rut=259aad8a3845e1dc007c6a3afd42a1fd555617bd4322986b7b8002b9f65b6a98', 'type': 'ddg', 'title': '用户地理数据分析系统：从ip解析到可视化全链路实践-csdn博客'}
- {'url': 'https://blog.csdn.net/m0_49915249/article/details/115028511&rut=b6848d85564d4718f7615304643d28fc1d71e24b2fab4249a3c3d1dc4cf87f48', 'type': 'ddg', 'title': '在线教育平台的数据分析——用户的地域分布 - Csdn博客'}
