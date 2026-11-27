# N85: Belady's MIN 算法的理论上限 H_MIN 与 LRU 下界 H_LRU 的差距 Gap = H_MIN - H_LRU 在重尾分布下通常大于 10 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N28

## Claim

Belady's MIN 算法的理论上限 H_MIN 与 LRU 下界 H_LRU 的差距 Gap = H_MIN - H_LRU 在重尾分布下通常大于 10 个百分点，因为 MIN 算法能全局最优地保留高 r_i/s_i 比值的对象，而 LRU 仅依赖时间局部性

## Corrected Claim

Belady's MIN 算法的理论上限 H_MIN 与 LRU 下界 H_LRU 的差距 Gap = H_MIN - H_LRU 在重尾分布下通常显著，因为 MIN 算法能全局最优地保留高 r_i/s_i 比值的对象，而 LRU 仅依赖时间局部性

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中的三个核心组件：H_MIN的具体数值及依据、H_LRU的具体数值及依据、以及Gap的计算结果及原因分析。三者逻辑独立，无重复或矛盾，且共同完整覆盖了父节点关于差距大小及其成因的描述。）

## Search Query

Belady MIN algorithm vs LRU performance gap heavy-tailed workload
