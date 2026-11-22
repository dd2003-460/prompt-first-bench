# N148: LFU 增益上限工作点 1（理想稳态，无更新）：假设负载完全静态，无对象更新，且 LFU 计数器无限精度。此时 LFU 驻留集合严格为 Top-K 对象，其中 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

LFU 增益上限工作点 1（理想稳态，无更新）：假设负载完全静态，无对象更新，且 LFU 计数器无限精度。此时 LFU 驻留集合严格为 Top-K 对象，其中 K 满足 Σ size_i <= 128GB。由于 ρ=-0.3，Top-K 对象平均大小小于全局平均。H_lfu_max = Σ_{i=1}^{K} (req_i * size_i) / Total_Bytes。基于 N39 和 N40，此工作点下 ΔH_lfu ≈ 10%-12%，是理论上限。

## Corrected Claim

LFU 增益上限工作点 1（理想稳态，无更新）：假设负载完全静态，无对象更新，且 LFU 计数器无限精度。此时 LFU 驻留集合严格为 Top-K 对象，其中 K 满足 Σ size_i <= 128GB。由于 ρ=-0.3，Top-K 对象平均大小小于全局平均。H_lfu_max = Σ_{i=1}^{K} (req_i * size_i) / Total_Bytes。基于 N39 和 N40，此工作点下 ΔH_lfu ≈ 10%-12%，是理论上限。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU optimal cache hit rate static workload Pareto distribution
