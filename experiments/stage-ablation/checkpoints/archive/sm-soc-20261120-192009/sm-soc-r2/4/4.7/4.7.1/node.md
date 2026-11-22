# N95: 买家行为代理指标定义：'查看成交价后调整预算' 定义为：用户在浏览某商品详情页并点击'历史成交价'模块后，其后续搜索关键词中的价格上限 P_max 下调幅度 >

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

买家行为代理指标定义：'查看成交价后调整预算' 定义为：用户在浏览某商品详情页并点击'历史成交价'模块后，其后续搜索关键词中的价格上限 P_max 下调幅度 > 5%；该行为发生率 f_adjust 需通过日志数据中 (P_max_t+1 - P_max_t) / P_max_t < -0.05 的事件占比计算。

## Corrected Claim

买家行为代理指标定义：'查看成交价后调整预算' 定义为：用户在浏览某商品详情页并点击'历史成交价'模块后，其后续搜索关键词中的价格上限 P_max 下调幅度 > 5%；该行为发生率 f_adjust 需通过日志数据中 (P_max_t+1 - P_max_t) / P_max_t < -0.05 的事件占比计算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Definition of budget adjustment behavior in e-commerce user logs
