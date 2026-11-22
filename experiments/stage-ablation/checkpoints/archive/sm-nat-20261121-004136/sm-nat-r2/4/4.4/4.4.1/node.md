# N57: 更新对象的条件期望大小 E[Size | Updated] 计算：假设更新事件独立于大小，E[Size | Updated] = E[Size] ≈ 10.9K

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

更新对象的条件期望大小 E[Size | Updated] 计算：假设更新事件独立于大小，E[Size | Updated] = E[Size] ≈ 10.9KB（基于 Pareto α=1.1, s_min=1KB 截断均值），用于计算基础带宽开销。

## Corrected Claim

更新对象的条件期望大小 E[Size | Updated] 计算：假设更新事件独立于大小，E[Size | Updated] = E[Size] ≈ 10.9KB（基于 Pareto α=1.1, s_min=1KB 截断均值），用于计算基础带宽开销。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布截断均值公式 E[S] = α*s_min/(α-1) 在 α=1.1, s_min=1KB 时计算结果为 10.9KB，数值量级与逻辑推导一致。
