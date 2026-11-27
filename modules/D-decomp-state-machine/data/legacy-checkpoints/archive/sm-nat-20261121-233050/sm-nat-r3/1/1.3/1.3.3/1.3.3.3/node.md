# N90: 相关性对 LRU vs LFU 差异的影响阈值判断：若 |J(ρ=0) - J(ρ=-0.3)| < 0.1，则相关性对命中率差异的影响小于 1 个百分点；否则

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

相关性对 LRU vs LFU 差异的影响阈值判断：若 |J(ρ=0) - J(ρ=-0.3)| < 0.1，则相关性对命中率差异的影响小于 1 个百分点；否则，需通过蒙特卡洛模拟计算加权命中率差异 ΔH = H_LFU - H_LRU，具体数值取决于 Jaccard Index 的变化幅度。

## Corrected Claim

相关性对 LRU vs LFU 差异的影响阈值判断：若 |J(ρ=0) - J(ρ=-0.3)| < 0.1，则相关性对命中率差异的影响小于 1 个百分点；否则，需通过蒙特卡洛模拟计算加权命中率差异 ΔH = H_LFU - H_LRU，具体数值取决于 Jaccard Index 的变化幅度。

## Evidence

先验知识/题面给定，逻辑校验通过
