# N230: 自建带宽利用率 U_bw = Actual_Bandwidth / Leased_Bandwidth = 3.5 Gbps / (10 POP * 10 Gbp

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

自建带宽利用率 U_bw = Actual_Bandwidth / Leased_Bandwidth = 3.5 Gbps / (10 POP * 10 Gbps) = 3.5%；极低利用率导致固定成本分摊后单位成本高昂，需提高缓存命中率 H 或增加 POP 数量以降低单位带宽成本，或转向公有云 CDN 以利用其规模效应。

## Corrected Claim

自建带宽利用率 U_bw = Actual_Bandwidth / Leased_Bandwidth = 3.5 Gbps / (10 POP * 10 Gbps) = 3.5%；极低利用率导致固定成本分摊后单位成本高昂，需提高缓存命中率 H 或增加 POP 数量以降低单位带宽成本，或转向公有云 CDN 以利用其规模效应。

## Evidence

父节点级核验未通过：非正交（子节点1（利用率临界点）和子节点3（时间维度敏感性）在逻辑上存在重叠和潜在矛盾。子节点1强调需提高流量/缓存命中率以解决利用率低的问题，隐含了静态或平均视角；而子节点3指出成本优化应基于日均流量且峰值边际成本为0，这实际上削弱了子节点1中关于‘需提升流量至50,000 GB/月’的紧迫性论证（因为峰值未超上限意味着不需要为峰值扩容，只需关注日均）。此外，子节点1和子节点3都涉及‘单位成本’的计算逻辑，但侧重点不同（一个是静态阈值，一个是时间波动），若未明确区分‘平均利用率’与‘峰值/低谷利用率’对成本的不同影响，会导致读者混淆。虽然不重复，但边界不够清晰，正交性稍弱。）
