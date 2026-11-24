# N52: 工作点C（低成本/冷数据主导）：鉴于80%为冷数据，进一步压缩SSD层至50TB（¥12,500），HDD层450TB（¥15,750）；采用软件定义分层（利用

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

工作点C（低成本/冷数据主导）：鉴于80%为冷数据，进一步压缩SSD层至50TB（¥12,500），HDD层450TB（¥15,750）；采用软件定义分层（利用Linux DM-cache或ZFS）替代专用硬件，管理成本¥5,000；服务器¥30,000；总CapEx ≈ ¥63,250，折合¥127/有效TB，但温数据扫描时间可能延长，需权衡性能损失。

## Corrected Claim

工作点C（低成本/冷数据主导）：鉴于80%为冷数据，进一步压缩SSD层至50TB，HDD层450TB；采用软件定义分层替代专用硬件；总CapEx估算约为¥63,250（基于当前市场参考价），折合约¥127/有效TB，但温数据扫描时间可能延长，需权衡性能损失。

## Evidence

[质询]具体硬件价格（SSD/HDD单价、服务器成本）及总CapEx计算属于特定市场时点的经验事实，无法从第一性原理推导，且参考来源未提供具体数值支持，存在价格波动或配置差异导致数值不准确的风险。 | 逻辑校验通过（50+450=500TB，12500+15750+5000+30000=63250元，63250/500≈126.5元/TB，四舍五入为127元/TB，计算自洽）；来源[1]仅定性支持冷数据降本策略，未提供具体价格数据，属经验事实缺直接来源支持。

## Search Query

software defined tiered storage cost savings hardware reduction

## Retrieval Sources

- {'url': 'https://developer.baidu.com/article/detail.html?id=6423206&rut=3b921c5ea651341725724b972480e2bff43fde3932e36214a5657f41cbfeb8e7', 'type': 'ddg', 'title': '冷数据存储：成本优化与长期保存的实践方案-百度开发者中心'}
