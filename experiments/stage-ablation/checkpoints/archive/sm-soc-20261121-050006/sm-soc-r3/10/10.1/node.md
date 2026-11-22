# N349: 卖家损失厌恶系数 λ_loss 的 Beta(4, 2) 分布参数应通过平台历史成交数据中的挂价偏差分布拟合校准，例如若 P_ask/P_ref 的偏度为 0.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N113

## Claim

卖家损失厌恶系数 λ_loss 的 Beta(4, 2) 分布参数应通过平台历史成交数据中的挂价偏差分布拟合校准，例如若 P_ask/P_ref 的偏度为 0.5，则 λ_loss 的均值和标准差需重新估计，而非直接使用理论值。

## Corrected Claim

卖家损失厌恶系数 λ_loss 的分布参数（如 Beta 分布）通常建议通过平台历史成交数据中的挂价偏差分布进行拟合校准，以反映实际市场行为，而非仅依赖理论假设值。

## Evidence

[质询]该陈述属于具体的工程实践建议（经验事实），声称特定的分布参数（Beta(4,2)）应通过特定的数据指标（挂价偏差偏度）进行校准，这并非第一性原理可推导的数学或物理定律，且缺乏通用的行业标准或理论共识支持这一特定的映射关系（偏度0.5直接对应Beta参数重估）。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该具体校准方法非通用公理）

## Search Query

seller loss aversion coefficient estimation C2C market price premium distribution
