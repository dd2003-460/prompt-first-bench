# N90: 选择偏差量化：'主动降价卖家'非随机样本，其降价概率 λ_reduce 与商品剩余价值 V_remain 负相关；若高价值商品降价概率 λ_high = 0.2

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

选择偏差量化：'主动降价卖家'非随机样本，其降价概率 λ_reduce 与商品剩余价值 V_remain 负相关；若高价值商品降价概率 λ_high = 0.2，低价值商品 λ_low = 0.6，则观察到的'降价后无咨询'群体中低价值商品占比将偏向 (0.6*V_low) / (0.2*V_high + 0.6*V_low)，导致对降价效果的估计产生方向性偏差，需引入倾向得分匹配(PSM)计算偏差幅度。

## Corrected Claim

选择偏差量化：'主动降价卖家'非随机样本，其降价概率 λ_reduce 与商品剩余价值 V_remain 负相关；若高价值商品降价概率 λ_high = 0.2，低价值商品 λ_low = 0.6，则观察到的'降价后无咨询'群体中低价值商品占比将偏向 (0.6*V_low) / (0.2*V_high + 0.6*V_low)，导致对降价效果的估计产生方向性偏差，需引入倾向得分匹配(PSM)计算偏差幅度。

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑依赖但基本正交：节点1负责模型设定与可行性检查，节点3负责匹配质量检验，节点2负责偏差量化与结论修正。然而，完备性不足，父节点明确指出了'观察到的群体中低价值商品占比偏向'这一具体的结构性偏差机制（Selection Bias Mechanism），但子节点仅提供了通用的PSM/IPW方法论，未具体说明如何量化或调整这种由λ_reduce与V_remain负相关导致的特定占比偏差（例如，未提及如何在PSM中具体处理V_remain作为核心混杂变量时的权重调整或敏感性分析）。此外，节点2中的偏差定义公式 E[Y|Reduce=1, NoConsult=1] - ... 实际上是在估计处理效应（ATE/ATT的变体），而非严格意义上的'选择偏差'本身（选择偏差通常指观察值与潜在结果期望之差），概念上略有混淆，但可视为操作化定义。）

## Search Query

Propensity score matching bias correction for self-selected price reduction
