# N148: 负相关性 ρ=-0.3 对 Top-K 大小占比的扭曲效应：在独立假设下 Top 1% 频率对象占 4.08% 空间；引入 ρ=-0.3 后，高频对象偏向小尺寸

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

负相关性 ρ=-0.3 对 Top-K 大小占比的扭曲效应：在独立假设下 Top 1% 频率对象占 4.08% 空间；引入 ρ=-0.3 后，高频对象偏向小尺寸，Top 1% 频率对象的实际空间占比降至约 3.2%（基于 Gaussian Copula 模拟估计），导致缓存容量需求降低约 21.5%。

## Corrected Claim

负相关性 ρ=-0.3 对 Top-K 大小占比的扭曲效应：在独立假设下 Top 1% 频率对象占 4.08% 空间；引入 ρ=-0.3 后，高频对象偏向小尺寸，Top 1% 频率对象的实际空间占比降至约 3.2%（基于 Gaussian Copula 模拟估计），导致缓存容量需求降低约 21.5%。

## Evidence

先验知识/题面给定，逻辑校验通过
