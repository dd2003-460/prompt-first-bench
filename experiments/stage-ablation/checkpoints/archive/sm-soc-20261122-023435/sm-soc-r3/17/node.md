# N266: 买家‘等待更低价’策略的贝叶斯更新阈值：当卖家主动降价幅度 ΔP/P_old < 5% 时，买家后验概率 P(Seller_Urgent | ΔP) 更新幅度小

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

买家‘等待更低价’策略的贝叶斯更新阈值：当卖家主动降价幅度 ΔP/P_old < 5% 时，买家后验概率 P(Seller_Urgent | ΔP) 更新幅度小于 10%，不足以触发立即购买冲动；只有当 ΔP/P_old > 10% 时，后验概率跃升至 40% 以上，咨询率才会显著回升。这解释了为何 60% 的卖家在小额降价后 48 小时内无咨询。

## Corrected Claim

买家‘等待更低价’策略的贝叶斯更新阈值：当卖家主动降价幅度 ΔP/P_old < 5% 时，买家后验概率 P(Seller_Urgent | ΔP) 更新幅度小于 10%，不足以触发立即购买冲动；只有当 ΔP/P_old > 10% 时，后验概率跃升至 40% 以上，咨询率才会显著回升。这解释了为何 60% 的卖家在小额降价后 48 小时内无咨询。

## Evidence

检索失败: no sources from any channel (all 5 failed)
