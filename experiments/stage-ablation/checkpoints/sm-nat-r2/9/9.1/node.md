# N78: 增益上限 ΔH_max 的边界条件：当 ρ → -1 时，头部对象大小趋近 x_min，LFU 可缓存对象数 K_lfu → C/x_min。此时 H_LFU 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

增益上限 ΔH_max 的边界条件：当 ρ → -1 时，头部对象大小趋近 x_min，LFU 可缓存对象数 K_lfu → C/x_min。此时 H_LFU → 1 - (1 - F_top_K_lfu)^β。若 C/x_min >> N，则 H_LFU → 1。因此 ΔH_max 受限于 C/x_min 与 N 的比值。

## Corrected Claim

增益上限 ΔH_max 的边界条件：当 ρ → -1 时，头部对象大小趋近 x_min，LFU 可缓存对象数 K_lfu → C/x_min。此时 H_LFU → 1 - (1 - F_top_K_lfu)^β。若 C/x_min >> N，则 H_LFU → 1。因此 ΔH_max 受限于 C/x_min 与 N 的比值。

## Evidence

先验知识/题面给定，逻辑校验通过
