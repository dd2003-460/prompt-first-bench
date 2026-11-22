# N121: 确定蒙特卡洛模拟中负相关联合分布的采样方法：使用 Gaussian Copula 或 Vine Copula 生成 r_i 和 s_i 的联合样本，确保边际分布

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N45

## Claim

确定蒙特卡洛模拟中负相关联合分布的采样方法：使用 Gaussian Copula 或 Vine Copula 生成 r_i 和 s_i 的联合样本，确保边际分布服从 Pareto(β=0.9) 和 Pareto(α=1.1)，且 Pearson 相关系数 ρ=-0.3；验证采样后的样本统计量（均值、方差、相关性）是否符合理论预期，以排除模拟偏差对 ΔH 估计的影响。

## Corrected Claim

确定蒙特卡洛模拟中负相关联合分布的采样方法：使用 Gaussian Copula 或 Vine Copula 生成 r_i 和 s_i 的联合样本，确保边际分布服从 Pareto(β=0.9) 和 Pareto(α=1.1)，且 Pearson 相关系数 ρ=-0.3；验证采样后的样本统计量（均值、方差、相关性）是否符合理论预期，以排除模拟偏差对 ΔH 估计的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian/Vine Copula 是生成具有指定相关结构（如 Pearson ρ=-0.3）且保持指定边际分布（Pareto）联合样本的标准且逻辑自洽的方法；验证样本统计量以排除模拟偏差也是蒙特卡洛模拟的标准质量控制步骤。
