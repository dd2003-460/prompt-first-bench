# N37: 市场公允价格 P_market 的代理变量计算公式：P_market = (P_median_recent * w_median + P_mean_volume

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

市场公允价格 P_market 的代理变量计算公式：P_market = (P_median_recent * w_median + P_mean_volume * w_mean) / (w_median + w_mean)，其中 w_median 和 w_mean 为权重，需根据商品类别（如电子产品 vs 奢侈品）进行差异化设定。

## Corrected Claim

市场公允价格 P_market 的代理变量计算公式：P_market = (P_median_recent * w_median + P_mean_volume * w_mean) / (w_median + w_mean)，其中 w_median 和 w_mean 为权重，需根据商品类别（如电子产品 vs 奢侈品）进行差异化设定。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了公式中的输入数据源（抽样误差）、两个核心代理变量的具体定义（中位数、加权均值）以及权重设定规则。各部分职责明确，互不重叠，且共同构成了父节点公式的完整实现逻辑。权重设定虽包含不同类目的具体数值，但这是参数化配置的必要部分，不属于冗余。）

## Search Query

market fair price proxy median recent sales volume weighted average
