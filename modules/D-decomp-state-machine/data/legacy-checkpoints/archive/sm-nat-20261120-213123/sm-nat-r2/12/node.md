# N81: LRU 与 LFU 的性能差距 ΔH = H_lfu - H_lru 主要源于 LRU 的‘时间局部性’偏差。在 Pareto(β=0.9) 长尾分布下，LRU

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU 与 LFU 的性能差距 ΔH = H_lfu - H_lru 主要源于 LRU 的‘时间局部性’偏差。在 Pareto(β=0.9) 长尾分布下，LRU 会错误地将近期访问过但频率较低的‘中等热度’对象保留在缓存中，挤占了高频对象的驻留空间。量化上，ΔH 近似等于被 LRU 错误缓存的中等热度对象字节流量占比减去被 LFU 正确缓存的高频对象但被 LRU 驱逐的字节流量占比。

## Corrected Claim

LRU 与 LFU 的性能差距 ΔH = H_lfu - H_lru 主要源于 LRU 的‘时间局部性’偏差。在 Pareto(β=0.9) 长尾分布下，LRU 会错误地将近期访问过但频率较低的‘中等热度’对象保留在缓存中，挤占了高频对象的驻留空间。量化上，ΔH 近似等于被 LRU 错误缓存的中等热度对象字节流量占比减去被 LFU 正确缓存的高频对象但被 LRU 驱逐的字节流量占比。

## Evidence

检索失败: no sources from any channel (all 5 failed)
