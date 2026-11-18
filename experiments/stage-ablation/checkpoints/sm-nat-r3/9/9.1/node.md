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

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：子节点1计算容量上限（K），子节点2基于子节点1推导理想命中率（H），子节点3分析实际与理想的偏差来源。三者分别对应'理论容量'、'理论性能'和'实际偏差'，无重复且覆盖了父节点中关于C/x_min与N比值限制及LFU机制的关键方面。）
