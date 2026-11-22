# N286: 后悔厌恶系数 eta 的个体差异分布：eta 并非固定值，而是服从 Beta 分布或正态分布 N(mu_eta, sigma_eta^2)。实证数据显示 mu_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94, N95, N96

## Claim

后悔厌恶系数 eta 的个体差异分布：eta 并非固定值，而是服从 Beta 分布或正态分布 N(mu_eta, sigma_eta^2)。实证数据显示 mu_eta ≈ 2.0，sigma_eta ≈ 0.5。只有当 eta > eta_threshold = C_search / (V_max - P_ask) 时，买家才会抑制重新搜索。在 P_ask = 1.2 P_ref 时，eta_threshold ≈ 0.8-1.2，意味着约 50-70% 的买家会因后悔厌恶而锁定。

## Corrected Claim

后悔厌恶系数 eta 存在个体差异，通常服从某种连续分布（如 Beta 或正态分布）。实证研究表明，后悔厌恶会显著抑制买家的重新搜索行为；当 P_ask 高于参考价格时，相当比例的买家（具体比例取决于 eta 的分布参数及市场条件）会因后悔厌恶而锁定当前选择。

## Evidence

[质询]该陈述包含具体的实证统计参数（mu_eta ≈ 2.0, sigma_eta ≈ 0.5）及特定的行为经济学模型阈值推导，属于经验事实。虽然逻辑框架（后悔厌恶导致搜索抑制）在理论上自洽，但具体的分布参数和百分比（50-70%）缺乏通用共识或标准文献支持，且不同实验环境下后悔厌恶系数的估计值差异较大，直接断言特定均值和标准差存在过度具体化的风险。 | source=knowledge，逻辑自洽（后悔厌恶确实会抑制搜索，阈值推导符合直觉），但具体数值（mu=2.0, sigma=0.5, 50-70%）属于经验事实，缺乏来源直接支持，且不同研究结果可能不一致，故降级为定性表述。

## Search Query

regret aversion coefficient distribution consumer choice experiments
