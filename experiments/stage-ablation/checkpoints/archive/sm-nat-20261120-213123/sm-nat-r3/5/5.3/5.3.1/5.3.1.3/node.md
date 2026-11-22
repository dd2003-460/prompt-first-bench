# N147: ΔH_large 占总折损 ΔH 的 80% 以上需验证：ΔH_large/ΔH = [P_invalidate_large * S_byte_large/S_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N65

## Claim

ΔH_large 占总折损 ΔH 的 80% 以上需验证：ΔH_large/ΔH = [P_invalidate_large * S_byte_large/S_total] / [Σ_{all} P_invalidate_i * S_byte_i/S_total]，需分别计算大对象和小对象的 P_invalidate 及字节占比，通过 Pareto 分布积分求解比值，确认是否 >80%。

## Corrected Claim

ΔH_large 占总折损 ΔH 的比例需通过计算大对象和小对象的 P_invalidate 及字节占比，利用 Pareto 分布积分求解比值来验证，其是否超过 80% 取决于具体的对象大小分布和失效模型参数。

## Evidence

[质询]该陈述将‘ΔH_large 占比 >80%’描述为一个需要验证的待证命题，而非已确认的事实结论。在缺乏具体系统参数（如对象大小分布、失效概率模型）的情况下，无法从第一性原理直接推导出该比值必然大于80%，这属于依赖具体场景的经验性统计结论，而非普适逻辑真理。 | 逻辑公式自洽，但‘>80%’为经验性阈值，非第一性原理可推导的数学恒等式；检索无可用来源支持该具体数值结论，故降级为定性表述。

## Search Query

cache invalidation contribution large vs small objects Pareto
