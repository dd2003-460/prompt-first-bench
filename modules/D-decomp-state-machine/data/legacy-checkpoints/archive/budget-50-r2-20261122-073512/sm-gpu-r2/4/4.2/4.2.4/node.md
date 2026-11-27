# N151: E_unit_price（当地电价）的区域化实例化：美国东部平均电价 = $0.15/kWh（2024, EIA 数据, [时效待核]）；欧洲平均电价 = $0

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

E_unit_price（当地电价）的区域化实例化：美国东部平均电价 = $0.15/kWh（2024, EIA 数据, [时效待核]）；欧洲平均电价 = $0.20/kWh（2024, [时效待核]）；中国东部平均电价 = $0.10/kWh（2024, [时效待核]）；需根据用户所在地选择对应值。

## Corrected Claim

E_unit_price（当地电价）的区域化实例化：美国东部平均电价 ≈ $0.16/kWh；欧洲平均电价 ≈ $0.25/kWh；中国东部平均电价 ≈ $0.09/kWh（2024年估算值，需根据最新EIA/IEA数据及汇率实时校准）。

## Evidence

[质询]数值量级与具体年份数据可能存在偏差：2024年美国平均居民电价约为$0.16-$0.17/kWh，欧洲（特别是西欧）平均电价通常高于$0.20/kWh（常达$0.25-$0.30/kWh），中国东部工业/居民电价换算后约为$0.08-$0.10/kWh。虽然量级正确，但具体数值（如欧洲$0.20）可能偏低或代表特定子区域/年份，且来源未提供2024年具体数据支持。 | 逻辑自洽，量级符合常识（美<欧，中<美），但参考来源[1][2][3]仅涉及电价API接入、优化算法及概念问答，未提供2024年具体区域的平均电价数值，属于经验事实且缺乏直接来源支持。

## Search Query

average electricity price per kWh USA Europe China 2024 commercial industrial

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00329/article/details/156506837&rut=4f237e704e5d97544f00a5411ead61910bc476aff68eb819f92599db64041a5f', 'type': 'ddg', 'title': '电力价格api完整指南：三步实现实时电价数据接入-csdn博客'}
- {'url': 'https://blog.csdn.net/x2y3z4a5b/article/details/162891157&rut=dbb4722083d95ae8b9cd64e6e89e38abac6ac8fa55206447c46182b26b2c3d81', 'type': 'ddg', 'title': '基于内点法的电力系统实时电价优化Matlab实现（含30节点案例与可视化结果）-CSDN博客'}
- {'url': 'https://ask.csdn.net/questions/9247285&rut=72b8938998bdcbb278c2eedf02fe6f619587447a8988050c3c8e8cc996d30c14', 'type': 'ddg', 'title': '电费单价设置如何实现分时、分段、分区域动态联动？_编程语言-csdn问答'}
