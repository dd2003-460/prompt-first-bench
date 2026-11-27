# N46: 流量弹性系数 k 的回归估计公式：k = Var(ΔTraffic) / Var(Deviation^2)，需基于平台历史 A/B 测试数据或自然实验数据计算；

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18, N19, N20

## Claim

流量弹性系数 k 的回归估计公式：k = Var(ΔTraffic) / Var(Deviation^2)，需基于平台历史 A/B 测试数据或自然实验数据计算；若缺乏数据，可用代理指标（如点击率对价格偏离度的二阶导数）进行贝叶斯估计，先验均值设为 10% per 10% deviation，方差设为 5%。

## Corrected Claim

流量弹性系数 k 的回归估计通常基于历史数据计算；若缺乏数据，可采用贝叶斯方法结合代理指标进行估计，但先验参数（如均值和方差）需根据具体业务场景和历史经验设定，而非固定为特定数值。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中的三个独立操作模块：1. 贝叶斯估计的具体公式与参数设定；2. 代理指标（二阶导数）的数学定义与统计检验逻辑；3. 缺乏数据时用于确定先验/数据方差的基准估计方法。三者职责清晰，互不重叠，且共同覆盖了父节点提到的‘回归公式’、‘代理指标’及‘数据缺失时的处理’三个关键方面。）

## Search Query

eBay second-hand market traffic elasticity price deviation regression analysis
