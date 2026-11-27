# N143: ΔCache 的字节流量占比工作点 1（大对象主导）：ΔCache 中对象主要为低频大对象，其字节流量占比 P_bytes_diff = (Σ_{i∈ΔCach

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

ΔCache 的字节流量占比工作点 1（大对象主导）：ΔCache 中对象主要为低频大对象，其字节流量占比 P_bytes_diff = (Σ_{i∈ΔCache} r_i * s_i) / R_bytes_total，在 α=1.1 重尾分布下，该值通常 < 5%，表明 LFU 与 LRU 的缓存差异对总字节命中率影响有限。

## Corrected Claim

ΔCache 的字节流量占比工作点 1（大对象主导）：ΔCache 中对象主要为低频大对象，其字节流量占比 P_bytes_diff = (Σ_{i∈ΔCache} r_i * s_i) / R_bytes_total，在 α=1.1 重尾分布下，该值通常 < 5%，表明 LFU 与 LRU 的缓存差异对总字节命中率影响有限。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache set difference byte traffic ratio
