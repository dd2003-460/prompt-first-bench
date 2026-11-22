# N121: 卖家侧历史残差投影：ε_seller 的历史依赖项量化为 ε_seller_history = α * Σ(β^t * ε_buyer_t)，其中 α 为学习率

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N36

## Claim

卖家侧历史残差投影：ε_seller 的历史依赖项量化为 ε_seller_history = α * Σ(β^t * ε_buyer_t)，其中 α 为学习率系数（典型值 0.2-0.4），β 为记忆衰减因子（典型值 0.7-0.9），ε_buyer_t 为第 t 期买家实际成交价与卖家预估价的偏差

## Corrected Claim

卖家侧历史残差投影：ε_seller 的历史依赖项量化为 ε_seller_history = α * Σ(β^t * ε_buyer_t)，其中 α 为学习率系数（典型值 0.2-0.4），β 为记忆衰减因子（典型值 0.7-0.9），ε_buyer_t 为第 t 期买家实际成交价与卖家预估价的偏差

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seller pricing bias historical transaction feedback learning rate
