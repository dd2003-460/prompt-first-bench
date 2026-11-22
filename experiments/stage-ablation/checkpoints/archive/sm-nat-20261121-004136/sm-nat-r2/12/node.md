# N80: 动态负载下 LFU 相对于 LRU 的潜在提升主要来源于对‘更新失效’的抵抗能力。若 LFU 能更有效地识别并重新加载高频对象（即使发生更新），其有效命中率提升

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

动态负载下 LFU 相对于 LRU 的潜在提升主要来源于对‘更新失效’的抵抗能力。若 LFU 能更有效地识别并重新加载高频对象（即使发生更新），其有效命中率提升上限受限于更新率 λ_update=1%/day 和对象热度分布的稳定性。在 1%/天 更新率下，LFU 相比 LRU 的最大潜在提升幅度估计在 0.1%-0.5% 之间，主要取决于 LFU 计数器刷新开销与 LRU 时间局部性失效的平衡。

## Corrected Claim

动态负载下 LFU 相对于 LRU 的潜在提升主要来源于对‘更新失效’的抵抗能力。若 LFU 能更有效地识别并重新加载高频对象（即使发生更新），其有效命中率提升上限受限于更新率 λ_update=1%/day 和对象热度分布的稳定性。在 1%/天 更新率下，LFU 相比 LRU 的最大潜在提升幅度估计在 0.1%-0.5% 之间，主要取决于 LFU 计数器刷新开销与 LRU 时间局部性失效的平衡。

## Evidence

检索失败: no sources from any channel (all 5 failed)
