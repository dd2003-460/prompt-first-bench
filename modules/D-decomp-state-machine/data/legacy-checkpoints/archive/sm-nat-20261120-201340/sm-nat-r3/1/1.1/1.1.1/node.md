# N29: 在边缘CDN典型负载假设下，对象最小大小 s_min = 10KB，据此计算 Pareto(α=1.1) 的期望大小 E[S] = 1.1 * 10KB / (

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

在边缘CDN典型负载假设下，对象最小大小 s_min = 10KB，据此计算 Pareto(α=1.1) 的期望大小 E[S] = 1.1 * 10KB / (1.1 - 1) = 110KB。

## Corrected Claim

在边缘CDN典型负载假设下，对象最小大小 s_min = 10KB，据此计算 Pareto(α=1.1) 的期望大小 E[S] = 1.1 * 10KB / (1.1 - 1) = 110KB。

## Evidence

父节点级核验未通过：有冗余（子节点本质上是同一参数 s_min 在不同取值下的计算结果，属于参数敏感性分析而非正交的逻辑分支。虽然覆盖了上下界，但结构上存在冗余，应合并为单一节点或参数化描述。）

## Search Query

typical edge CDN object size distribution minimum size
