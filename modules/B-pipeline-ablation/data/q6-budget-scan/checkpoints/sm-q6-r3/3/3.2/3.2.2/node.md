# N84: 自建POP点带宽采购最小单位与闲置成本：运营商通常以1Gbps为最小购买单元或提供100M/1G/10G套餐；若每点仅购1Gbps带宽（月费约¥5,000-15

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

自建POP点带宽采购最小单位与闲置成本：运营商通常以1Gbps为最小购买单元或提供100M/1G/10G套餐；若每点仅购1Gbps带宽（月费约¥5,000-15,000/点），10点月费¥50,000-150,000；若冗余配置10Gbps（月费¥50,000-100,000/点），则存在80-95%带宽闲置，导致单位有效带宽成本虚高

## Corrected Claim

自建POP点带宽采购通常以1Gbps为最小单元或提供阶梯套餐；若按典型市场估算，每点1Gbps月费约¥5,000-15,000，10点总月费¥50,000-150,000；若冗余配置10Gbps（月费约¥50,000-100,000/点），在低负载下可能导致80-95%带宽闲置，从而推高单位有效带宽成本。

## Evidence

父节点级核验未通过：不完备（子节点之间逻辑清晰且正交（定价模型、利用率基准、成本计算公式）。但完备性不足：父节点核心在于解释‘最小购买单元’和‘套餐’导致的结构性闲置（如买1G实际只用200M），而子节点主要关注基于流量峰值的动态利用率，未明确涵盖‘最小粒度限制’这一关键结构性因素，导致无法完全解释父节点中‘80-95%闲置’的特定来源。）

## Search Query

China telecom edge POP bandwidth pricing 1Gbps 10Gbps monthly cost 2024

## Retrieval Sources

- {'url': 'https://b2bwiki.baidu.com/article/aw_56bcad9c6793fff31e116a6a028328dc&rut=c439a1f5a23c5d0155dc849c8652a3b5296bf1fbc574eb875241aeece4f2eb2e', 'type': 'ddg', 'title': '闲置宽带资源化改造：采购成本测算与设备选型要点'}
- {'url': 'https://developer.baidu.com/article/detail.html?id=6097309&rut=28b5ec3913fdbc59c2bdd8a3859aa572c2adedb53093f7f6040cea35a9ee91dc', 'type': 'ddg', 'title': '自建数据中心互联：从野蛮生长到架构优化-百度开发者中心'}
