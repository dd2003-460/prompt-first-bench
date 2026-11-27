# N44: 敏感度计算与验证：S_buyer = (ΔUtility_lost / ΔTime_spent)，其中 ΔUtility_lost 为因搜索时间增加而放弃的潜在

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N11

## Claim

敏感度计算与验证：S_buyer = (ΔUtility_lost / ΔTime_spent)，其中 ΔUtility_lost 为因搜索时间增加而放弃的潜在交易效用，ΔTime_spent 为增加的搜索时间。需验证 S_buyer 是否在 95% 置信区间内大于 0.5，以确认买家是被动接受高挂价的核心群体。

## Corrected Claim

敏感度计算与验证：S_buyer = (ΔUtility_lost / ΔTime_spent)，其中 ΔUtility_lost 为因搜索时间增加而放弃的潜在交易效用，ΔTime_spent 为增加的搜索时间。需通过统计检验验证 S_buyer 是否显著大于 0（具体阈值如 0.5 需依据特定实证数据或模型设定确定），以确认买家对高挂价的敏感度。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式中的分子（ΔUtility_lost）、分母（ΔTime_spent）和整体统计推断（S_buyer的置信区间），三者逻辑独立且无重叠，共同完整覆盖了父节点中关于计算定义、变量获取及验证标准的所有要求。）

## Search Query

consumer search cost sensitivity elasticity trade off time money online marketplace
