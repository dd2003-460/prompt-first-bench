# N9: LFU 增益上限 = (H_LFU - H_LRU) * 100%，其中 H_LFU 假设按热度频率分配缓存空间，H_LRU 按最近访问分配；在热度 Paret

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LFU 增益上限 = (H_LFU - H_LRU) * 100%，其中 H_LFU 假设按热度频率分配缓存空间，H_LRU 按最近访问分配；在热度 Pareto(β=0.9) 下，LFU 对头部 10% 对象（占 90% 请求）的缓存保留率更高，增益上限 ≈ 5-15 个百分点 [待核验]

## Corrected Claim

LFU 增益上限 = (H_LFU - H_LRU) * 100%，其中 H_LFU 假设按热度频率分配缓存空间，H_LRU 按最近访问分配；在热度 Pareto(β=0.9) 下，LFU 对头部 10% 对象（占 90% 请求）的缓存保留率更高，增益上限 ≈ 5-15 个百分点 [待核验]

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别聚焦于 LFU 命中率模型、LRU 命中率模型以及两者差值（增益）的边界条件分析，逻辑上互不重叠且共同覆盖了父节点中公式定义的各个变量及修正逻辑。虽然子节点 3 综合了前两个节点的结论，但其核心贡献在于指出了父节点中‘5-15%’估计与‘K=N（容量充足）’前提之间的矛盾，属于必要的修正说明，而非简单冗余。）

## Search Query

LFU vs LRU hit rate Pareto distribution edge case
