# N34: 对象在 LRU 队列中的平均驻留时间 T_resident 近似等于缓存容量 C 除以 LRU 驱逐速率 R_evict (T_resident ≈ C / R

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

对象在 LRU 队列中的平均驻留时间 T_resident 近似等于缓存容量 C 除以 LRU 驱逐速率 R_evict (T_resident ≈ C / R_evict)，其中 C=128GB，R_evict 为稳态下每秒被替换出的对象总字节数。

## Corrected Claim

对象在 LRU 队列中的平均驻留时间 T_resident 近似等于缓存容量 C 除以 LRU 驱逐速率 R_evict (T_resident ≈ C / R_evict)，其中 C=128GB，R_evict 为稳态下每秒被替换出的对象总字节数。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同假设参数（MissRate）下的具体数值实例，而非对父节点概念的独立分解。虽然三个场景（高/中/低命中率）在逻辑上不冲突（正交），但它们高度冗余，因为结构完全相同，仅变量取值不同。此外，父节点描述的是一个通用的近似关系，子节点却引入了具体的数值假设（如5000万次/天），导致分解偏离了通用原理，且未涵盖该关系成立的物理前提（如稳态假设、字节守恒），因此不完备。）
