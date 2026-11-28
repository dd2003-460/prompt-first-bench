# N223: scipy.stats.ttest_ind 在 n=10^5 样本下的单线程 CPU 基准耗时为 3.2ms ± 0.5ms（基于 Intel i7-12700

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N66

## Claim

scipy.stats.ttest_ind 在 n=10^5 样本下的单线程 CPU 基准耗时为 3.2ms ± 0.5ms（基于 Intel i7-12700 @ 3.6GHz, AVX2 enabled），内存峰值占用为 64MB（float64 存储开销）

## Corrected Claim

scipy.stats.ttest_ind 在 n=10^5 样本下的单线程 CPU 基准耗时约为毫秒级（具体数值取决于硬件与软件环境），内存峰值占用主要受 float64 数据存储开销影响。

## Evidence

[质询]具体硬件环境（i7-12700 @ 3.6GHz）下的精确耗时（3.2ms）和内存峰值（64MB）属于高度依赖具体实现细节、编译器优化及系统状态的微观性能指标，无法从第一性原理推导，且不同构建版本间可能存在显著差异。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

scipy.stats.ttest_ind benchmark n=100000 latency memory usage float64
