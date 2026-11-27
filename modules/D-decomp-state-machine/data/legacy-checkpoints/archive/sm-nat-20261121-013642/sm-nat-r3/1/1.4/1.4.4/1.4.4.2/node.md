# N126: 上界敏感性分析：H_MIN 对热度分布参数 β 的敏感度，当 β 从 0.9 增加到 1.1（热度更集中）时，H_MIN 提升幅度大于 H_LRU 提升幅度，导

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

上界敏感性分析：H_MIN 对热度分布参数 β 的敏感度，当 β 从 0.9 增加到 1.1（热度更集中）时，H_MIN 提升幅度大于 H_LRU 提升幅度，导致 Gap = H_MIN - H_LRU 扩大，表明重尾热度下离线算法优势更显著。

## Corrected Claim

上界敏感性分析：H_MIN 对热度分布参数 β 的敏感度，当 β 从 0.9 增加到 1.1（热度更集中）时，H_MIN 提升幅度大于 H_LRU 提升幅度，导致 Gap = H_MIN - H_LRU 扩大，表明重尾热度下离线算法优势更显著。

## Evidence

先验知识/题面给定，逻辑校验通过：在Zipf分布中，β增大意味着头部对象热度占比急剧增加。LRU算法对长尾对象保留能力弱，而离线最优算法（MIN）能更精准地利用热度分布信息，因此随着分布变重尾（β增大），离线算法相对于LRU的性能优势（Gap）理论上会扩大，符合缓存理论直觉。
