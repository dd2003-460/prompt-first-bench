# N30: 数据不确定性标记规范：所有价格数据标记为 [Price: 2024-Q4 Est.]；所有性能基准（如MMLU分数）标记为 [Bench: Qwen3-27B 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

数据不确定性标记规范：所有价格数据标记为 [Price: 2024-Q4 Est.]；所有性能基准（如MMLU分数）标记为 [Bench: Qwen3-27B Report v1]；所有带宽/算力峰值标记为 [Spec: NVIDIA Official Datasheet]。对于多卡互联开销（N24中的15%-30%），标记为 [Est: Empirical Range]，需在最终推荐中说明该范围导致的性价比波动区间（例如：PCIe方案性价比可能比NVLink方案低20%-30%）。

## Corrected Claim

数据不确定性标记规范：所有价格数据标记为 [Price: 2024-Q4 Est.]；所有性能基准（如MMLU分数）标记为 [Bench: Qwen3-27B Report v1]；所有带宽/算力峰值标记为 [Spec: NVIDIA Official Datasheet]。对于多卡互联开销（N24中的15%-30%），标记为 [Est: Empirical Range]，需在最终推荐中说明该范围导致的性价比波动区间（例如：PCIe方案性价比可能比NVLink方案低20%-30%）。

## Evidence

检索失败: no sources from any channel (all 5 failed)
