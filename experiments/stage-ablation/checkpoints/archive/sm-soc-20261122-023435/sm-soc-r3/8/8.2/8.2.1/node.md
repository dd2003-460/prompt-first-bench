# N232: 卖家平均决策周期 T_seller 的统计分布：T_seller 通常服从对数正态分布，均值 μ ≈ 48h，标准差 σ ≈ 24h。T_penalty = 3

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N75

## Claim

卖家平均决策周期 T_seller 的统计分布：T_seller 通常服从对数正态分布，均值 μ ≈ 48h，标准差 σ ≈ 24h。T_penalty = 3 * σ_T_seller = 72h 对应于 99.7% 的卖家决策周期上限，确保绝大多数卖家在惩罚前已做出降价或下架决策。

## Corrected Claim

卖家平均决策周期 T_seller 通常服从对数正态分布。T_penalty 通常设定为 3 * σ_T_seller，以覆盖约 99.7% 的卖家决策周期上限，确保绝大多数卖家在惩罚前已做出决策。具体均值和标准差需根据实际市场数据确定。

## Evidence

[质询]该陈述包含具体的经验统计参数（均值48h、标准差24h），属于经验事实而非第一性原理可推导内容；且参考来源全部缺失，无法验证这些具体数值的真实性或来源可靠性。 | 经验事实，逻辑自洽（3σ对应99.7%符合正态分布性质，对数正态分布常用于描述时间周期），但缺来源支持具体数值。

## Search Query

seller decision cycle time distribution second-hand platform
