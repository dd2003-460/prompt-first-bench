# N66: 量化负相关对命中率下界的修正项 δ_ρ 的数值：在β=0.9和α=1.1条件下，ρ=-0.3使得字节命中率 H_byte 相比独立假设下的 H_byte_ind

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

量化负相关对命中率下界的修正项 δ_ρ 的数值：在β=0.9和α=1.1条件下，ρ=-0.3使得字节命中率 H_byte 相比独立假设下的 H_byte_independent 提升约 2-4 个百分点，因为小对象被更频繁访问且占用更少缓存空间。

## Corrected Claim

在β=0.9和α=1.1条件下，ρ=-0.3使得字节命中率 H_byte 相比独立假设下的 H_byte_independent 有所提升，因为小对象被更频繁访问且占用更少缓存空间。

## Evidence

[质询]该陈述包含具体的经验数值（2-4个百分点），属于经验事实而非第一性原理可推导的数学恒等式。在缺乏具体缓存模型参数（如对象大小分布、缓存容量、访问模式细节）的情况下，仅凭相关性系数ρ=-0.3无法严格推导出确切的命中率提升幅度，且不同模型下该数值可能波动较大。 | 经验事实，逻辑自洽（负相关确实倾向于提升小对象命中率从而提升整体命中率），但缺来源支持且数值具体性无法通过第一性原理严格验证。

## Search Query

impact of size-popularity correlation on cache byte hit rate zipf pareto
