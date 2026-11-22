# N26: 在标准CDN边缘节点场景中，最小对象大小 x_min 的典型工程阈值为 1KB (1024 Bytes)，用于截断 Pareto(α=1.1) 分布以计算 E[

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

在标准CDN边缘节点场景中，最小对象大小 x_min 的典型工程阈值为 1KB (1024 Bytes)，用于截断 Pareto(α=1.1) 分布以计算 E[S] = 1.1/(0.1) * 1024 B = 11264 B ≈ 11.0 KB

## Corrected Claim

在标准CDN边缘节点场景中，最小对象大小 x_min 的典型工程阈值为 1KB (1024 Bytes)，用于截断 Pareto(α=1.1) 分布以计算 E[S] = 1.1/(0.1) * 1024 B = 11264 B ≈ 11.0 KB

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布截断期望公式 E[S] = α*x_min/(α-1) 在 α=1.1, x_min=1024 时计算结果为 11264 B，量级与工程常识相符。

## Search Query

typical minimum object size CDN edge node 1KB threshold
