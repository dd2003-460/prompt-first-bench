# N84: 自建POP点带宽采购最小单位与闲置成本：运营商通常以1Gbps为最小购买单元或提供100M/1G/10G套餐；若每点仅购1Gbps带宽（月费约¥5,000-15

- **status**: degraded
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

[质询]具体数值（如1Gbps月费¥5,000-15,000、10Gbps月费¥50,000-100,000）属于高度依赖地区、运营商及合同谈判的经验性市场数据，缺乏通用标准，且参考来源未提供具体价格佐证，存在数值偏差风险。 | 来源[2]提及POP点架构与成本平衡，间接支持自建POP点的业务场景；但具体带宽单价及闲置率计算属于经验事实，逻辑自洽但缺乏直接来源支持具体数值。

## Search Query

China telecom edge POP bandwidth pricing 1Gbps 10Gbps monthly cost 2024

## Retrieval Sources

- {'url': 'https://b2bwiki.baidu.com/article/aw_56bcad9c6793fff31e116a6a028328dc&rut=c439a1f5a23c5d0155dc849c8652a3b5296bf1fbc574eb875241aeece4f2eb2e', 'type': 'ddg', 'title': '闲置宽带资源化改造：采购成本测算与设备选型要点'}
- {'url': 'https://developer.baidu.com/article/detail.html?id=6097309&rut=28b5ec3913fdbc59c2bdd8a3859aa572c2adedb53093f7f6040cea35a9ee91dc', 'type': 'ddg', 'title': '自建数据中心互联：从野蛮生长到架构优化-百度开发者中心'}
