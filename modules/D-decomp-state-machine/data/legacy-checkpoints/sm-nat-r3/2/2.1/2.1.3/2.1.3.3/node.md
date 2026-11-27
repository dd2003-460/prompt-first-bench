# N143: 在假设对象大小分布为对数正态分布而非 Pareto 的工作点下，E[S] 的计算公式不同，需重新计算分母项以量化分布假设对 LRU 字节命中率下界的影响。

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

在假设对象大小分布为对数正态分布而非 Pareto 的工作点下，E[S] 的计算公式不同，需重新计算分母项以量化分布假设对 LRU 字节命中率下界的影响。

## Corrected Claim

在假设对象大小分布为对数正态分布而非 Pareto 的工作点下，E[S] 的计算公式不同，需重新计算分母项以量化分布假设对 LRU 字节命中率下界的影响。

## Evidence

逻辑推导成立，来源未直接覆盖

## Search Query

log-normal distribution expectation calculation
