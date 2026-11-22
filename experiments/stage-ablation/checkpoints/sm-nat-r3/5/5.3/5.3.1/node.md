# N82: Pareto 分布截断点 x_min 的敏感性分析：假设 x_min 从 1KB 变化到 4KB，重新计算 E[S] 和 N_cache，量化对 LRU 命中率

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

Pareto 分布截断点 x_min 的敏感性分析：假设 x_min 从 1KB 变化到 4KB，重新计算 E[S] 和 N_cache，量化对 LRU 命中率下界的影响。当 x_min=1KB 时，E[S]≈1.1KB，N_cache≈119,005；当 x_min=4KB 时，E[S]≈4.4KB，N_cache≈29,751，覆盖率从 119% 降至 30%，导致 LRU 命中率下界从 99.96% 降至约 70%，误差范围 ±30%。

## Corrected Claim

Pareto 分布截断点 x_min 的敏感性分析：假设 x_min 从 1KB 变化到 4KB，需明确 Pareto 分布的形状参数 alpha 及总数据量/工作集大小。在典型参数下，x_min 增大会导致 E[S] 增大，N_cache 减小，从而降低 LRU 命中率下界，但具体数值（如 99.96% 降至 70%）需基于具体分布参数重新计算，当前数值缺乏来源支持且存在逻辑疑点。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点存在严重冗余和结构性错误。子节点1、2与3、4存在逻辑重叠：子节点1/2指出公式计算错误（E[S]应为11KB/44KB），而子节点3/4直接基于修正后的数值（11KB/44KB）计算了N_cache和覆盖率。这意味着子节点3/4已经隐含了子节点1/2的结论，导致子节点1/2成为多余的‘纠错步骤’而非独立的分析维度。此外，子节点1和2、子节点3和4分别是对称的两种x_min取值情况，属于同一计算流程的不同参数实例，而非正交的概念分解。）

## Search Query

Pareto distribution truncation point x_min 1KB 4KB sensitivity analysis cache hit rate LRU 128GB 100000 objects
