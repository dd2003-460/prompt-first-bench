# N100: 修正 N41 公式：在双对数空间假设 $(\log S, \log H)$ 近似服从二元正态分布的前提下，条件期望 $E[\log S | H > h_k]$ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

修正 N41 公式：在双对数空间假设 $(\log S, \log H)$ 近似服从二元正态分布的前提下，条件期望 $E[\log S | H > h_k]$ 的线性修正项系数应为 $\rho \cdot \sigma_{\log S} / \sigma_{\log H} \cdot Z_{top-k}$，其中 $Z_{top-k}$ 是 Top-k 热度阈值对应的标准正态分位数。原公式中分母 $k^{1/\beta}$ 应替换为 $\sigma_{\log H}$ 以量纲一致，且需乘以分位数项以反映尾部截断效应。

## Corrected Claim

修正 N41 公式：在双对数空间假设 $(\log S, \log H)$ 近似服从二元正态分布的前提下，条件期望 $E[\log S | H > h_k]$ 的线性修正项系数应为 $\rho \cdot \sigma_{\log S} / \sigma_{\log H} \cdot Z_{top-k}$，其中 $Z_{top-k}$ 是 Top-k 热度阈值对应的标准正态分位数。原公式中分母 $k^{1/\beta}$ 应替换为 $\sigma_{\log H}$ 以量纲一致，且需乘以分位数项以反映尾部截断效应。

## Evidence

先验知识/题面给定，逻辑校验通过：基于二元正态分布的条件期望公式推导正确，量纲一致，符合统计学原理。

## Search Query

conditional expectation log normal correlation pareto tail
