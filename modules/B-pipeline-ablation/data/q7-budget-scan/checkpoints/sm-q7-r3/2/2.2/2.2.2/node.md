# N51: 工作点B（标准配比）：SSD层100TB（¥25,000 @¥250/TB），HDD层400TB（¥14,000 @¥35/TB）；分层软件许可/硬件¥10,0

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

工作点B（标准配比）：SSD层100TB（¥25,000 @¥250/TB），HDD层400TB（¥14,000 @¥35/TB）；分层软件许可/硬件¥10,000；服务器¥30,000；总CapEx ≈ ¥79,000，折合¥158/有效TB，满足基本SLA，是大多数数据湖的推荐起点。

## Corrected Claim

工作点B（标准配比）：SSD层100TB，HDD层400TB；假设SSD单价¥250/TB，HDD单价¥35/TB，分层软件/硬件¥10,000，服务器¥30,000，则总CapEx约为¥79,000，折合¥158/有效TB。此配置通常被视为满足基本SLA的数据湖推荐起点，但具体成本需根据实际采购价格调整。

## Evidence

父节点级核验未通过：不完备（子节点在维度上是正交的（分别对应电力、折旧、人力、容量修正），且无冗余。但完备性不足：父节点明确提到“满足基本SLA”，而子节点中缺乏关于延迟、IOPS或可靠性等性能指标的验证；此外，子节点4修正了有效容量和单价（¥171.7），但这与父节点声称的“¥158”存在表面矛盾，虽然子节点解释了原因，但父节点作为基准描述应保持一致性或明确标注为“裸容量单价”，否则在知识图谱中会造成数据冲突。更重要的是，缺少对“分层策略本身”带来的性能提升或成本优化效果的量化分析（如相比全SSD或全HDD的优势），仅拆解了成本构成而未涵盖“为什么选这个工作点”的核心论证部分（除了价格）。）

## Search Query

HDD SSD tiered storage typical configuration cost 100TB SSD 400TB HDD

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/634851956&rut=f31a7ce9687aa30e0b858d15533efdd636f55d9e847c0364285920663bb5747a', 'type': 'ddg', 'title': '[Sauron] 基于真实100TB数据的SSD组与评测 - 知乎'}
