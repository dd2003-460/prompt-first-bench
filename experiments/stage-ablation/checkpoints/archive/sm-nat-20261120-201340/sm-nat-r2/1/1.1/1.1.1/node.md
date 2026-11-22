# N29: 在边缘CDN典型负载假设下，对象最小大小 s_min = 10KB，据此计算 Pareto(α=1.1) 的期望大小 E[S] = 1.1 * 10KB / (

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

在边缘CDN典型负载假设下，对象最小大小 s_min = 10KB，据此计算 Pareto(α=1.1) 的期望大小 E[S] = 1.1 * 10KB / (1.1 - 1) = 110KB。

## Corrected Claim

在边缘CDN典型负载假设下，对象最小大小 s_min = 10KB，据此计算 Pareto(α=1.1) 的期望大小 E[S] = 1.1 * 10KB / (1.1 - 1) = 110KB。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布期望公式 E[S] = α*s_min/(α-1) 代入 α=1.1, s_min=10KB 计算得 110KB，数学推导正确。

## Search Query

typical edge CDN object size distribution minimum size
