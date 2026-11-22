# N215: 在截断 Pareto(α=1.1, s_min=1KB, s_max=100MB) 且独立假设下，LRU 流体模型命中率公式 H_LRU(C) = 1 - ∫_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75, N76, N77

## Claim

在截断 Pareto(α=1.1, s_min=1KB, s_max=100MB) 且独立假设下，LRU 流体模型命中率公式 H_LRU(C) = 1 - ∫_{s > C/K} (1-F(s)) dR(s) 的解析解与蒙特卡洛仿真结果的绝对误差为 1.2% (基于 10,000 次独立仿真均值)

## Corrected Claim

在截断 Pareto(α=1.1, s_min=1KB, s_max=100MB) 且独立假设下，LRU 流体模型命中率公式 H_LRU(C) = 1 - ∫_{s > C/K} (1-F(s)) dR(s) 的解析解与蒙特卡洛仿真结果存在较小误差（具体数值需依据特定仿真配置确定）。

## Evidence

[质询]该陈述包含具体的经验性数值（1.2%误差）和特定的仿真参数（10,000次），属于经验事实而非第一性原理可推导的数学恒等式。在缺乏外部来源支持的情况下，无法验证该具体数值是否准确，可能存在仿真设置偏差或统计波动导致的误差范围不同。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LRU fluid model hit rate error truncated Pareto distribution simulation
