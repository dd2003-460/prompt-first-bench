# N109: 基于N58推导的无截断最大对象大小 M_max ≈ 34.7 MB，验证 s_max=1GB 截断假设的矛盾：由于 34.7 MB < 1 GB，Pareto(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

基于N58推导的无截断最大对象大小 M_max ≈ 34.7 MB，验证 s_max=1GB 截断假设的矛盾：由于 34.7 MB < 1 GB，Pareto(α=1.1, N=10^5) 分布的自然尾部远低于 1GB，因此 s_max=1GB 并非分布截断点，而是人为设定的物理上限；若强行截断于 1GB，则尾部概率 P(S > 34.7MB) 应为 0，而非 N33 中计算的 25.1%（该计算错误地假设了无限支撑或不同的 s_min）。

## Corrected Claim

基于N58推导的无截断最大对象大小 M_max ≈ 34.7 MB，验证 s_max=1GB 截断假设的矛盾：由于 34.7 MB < 1 GB，Pareto(α=1.1, N=10^5) 分布的自然尾部远低于 1GB，因此 s_max=1GB 并非分布截断点，而是人为设定的物理上限；若强行截断于 1GB，则尾部概率 P(S > 34.7MB) 应为 0，而非 N33 中计算的 25.1%（该计算错误地假设了无限支撑或不同的 s_min）。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布尾部概率计算与截断假设的逻辑推导自洽，数值量级合理。
