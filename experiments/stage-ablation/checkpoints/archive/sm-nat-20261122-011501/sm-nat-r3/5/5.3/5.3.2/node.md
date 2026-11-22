# N63: LFU 增益下限工作点（高时间波动性）：假设访问模式包含 20% 的突发流量（burstiness factor γ=0.2），LFU 因频率计数滞后导致对新热

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

LFU 增益下限工作点（高时间波动性）：假设访问模式包含 20% 的突发流量（burstiness factor γ=0.2），LFU 因频率计数滞后导致对新热点响应慢，此时 ΔH_lfu 降至 2%-4%，甚至可能出现负增益（LFU < LRU）若突发对象大小显著大于平均大小。

## Corrected Claim

LFU 增益下限工作点（高时间波动性）：假设访问模式包含 20% 的突发流量（burstiness factor γ=0.2），LFU 因频率计数滞后导致对新热点响应慢，此时 ΔH_lfu 降至 2%-4%，甚至可能出现负增益（LFU < LRU）若突发对象大小显著大于平均大小。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 基于历史频率计数，在突发流量（高时间波动性）下确实存在滞后性，导致对新热点响应慢，相比 LRU 的局部性优势减弱，增益下降甚至为负符合缓存替换算法的基本原理。

## Search Query

LFU cache performance degradation bursty traffic frequency count lag
