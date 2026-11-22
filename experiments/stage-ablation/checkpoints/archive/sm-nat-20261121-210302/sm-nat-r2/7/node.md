# N21: LFU 相比 LRU 的提升上限受限于‘频率-大小’错配：当 β=0.9 且 ρ=-0.3 时，LFU 保留的热点对象平均大小 S_LFU_hot 显著小于 L

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LFU 相比 LRU 的提升上限受限于‘频率-大小’错配：当 β=0.9 且 ρ=-0.3 时，LFU 保留的热点对象平均大小 S_LFU_hot 显著小于 LRU 驱逐的平均大小 S_LRU_evict，提升百分点 Δ% ≈ (S_LRU_evict - S_LFU_hot)/S_LRU_evict * MissRate_LRU。

## Corrected Claim

LFU 相比 LRU 的提升上限受限于‘频率-大小’错配：当 β=0.9 且 ρ=-0.3 时，LFU 保留的热点对象平均大小 S_LFU_hot 显著小于 LRU 驱逐的平均大小 S_LRU_evict，提升百分点 Δ% ≈ (S_LRU_evict - S_LFU_hot)/S_LRU_evict * MissRate_LRU。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了父节点公式中的三个核心变量（S_LFU_hot, S_LRU_evict, Δ% 的上界），彼此独立且无重叠。虽然子节点3的公式形式与父节点略有不同（引入了 P_hot_bytes 修正项，使其成为更严谨的上界），但这属于对父节点‘量化上界’的具体展开，而非矛盾。所有关键组件均已覆盖。）
