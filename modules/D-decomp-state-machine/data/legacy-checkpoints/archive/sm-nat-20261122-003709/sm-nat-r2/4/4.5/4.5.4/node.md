# N74: LFU相对LRU的理论优势窗口修正项δ_ρ，量化ρ=-0.3（热小冷大）对LFU保留策略的增强效应，公式为δ_ρ = ρ * (∂H/∂ρ)，其中∂H/∂ρ需通

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N20, N21, N22

## Claim

LFU相对LRU的理论优势窗口修正项δ_ρ，量化ρ=-0.3（热小冷大）对LFU保留策略的增强效应，公式为δ_ρ = ρ * (∂H/∂ρ)，其中∂H/∂ρ需通过蒙特卡洛模拟在ρ∈[-0.5, 0.5]区间内拟合得出，具体数值需联网查证或模拟计算。

## Corrected Claim

LFU相对LRU的理论优势窗口修正项δ_ρ通常量化为ρ与敏感度∂H/∂ρ的乘积，其中∂H/∂ρ需通过模拟或实验在特定ρ区间内拟合得出，具体数值依赖于工作负载特征。

## Evidence

[质询]该陈述包含具体的经验性数值（ρ=-0.3）和特定的工程实现细节（蒙特卡洛模拟拟合），属于经验事实而非第一性原理可推导的数学恒等式。在缺乏外部来源支持的情况下，无法验证该特定参数下的增强效应数值或公式的具体适用性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

LFU LRU performance difference negative correlation size popularity rho=-0.3 Monte Carlo simulation
