# N11: 摩擦耗散贡献量级估算：假设边界层高度 h~1km，风应力 τ~2-5 Pa，单位面积功率耗散 P=τ*V ~ 20-50 W/m²，相比潜热输入 ~100-20

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

摩擦耗散贡献量级估算：假设边界层高度 h~1km，风应力 τ~2-5 Pa，单位面积功率耗散 P=τ*V ~ 20-50 W/m²，相比潜热输入 ~100-200 W/m²，摩擦耗散约占总能量的 20-50%，是重要的次要项而非唯一主导项。

## Corrected Claim

摩擦耗散贡献量级估算：基于边界层高度h~1km和风应力τ~2-5 Pa的量级假设，单位面积功率耗散P=τ*V约为20-50 W/m²。相较于潜热输入~100-200 W/m²，摩擦耗散在数量级上属于次要项（约占20-50%），但具体占比需依赖具体气象案例的能量收支分析，现有来源未提供直接实证支持。

## Evidence

[质询]参考来源均为CFD工程模拟或特定边界条件推导，缺乏气象学中关于台风/风暴能量收支（潜热 vs 摩擦耗散）的直接观测数据或权威文献支持，无法验证具体的数值量级（20-50%占比）是否准确。 | 逻辑推导自洽（P=τV量级估算合理），但参考来源[1][2][3]主要涉及CFD仿真与边界层理论推导，未提供大气能量收支的经验数据支持，属于经验事实且缺直接来源支持。

## Search Query

surface friction dissipation power budget tropical cyclone landfall watts per square meter

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_32520095/article/details/169230678&rut=4bac8627ed4dfd26f1f369307f026d7eed17f554ceca91bcea106ed0b0b2a610', 'type': 'ddg', 'title': 'C/C++实现大气边界层风剖面与湍动能耗散率计算及Fluent UDF集成-CSDN博客'}
- {'url': 'https://blog.csdn.net/m0_57781768/article/details/140683226&rut=4b6db1e6bf985b411f1a7322c14c8ccf902736891208db1efe0e9cdc6ad2a3a1', 'type': 'ddg', 'title': '利用Fluent进行风剖面、湍流剖面及耗散率剖面的开发与分析：基于日本规范的应用详解_fluent剖面-CSDN博客'}
- {'url': 'https://pubs.cstam.org.cn/article/doi/10.15959/j.cnki.0254-0053.2015.02.017&rut=341bfd2402ba8bc28c6c00f2a0d7d97f1e144117f609fe8300205a72284a1e1e', 'type': 'ddg', 'title': '一类平衡大气边界层边界条件研究 - cstam.org.cn'}
