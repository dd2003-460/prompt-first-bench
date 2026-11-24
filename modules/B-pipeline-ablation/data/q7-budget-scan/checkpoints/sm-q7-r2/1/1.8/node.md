# N13: HDD 单位容量功耗（W/TB），基于 16TB HDD 典型空闲 4-5W、读写 8-10W 计算

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

HDD 单位容量功耗（W/TB），基于 16TB HDD 典型空闲 4-5W、读写 8-10W 计算

## Corrected Claim

HDD 单位容量功耗（W/TB），基于 16TB HDD 典型空闲约 4-5W、读写约 5-10W（视负载及型号而定）计算

## Evidence

父节点级核验未通过：不完备（父节点明确限定为“基于 16TB HDD 典型空闲 4-5W、读写 8-10W”进行计算，这隐含了仅考虑 Active 状态（Read/Write/Active Idle）的功耗模型。然而，子节点引入了“Spin-down”状态及其功耗，并假设了包含 60% Spin-down 的工作负载。这导致两个主要问题：1. 完备性缺失：子节点中关于 Read/Write/Active Idle 的具体功耗数值（父节点已给定的 4-5W, 8-10W）并未作为独立的子节点或参数显式列出，而是隐藏在父节点描述中，导致分解结构不完整，无法直接通过子节点推导父节点结果。2. 逻辑不一致：父节点的前提条件未包含 Spin-down，但子节点却依赖 Spin-down 进行计算，存在前提与分解逻辑的错位。）

## Search Query

enterprise HDD power consumption watts idle active 16TB

## Retrieval Sources

- {'url': 'https://www.zhihu.com/question/642618994&rut=26c339bb21b1a49c4835b4bb70c72bc311b91d9aae5c3d6fcfd99944da1716f4', 'type': 'ddg', 'title': '希捷16tb功耗多少？ - 知乎'}
- {'url': 'https://zhidao.baidu.com/question/1055485736253777779.html&rut=f0627ddbb81f633f87fb5b2b649f29823007f8ac243c438b27f3afa6aadc2c57', 'type': 'ddg', 'title': '西部数据氦气硬盘16t功耗 - 百度知道'}
