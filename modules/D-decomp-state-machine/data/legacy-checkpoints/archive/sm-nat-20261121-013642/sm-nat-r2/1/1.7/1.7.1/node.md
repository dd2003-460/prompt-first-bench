# N49: LFU 与 LRU 的字节命中率差值 ΔH 可分解为集合对称差项：ΔH = (B_LFU_only - B_LRU_only) / R_total_bytes，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

LFU 与 LRU 的字节命中率差值 ΔH 可分解为集合对称差项：ΔH = (B_LFU_only - B_LRU_only) / R_total_bytes，其中 B_LFU_only 为仅在 LFU 缓存中且被请求的字节量，B_LRU_only 为仅在 LRU 缓存中且被请求的字节量

## Corrected Claim

LFU 与 LRU 的字节命中率差值 ΔH 可分解为集合对称差项：ΔH = (B_LFU_only - B_LRU_only) / R_total_bytes，其中 B_LFU_only 为仅在 LFU 缓存中且被请求的字节量，B_LRU_only 为仅在 LRU 缓存中且被请求的字节量

## Evidence

先验知识/题面给定，逻辑校验通过
