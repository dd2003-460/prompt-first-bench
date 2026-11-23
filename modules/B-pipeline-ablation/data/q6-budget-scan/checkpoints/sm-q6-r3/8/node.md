# N17: 自建节点电力与机房成本量化：10个POP点，每点10台服务器，单台功耗500W，PUE 1.5，电价¥0.8/kWh，月电费约为 ¥18,000/点，总月电费 

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

自建节点电力与机房成本量化：10个POP点，每点10台服务器，单台功耗500W，PUE 1.5，电价¥0.8/kWh，月电费约为 ¥18,000/点，总月电费 ¥180,000。

## Corrected Claim

10个POP点，每点10台服务器，单台功耗500W，PUE 1.5，电价¥0.8/kWh，月电费约为 ¥4,320/点，总月电费 ¥43,200。

## Evidence

父节点级核验未通过：非正交, 不完备（1. 数据矛盾（非正交）：父节点声称月电费为 ¥180,000，但子节点计算结果为 ¥43,200，两者严重不符，存在逻辑矛盾。2. 覆盖不全（非完备）：父节点标题包含“电力与机房成本”，但子节点缺失了10个POP点的总硬件折旧成本汇总，也未提供最终的总成本汇总项。）

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_42526087/article/details/164049564&rut=14324b2ea135d04257608a525a205a5efde166303ba1844e007f6bbd0776b62e', 'type': 'ddg', 'title': '数据中心电力成本管理与pue优化实战：从计量到降耗的完整路径-csdn博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/93498882&rut=99faa57e3e67f35dabe05dd924d082bbf4756dde0a2c5e04fdda9f6e05c2438d', 'type': 'ddg', 'title': '边缘计算与PCDN：自建机房的成本与收益分析_边缘计算_weixin_34289454-亚马逊云科技技术品牌专区'}
- {'url': 'https://blog.csdn.net/weixin_32050773/article/details/166540360&rut=b32b7f0b9661ab68b0a8f33848c56d3241a73b987c761f277a0729310661c3ff', 'type': 'ddg', 'title': 'Idc机房建设与运行成本分析：从单柜投资到tco的算账方法-csdn博客'}
