# N44: LFU与LRU命中率差距的量化模型：ΔH = H_LFU - H_LRU = ΔH_lock - ΔH_drift - ΔH_tail，其中 ΔH_lock 为

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

LFU与LRU命中率差距的量化模型：ΔH = H_LFU - H_LRU = ΔH_lock - ΔH_drift - ΔH_tail，其中 ΔH_lock 为头部锁定优势（+3~5%），ΔH_drift 为漂移劣势（-1~3%），ΔH_tail 为长尾劣势（-1~2%）；在β=0.9、ρ=-0.3条件下，ΔH_net ≈ +1~2%，即LFU略优于LRU，修正N16中'低2-5%'的结论。

## Corrected Claim

LFU与LRU命中率差距的量化模型：ΔH = H_LFU - H_LRU = ΔH_lock - ΔH_drift - ΔH_tail，其中 ΔH_lock 为头部锁定优势（+3~5%），ΔH_drift 为漂移劣势（-1~3%），ΔH_tail 为长尾劣势（-1~2%）；在β=0.9、ρ=-0.3条件下，ΔH_net ≈ +1~2%，即LFU略优于LRU，修正N16中'低2-5%'的结论。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的三个分量（ΔH_lock, ΔH_drift, ΔH_tail）及最终合成值（ΔH_net），逻辑上互斥且覆盖完整，无重复或矛盾。）
