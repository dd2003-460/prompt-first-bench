# N103: 买家放弃概率 P(Abort) 的分布拟合：验证 P(Abort) = 1 - exp(-(P_ask - P_market)/σ_price) 模型是否适用于

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

买家放弃概率 P(Abort) 的分布拟合：验证 P(Abort) = 1 - exp(-(P_ask - P_market)/σ_price) 模型是否适用于不同价格区间，需计算不同溢价率（10%, 20%, 30%）下的实际放弃率与模型预测值的残差。

## Corrected Claim

买家放弃概率 P(Abort) 的分布拟合：需通过实证数据验证 P(Abort) = 1 - exp(-(P_ask - P_market)/σ_price) 模型在不同价格区间的适用性，具体方法为计算不同溢价率（10%, 20%, 30%）下的实际放弃率与模型预测值的残差。

## Evidence

[质询]该陈述描述的是一个具体的实证验证任务（计算残差），而非一个已确立的数学恒等式或物理定律。其核心假设（放弃概率服从指数分布且仅由价格差决定）是一个经验性模型假设，无法从第一性原理严格推导，且缺乏数据支持其普适性。 | 经验事实/实证任务，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

buyer drop out probability price premium distribution fit used market data
