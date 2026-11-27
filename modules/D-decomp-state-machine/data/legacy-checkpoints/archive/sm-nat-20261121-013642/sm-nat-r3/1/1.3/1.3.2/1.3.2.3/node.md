# N115: 工作点1（高热度高字节权重）：假设缓存策略完美保留字节流量前 10% 的对象，此时 |Cache| 中对象平均大小 E[s|Cache] ≈ 5 * E[s|g

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37, N38, N39

## Claim

工作点1（高热度高字节权重）：假设缓存策略完美保留字节流量前 10% 的对象，此时 |Cache| 中对象平均大小 E[s|Cache] ≈ 5 * E[s|global]，平均频率 E[r|Cache] ≈ 100 * E[r|global]，分子 Σ(r*s) ≈ 0.9 * Total_Bytes。此工作点代表 LFU/字节加权策略的理论上限，用于对比 LRU 的实际性能差距。

## Corrected Claim

工作点1（高热度高字节权重）：假设缓存策略完美保留字节流量前 10% 的对象，此时 |Cache| 中对象平均大小 E[s|Cache] ≈ 5 * E[s|global]，平均频率 E[r|Cache] ≈ 100 * E[r|global]，分子 Σ(r*s) ≈ 0.9 * Total_Bytes。此工作点代表 LFU/字节加权策略的理论上限，用于对比 LRU 的实际性能差距。

## Evidence

先验知识/题面给定，逻辑校验通过
