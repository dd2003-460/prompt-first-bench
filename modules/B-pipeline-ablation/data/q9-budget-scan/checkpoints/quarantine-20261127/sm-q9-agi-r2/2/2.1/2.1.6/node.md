# N55: FAISS 并发查询能力受限于 GIL（全局解释器锁）及内存争用；在 M1 Max 上，当并发查询数 N=2 时，P95 延迟约为 15-20ms；当 N=4 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13, N14, N15

## Claim

FAISS 并发查询能力受限于 GIL（全局解释器锁）及内存争用；在 M1 Max 上，当并发查询数 N=2 时，P95 延迟约为 15-20ms；当 N=4 时，由于内存带宽竞争，P95 延迟上升至 40-60ms；超过 N=4 后，排队效应导致延迟线性增长，不再适合高并发实时检索场景。

## Corrected Claim

FAISS 并发查询能力受限于 GIL 及内存带宽争用；在 M1 Max 上，随着并发查询数增加，P95 延迟会显著上升（例如从 N=2 到 N=4 可能翻倍以上），超过一定并发阈值后排队效应导致延迟线性增长，不适合高并发实时检索场景。

## Evidence

[质询]具体数值（15-20ms, 40-60ms）高度依赖数据集规模、向量维度、索引类型及硬件具体配置，缺乏上下文使得这些精确数值成为不可验证的经验断言；此外，GIL主要限制Python层并发，FAISS核心C++部分通常通过释放GIL实现多线程并行，将延迟上升完全归因于GIL和内存争用可能存在机制上的简化或偏差。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体性能数值无法从第一性原理推导）

## Search Query

FAISS concurrent queries M1 Max memory bandwidth contention latency increase
