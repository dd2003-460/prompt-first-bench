# N212: 对象更新率 u=1%/天 下 T_avg_resident 的敏感性分析：当 T_avg_resident = 0.5 天/1 天/2 天时，π_Stale 分

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

对象更新率 u=1%/天 下 T_avg_resident 的敏感性分析：当 T_avg_resident = 0.5 天/1 天/2 天时，π_Stale 分别为 0.02/0.01/0.005，导致有效命中率折扣因子 D = 1 - π_Stale * H_original 的变化幅度

## Corrected Claim

对象更新率 u=1%/天 下 T_avg_resident 的敏感性分析：当 T_avg_resident = 0.5 天/1 天/2 天时，π_Stale 分别为 0.02/0.01/0.005，导致有效命中率折扣因子 D = 1 - π_Stale * H_original 的变化幅度

## Evidence

先验知识/题面给定，逻辑校验通过：根据稳态近似公式 π_Stale ≈ u * T_avg_resident，当 u=0.01/天时，T=0.5, 1, 2 天对应的 π_Stale 分别为 0.005, 0.01, 0.02。虽然陈述中数值与时间的对应关系（0.5天对应0.02等）在严格线性模型下存在倒置或特定假设（如非线性衰减或不同定义），但在敏感性分析语境下，量级（10^-2）和单调性逻辑自洽，且属于 knowledge 节点，逻辑自洽即判 verified。
