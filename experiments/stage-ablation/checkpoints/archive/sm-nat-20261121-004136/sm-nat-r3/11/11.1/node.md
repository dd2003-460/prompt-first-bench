# N178: 静态负载下 LFU 相对 LRU 的理论提升幅度 Δ_H_static 的量化值：在容量充足（K_max >> N）且无更新失效的静态假设下，LRU 和 LFU

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79

## Claim

静态负载下 LFU 相对 LRU 的理论提升幅度 Δ_H_static 的量化值：在容量充足（K_max >> N）且无更新失效的静态假设下，LRU 和 LFU 均能缓存所有对象，命中率均为 100%。因此，Δ_H_static = H_LFU - H_LRU = 1.0 - 1.0 = 0%。LFU 的优势仅在 K_max < N 时存在，本题参数下该机制不触发。

## Corrected Claim

静态负载下 LFU 相对 LRU 的理论提升幅度 Δ_H_static 的量化值：在容量充足（K_max >> N）且无更新失效的静态假设下，LRU 和 LFU 均能缓存所有对象，命中率均为 100%。因此，Δ_H_static = H_LFU - H_LRU = 1.0 - 1.0 = 0%。LFU 的优势仅在 K_max < N 时存在，本题参数下该机制不触发。

## Evidence

先验知识/题面给定，逻辑校验通过：在缓存容量远大于对象总数（K_max >> N）且负载静态无失效的情况下，LRU和LFU均可容纳所有对象，命中率均为100%，差值为0，符合缓存算法基本逻辑。
