# N91: 移除高价排序权重后，成交周期延长的反事实推断值 ΔT_counterfactual，即 T_with_intervention - T_baseline，需满足

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N26

## Claim

移除高价排序权重后，成交周期延长的反事实推断值 ΔT_counterfactual，即 T_with_intervention - T_baseline，需满足 ΔT_counterfactual / T_baseline > 20% 才能支持 H3（平台驱动均衡），该阈值需通过自然实验数据验证。

## Corrected Claim

移除高价排序权重后，成交周期延长的反事实推断值 ΔT_counterfactual 需满足显著性检验（具体阈值如20%需依据特定自然实验数据或研究假设确定），以支持 H3（平台驱动均衡）。

## Evidence

[质询]该陈述中的具体阈值（20%）及特定的反事实推断公式属于经验性设定或特定研究假设，并非通用的第一性原理或数学公理，且参考来源中未包含任何关于此特定阈值或H3假设验证标准的信息，存在来源缺失风险。 | 逻辑上自洽（反事实推断定义清晰，阈值用于假设检验符合统计推断逻辑），但参考来源[1][2][3]均涉及量化交易策略、因子或数据清洗，与该特定平台均衡假设的验证阈值无关，属于经验事实且缺乏直接来源支持。

## Search Query

counterfactual transaction time increase after removing high price ranking weight

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2017381574597976552&rut=09c15e9ecb814470f0e8b0d9b8ebd39af6b9155cf358630b0d32e7ce5597f878', 'type': 'ddg', 'title': '10篇量化前沿论文讲透：从多因子选股、风险模型到高频交易，量化小白也能看懂的实战分析 - 知乎'}
- {'url': 'https://github.com/YungFuu/Cryptocurrency-trading-strategy-replication/blob/main/Part1%20%E8%B0%83%E7%94%A8%E6%95%B0%E6%8D%AEapi%EF%BC%8C%E6%95%B0%E6%8D%AE%E6%B8%85%E6%B4%97%E4%B8%8E%E5%A4%84%E7%90%86.md&rut=1b219fe998d731430457e402f2d449996897ed675d52143c0a46c9706f72d936', 'type': 'ddg', 'title': 'Cryptocurrency-trading-strategy-replication/Part1 调用数据 ... - GitHub'}
- {'url': 'https://zhuanlan.zhihu.com/p/2018451714001384703&rut=da46f17bb993600cb6696aa4223c0ffa39e93e6f28ced3a8fefb3be7f8f8c5dc', 'type': 'ddg', 'title': '经典cta因子拆解：从失效归因到策略迭代 - 知乎'}
