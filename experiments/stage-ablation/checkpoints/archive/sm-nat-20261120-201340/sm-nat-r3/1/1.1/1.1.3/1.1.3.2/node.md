# N87: 缓存覆盖率 Ratio 的临界工作点 C（严重不足假设）：若 s_min > 1.2MB，则 Ratio < 1，缓存无法容纳所有对象，LRU 稳态命中率将显著

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

缓存覆盖率 Ratio 的临界工作点 C（严重不足假设）：若 s_min > 1.2MB，则 Ratio < 1，缓存无法容纳所有对象，LRU 稳态命中率将显著低于 100%，且 LFU 优势开始显现（ΔH > 0），此场景需重新计算 k 值。

## Corrected Claim

缓存覆盖率 Ratio 的临界工作点 C（严重不足假设）：若 s_min > 1.2MB，则 Ratio < 1，缓存无法容纳所有对象，LRU 稳态命中率将显著低于 100%，且 LFU 优势开始显现（ΔH > 0），此场景需重新计算 k 值。

## Evidence

先验知识/题面给定，逻辑校验通过：当缓存容量小于最小对象尺寸（s_min > 1.2MB 且 Ratio < 1 意味着缓存无法容纳所有对象）时，LRU 必然无法达到 100% 命中率，且 LFU 在存在热点对象时通常优于 LRU，符合缓存替换算法的基本原理。
