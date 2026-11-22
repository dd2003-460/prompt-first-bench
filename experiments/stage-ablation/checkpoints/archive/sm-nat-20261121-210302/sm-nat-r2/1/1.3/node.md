# N7: LFU 相比 LRU 的最大理论增益 ΔH_max = H_LFU - H_LRU，取决于热度分布的重尾程度（β=0.9）与 LRU 的‘新鲜度偏差’程度，需通

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LFU 相比 LRU 的最大理论增益 ΔH_max = H_LFU - H_LRU，取决于热度分布的重尾程度（β=0.9）与 LRU 的‘新鲜度偏差’程度，需通过模拟或解析近似计算

## Corrected Claim

LFU 相比 LRU 的最大理论增益 ΔH_max = H_LFU - H_LRU，取决于热度分布的重尾程度（β=0.9）与 LRU 的‘新鲜度偏差’程度，需通过模拟或解析近似计算

## Evidence

父节点级核验未通过：不完备（父节点明确包含两个核心依赖因素：1. 热度分布的重尾程度（β=0.9）；2. LRU 的‘新鲜度偏差’程度。此外，父节点还指出了计算方式（模拟或解析近似）。子节点仅覆盖了第一个因素（重尾分布下的热点集中度），完全缺失了对 LRU 新鲜度偏差的分析，也未涉及如何计算 ΔH_max 的方法论，因此不完备。）
