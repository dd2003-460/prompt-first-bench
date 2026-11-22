# N79: 数据似然函数 P(Data|H1) 的量化：Data 包含'高挂价'与'短周期'两个观测，P(Data|H1) = P(Short_Cycle|High_Pri

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

数据似然函数 P(Data|H1) 的量化：Data 包含'高挂价'与'短周期'两个观测，P(Data|H1) = P(Short_Cycle|High_Price, H1) * P(High_Price|H1)；需基于历史数据拟合高挂价商品在H1假设下的周期分布均值与标准差，以计算具体概率值。

## Corrected Claim

在假设H1下，若数据包含'高挂价'与'短周期'两个观测，其似然函数可依据链式法则分解为 P(Short_Cycle|High_Price, H1) * P(High_Price|H1)，具体数值需基于历史数据拟合分布参数计算。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1和子节点2分别对应父节点公式中的两个独立因子 P(Cycle|...) 和 P(High_Price|...)，符合独立性假设下的乘法原理，彼此正交。子节点3提供了零假设对照，虽然不直接属于 P(Data|H1) 的计算，但父节点明确提到‘以计算具体概率值’通常隐含与基准的比较（似然比），且该节点作为独立假设下的参数拟合，与H1下的拟合不重复。整体覆盖了分布拟合、概率计算及对照基准，无冗余。）

## Search Query

likelihood function high price short cycle transaction data second hand

## Retrieval Sources

- {'url': 'https://blog.csdn.net/wenqiwenqi123/article/details/79819542&rut=c2e3c355cd67e7b6ae0cc6ae26c99456825c3afe6a034ce8e0a1cd7190273eee', 'type': 'ddg', 'title': '似然函数解析-csdn博客'}
