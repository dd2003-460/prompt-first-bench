# N78: 在给定参数下（N=100k, E[S]≈9.35KB, C=128GB），缓存容量约束为非绑定约束（Non-binding Constraint），因为存储所有

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在给定参数下（N=100k, E[S]≈9.35KB, C=128GB），缓存容量约束为非绑定约束（Non-binding Constraint），因为存储所有对象所需容量仅约 0.9GB，远小于 128GB。因此，LRU 的稳态字节命中率下界 H_LRU_lb 在静态无更新假设下应修正为 100% (1.0)，而非基于容量截断计算的 5.56%。

## Corrected Claim

在给定参数下（N=100k, E[S]≈9.35KB, C=128GB），缓存容量约束为非绑定约束（Non-binding Constraint），因为存储所有对象所需容量仅约 0.9GB，远小于 128GB。因此，LRU 的稳态字节命中率下界 H_LRU_lb 在静态无更新假设下应修正为 100% (1.0)，而非基于容量截断计算的 5.56%。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

LRU cache hit rate 100% when capacity exceeds working set size
