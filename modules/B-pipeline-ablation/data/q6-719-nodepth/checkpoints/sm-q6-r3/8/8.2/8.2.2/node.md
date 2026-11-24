# N378: 自建节点带宽成本工作点1（高带宽高固定成本）：10个POP点，每个POP租赁10Gbps带宽，一线城市5个单价¥8000/月/10Gbps，二线城市5个单价¥5

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N132

## Claim

自建节点带宽成本工作点1（高带宽高固定成本）：10个POP点，每个POP租赁10Gbps带宽，一线城市5个单价¥8000/月/10Gbps，二线城市5个单价¥5000/月/10Gbps，总带宽成本 = 5×8000 + 5×5000 = 65000元/月；此成本不随流量变化，是固定成本。

## Corrected Claim

自建节点带宽成本工作点1（高带宽高固定成本）：10个POP点，每个POP租赁10Gbps带宽，假设一线城市5个单价¥8000/月/10Gbps，二线城市5个单价¥5000/月/10Gbps，则总带宽成本约为65000元/月；此成本为固定成本，不随流量变化。

## Evidence

[质询]具体单价（¥8000/月/10Gbps 和 ¥5000/月/10Gbps）属于经验事实，缺乏权威来源直接支持，且不同运营商、不同时期价格波动较大，存在口径混淆或数据过时的风险。 | 逻辑推导成立（5*8000+5*5000=65000），但参考来源[1]仅涉及POP组网拓扑，[2]涉及跨境网络成本但量级和场景不符，均无直接支持该具体单价的证据；作为经验事实，缺来源支持故降级。

## Search Query

China datacenter 10Gbps port rental price tier 1 vs tier 2 cities 2024

## Retrieval Sources

- {'url': 'https://www.h3c.com/cn/pub/Document_Center/2025/09/WebHelp_AD_WAN_FZFAGZCLSC/html/topic_634221.html&rut=996762c841ce3ec8fec2969e554de599f1e3f33747ff375cbb4c6a78eecc76f2', 'type': 'ddg', 'title': '多租户pop组网（Msp运营组网） - H3c'}
- {'url': 'https://blog.csdn.net/Bobolink_/article/details/163073091&rut=b8e1b5726fb2931bd51ef63d08e4cc1c4298cc1bc576ecf61c7d7f51f0b6d1d1', 'type': 'ddg', 'title': '跨境网络自己搭建vs直接买现成服务，成本和时间分别差多少_跨境网络搭建-CSDN博客'}
