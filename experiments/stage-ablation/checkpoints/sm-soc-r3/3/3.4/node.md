# N18: 最小干预方案：平台引入‘价格合理性标签’，当 P_ask > P_market × 1.2 时显示‘高于近期成交价 20%’警示，预期降低买家搜寻成本 C_se

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

最小干预方案：平台引入‘价格合理性标签’，当 P_ask > P_market × 1.2 时显示‘高于近期成交价 20%’警示，预期降低买家搜寻成本 C_search 10%-15%，但伤害卖家短期利润（Π_seller 下降 5%-10%）及平台广告收入（R_advertising 下降 3%-5%）。

## Corrected Claim

平台引入‘价格合理性标签’（当 P_ask > P_market × 1.2 时显示警示），预期通过降低信息不对称来降低买家搜寻成本，但可能因抑制高价成交或流量转化而损害卖家短期利润及平台广告收入。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上分别对应父节点中的三个独立后果（买家搜寻成本、卖家利润、平台广告收入），彼此正交且无冗余。然而，父节点明确包含‘触发阈值（P_ask > P_market × 1.2）’这一核心机制定义，子节点1仅进行了敏感性分析而未包含基础阈值的设定与逻辑验证，导致对父节点‘方案定义’部分的覆盖存在细微缺口。）

## Search Query

price reasonableness label intervention marketplace seller profit impact
