# N177: 价格策略投影：卖家实际挂价 P_actual = intrinsic_value * (1 + anchor_bias) + ε_price，其中 anchor

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N54

## Claim

价格策略投影：卖家实际挂价 P_actual = intrinsic_value * (1 + anchor_bias) + ε_price，其中 anchor_bias = 0.2 为系统性高估，ε_price ~ N(0, 0.15^2) 为独立随机噪声；需计算 P_actual 落在 [intrinsic_value*0.8, intrinsic_value*1.5] 区间外的概率，若 > 5% 则策略空间边界需重新校准。

## Corrected Claim

价格策略投影模型假设卖家挂价 P_actual = intrinsic_value * (1 + anchor_bias) + ε_price，其中 anchor_bias 和 ε_price 为待校准的系统性偏差与随机噪声项；需基于实证数据确定参数分布后，计算 P_actual 落在 [intrinsic_value*0.8, intrinsic_value*1.5] 区间外的概率以评估策略边界。

## Evidence

[质询]该陈述包含具体的经验参数（anchor_bias=0.2, 噪声标准差=0.15），这些数值并非第一性原理可推导，且参考来源中未提供这些具体参数的实证支持或定义，属于缺乏来源支撑的经验假设。 | 逻辑上概率计算框架自洽，但 anchor_bias 和噪声分布的具体数值为经验事实，参考来源 [1] 讨论 ICT 价格投射战法，[2] 定义内在价值，均未提供该特定定价模型参数的直接支持或数据验证，故降级。

## Search Query

seller actual price distribution anchor bias random noise variance second hand market

## Retrieval Sources

- {'url': 'https://www.toutiao.com/w/1861956322613257/&rut=5cf839f9691a4a7de17b98719bcbbf63f8073349a4a3d0b03b399342b79363a2', 'type': 'ddg', 'title': '3 种 ICT 交易核心量价战法 操作手册（通俗拆解版） 这张图是 ICT（Inner Circle Trader）交易体系里3 种经典的价格 ...'}
- {'url': 'https://en.wikipedia.org/wiki/Intrinsic_value_(finance)&rut=dc5cd30db9cfb23755542962964cc155ae74130c93a51cfff81c7dac5b21aa3a', 'type': 'ddg', 'title': 'Intrinsic value (finance) - Wikipedia'}
