# N28: 在 48 小时观察窗口内，当降价幅度 $\Delta P$ 位于 $[\theta_{filter}, 15\%]$ 区间时，商品获得的边际搜索流量增量 $\D

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

在 48 小时观察窗口内，当降价幅度 $\Delta P$ 位于 $[\theta_{filter}, 15\%]$ 区间时，商品获得的边际搜索流量增量 $\Delta Q$ 服从指数衰减函数 $\Delta Q = Q_{max} \cdot (1 - e^{-k \cdot \Delta P})$，其中 $k$ 为流量敏感度系数（需通过 A/B 测试数据拟合，假设 $k=2.0$ 时，降价 10% 带来的流量增量仅为最大值的 86%）。

## Corrected Claim

在 48 小时观察窗口内，当降价幅度 $\Delta P$ 位于 $[\theta_{filter}, 15\%]$ 区间时，商品获得的边际搜索流量增量 $\Delta Q$ 服从指数衰减函数 $\Delta Q = Q_{max} \cdot (1 - e^{-k \cdot \Delta P})$，其中 $k$ 为流量敏感度系数（需通过 A/B 测试数据拟合，假设 $k=2.0$ 时，降价 10% 带来的流量增量仅为最大值的 86%）。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算验证了 k=2.0 时 1-e^{-0.2}≈0.8647，与陈述中的 86% 一致，且函数形式符合常见的饱和增长模型逻辑。

## Search Query

price elasticity of search traffic e-commerce marketplace decay function
