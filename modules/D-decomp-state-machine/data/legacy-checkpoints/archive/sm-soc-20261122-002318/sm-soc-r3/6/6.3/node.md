# N90: 拒绝行为对成交周期 T_cycle 的边际影响：ΔT_cycle = k_reject * P(Reject) * T_negotiation，其中 k_rej

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N31

## Claim

拒绝行为对成交周期 T_cycle 的边际影响：ΔT_cycle = k_reject * P(Reject) * T_negotiation，其中 k_reject 为因拒绝导致的重新匹配时间系数，T_negotiation 为平均谈判时长，需量化 k_reject 以评估该演化启发式对宏观‘短周期’现象的抑制或促进方向。

## Corrected Claim

拒绝行为对成交周期 T_cycle 的边际影响可建模为 ΔT_cycle = k_reject * P(Reject) * T_negotiation，其中 k_reject 为重新匹配时间系数，该模型需通过具体场景数据量化 k_reject 以评估其对宏观周期的影响方向。

## Evidence

[质询]该公式为特定模型下的经验性假设，缺乏通用理论支持；参考来源仅定义通用周期时间概念，未涉及拒绝行为对成交周期的具体量化影响机制，无法证实该特定线性关系及系数 k_reject 的普适性。 | 逻辑自洽（量纲合理：时间=系数*概率*时间），但参考来源[1][2]仅解释Cycle Time/Order Cycle Time定义，与‘拒绝行为边际影响’这一具体机制无关，属经验事实且缺直接来源支持。

## Search Query

impact of seller rejection on transaction cycle time online marketplace negotiation duration

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2065804184570663482&rut=b97ce2ea0aacbaf0ed32642a94e7b2c675a8a4ce9bfaab20ed6e043405084002', 'type': 'ddg', 'title': 'Takt Time（TT）、Cycle Time（CT）与 Lead Time（LT）分别是什么？'}
- {'url': 'https://zhuanlan.zhihu.com/p/714672735&rut=1aece2afe1c5800acba7f4f409b91c07fa58d4d4b42ee47060360b9c6f8fa9ed', 'type': 'ddg', 'title': '订单周期时间（Order Cycle Time）详解：定义、影响因素与优化策略'}
