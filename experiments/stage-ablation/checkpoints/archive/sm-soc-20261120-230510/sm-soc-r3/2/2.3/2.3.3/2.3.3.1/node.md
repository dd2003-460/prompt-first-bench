# N172: 买家保留价格 V_buyer 的量化：V_buyer = V_base + δ_replacement，其中 V_base 为同类商品市场均价（P_median

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N52

## Claim

买家保留价格 V_buyer 的量化：V_buyer = V_base + δ_replacement，其中 V_base 为同类商品市场均价（P_median），δ_replacement 为替代成本溢价（典型值 5-15% of P_median），反映买家为避免等待替代品的额外支付意愿。

## Corrected Claim

买家保留价格 V_buyer 可量化为 V_base + δ_replacement，其中 V_base 为同类商品市场均价，δ_replacement 为替代成本溢价，具体数值需根据市场情境确定（典型值可能在5-15%区间，但缺乏通用来源支持）。

## Evidence

[质询]该陈述属于特定经济模型或场景下的经验性参数设定（如5-15%的替代成本溢价），并非普适的经济定律或第一性原理可推导的数学事实，且参考来源完全无关，缺乏直接证据支持该具体数值范围。 | 逻辑自洽（保留价格=基准价+溢价符合经济学直觉），但参考来源[1]讨论的是VWAP技术指标，与买家保留价格量化无关，属于经验事实且缺来源支持。

## Search Query

buyer reservation price replacement cost premium used goods market

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1926694507409277492&rut=96b665bb4fc576aeb2351d4c09dc70a9982ee1c9d18682df9a591f0d095be145', 'type': 'ddg', 'title': '成交量加权平均价格（VWAP）因子：知识与研究深度解析'}
