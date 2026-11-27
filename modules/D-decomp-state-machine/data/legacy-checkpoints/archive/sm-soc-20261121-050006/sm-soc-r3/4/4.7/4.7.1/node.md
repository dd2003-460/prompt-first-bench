# N89: 强制显示均价导致的卖家挂价下调幅度 ΔP_ask 的量化模型：ΔP_ask = α_info * (P_ask_initial - P_median)，其中 α

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

强制显示均价导致的卖家挂价下调幅度 ΔP_ask 的量化模型：ΔP_ask = α_info * (P_ask_initial - P_median)，其中 α_info ∈ [0.2, 0.5] 为信息敏感度系数，P_median 为近30天成交中位数；该系数需通过 A/B 测试中的处理组与控制组挂价差异校准，当前估计为 [待核验]。

## Corrected Claim

强制显示均价导致的卖家挂价下调幅度 ΔP_ask 的量化模型：ΔP_ask = α_info * (P_ask_initial - P_median)，其中 α_info ∈ [0.2, 0.5] 为信息敏感度系数，P_median 为近30天成交中位数；该系数需通过 A/B 测试中的处理组与控制组挂价差异校准，当前估计为 [待核验]。（注：此为特定场景下的经验假设，缺乏通用理论或外部数据支持，需具体实验验证）

## Evidence

[质询]该模型为特定场景下的经验性假设，缺乏通用理论支持；且参考来源讨论的是量化交易中的盘口价差（Bid-Ask Spread），与二手/零售市场中卖家因强制显示均价而调整挂价（P_ask）的行为机制完全不同，存在严重的领域错配。 | 逻辑上公式结构自洽（线性调整模型），但参考来源[1]主题为量化交易微观结构，与卖家挂价行为无关，无法提供外部支持；作为经验事实，缺乏直接来源支持，故降级。

## Search Query

A/B test effect of displaying market price on seller listing price reduction magnitude alpha info sensitivity

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/706742625&rut=313c29e7c0f5decc88cbcad51d6d3fdb4d385ef0788ce241d21c172f586e5990', 'type': 'ddg', 'title': '在量化交易中，怎么用好盘口价差指标？ - 知乎'}
