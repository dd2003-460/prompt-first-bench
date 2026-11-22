# N22: 卖家受损量化：高挂价卖家（P_ask > P_median * 1.15）在干预措施B下曝光量减少 50%，假设其成交概率 p_deal 从 0.3 降至 0.

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5

## Claim

卖家受损量化：高挂价卖家（P_ask > P_median * 1.15）在干预措施B下曝光量减少 50%，假设其成交概率 p_deal 从 0.3 降至 0.15，期望收入 ΔRev_seller = -0.5 * p_deal * P_ask，同时降价卖家（P_ask ≤ P_median * 1.15）获得 +20% 曝光，期望收入 ΔRev_seller_low = +0.2 * p_deal_low * P_ask_low，净效应取决于高/低挂价卖家比例 r_high ∈ [0.3, 0.5] [待核验]。

## Corrected Claim

卖家受损量化模型：假设高挂价卖家在干预措施B下曝光量减少50%，成交概率从0.3降至0.15，期望收入变化为 -0.5 * p_deal * P_ask；降价卖家曝光增加20%，期望收入变化为 +0.2 * p_deal_low * P_ask_low。净效应取决于高/低挂价卖家比例 r_high（具体数值需根据实际市场数据校准，此处假设区间为 [0.3, 0.5]）。

## Evidence

[质询]该陈述包含大量具体的经验性参数（如曝光减少50%、成交概率从0.3降至0.15、曝光增加20%、高挂价卖家比例区间[0.3, 0.5]），这些数值并非基于第一性原理或数学公理推导，而是依赖于特定市场环境和干预措施B的具体定义，属于经验事实。 | 参考来源[1][2][3]均讨论市场微结构、订单簿建模及价差预测，与具体的卖家干预措施量化模型无关，无法提供外部支持；该陈述为经验事实，逻辑自洽但缺乏来源直接支持，故降级。

## Search Query

seller revenue impact search ranking change high priced items

## Retrieval Sources

- {'url': 'https://quant67.com/post/quant/03-microstructure/03-microstructure.html&rut=1a7cff487e8b3fbe0ed23c3bd734276c40f0a37328d80ef7909343eefa3b66e3', 'type': 'ddg', 'title': '【量化交易】市场微结构：订单簿、价差、流动性、冲击 | 土法炼钢 · 系统与基础设施'}
- {'url': 'https://marketmaker.cc/zh/blog/post/spread-modeling-machine-learning/&rut=c40258993ac485fcacaf9119a98ca69692d1196706dd4a79093671412521bcd3', 'type': 'ddg', 'title': '用机器学习对买卖价差进行建模与预测 | marketmaker.cc'}
- {'url': 'https://archimedesspx.com/2025/11/11/%E9%87%8F%E5%8C%96lesson2/&rut=29f8cf963da9d8e2c64c71f8b4ffd10d6e23d8078bfb212aebade687e2426ef8', 'type': 'ddg', 'title': '量化lesson2 - archimedesspx的生活指南'}
