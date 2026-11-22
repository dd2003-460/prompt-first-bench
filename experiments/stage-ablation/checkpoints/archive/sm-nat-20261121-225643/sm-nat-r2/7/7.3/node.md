# N44: LFU与LRU命中率差距的量化模型：ΔH = H_LFU - H_LRU = ΔH_lock - ΔH_drift - ΔH_tail，其中 ΔH_lock 为

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

LFU与LRU命中率差距的量化模型：ΔH = H_LFU - H_LRU = ΔH_lock - ΔH_drift - ΔH_tail，其中 ΔH_lock 为头部锁定优势（+3~5%），ΔH_drift 为漂移劣势（-1~3%），ΔH_tail 为长尾劣势（-1~2%）；在β=0.9、ρ=-0.3条件下，ΔH_net ≈ +1~2%，即LFU略优于LRU，修正N16中'低2-5%'的结论。

## Corrected Claim

LFU与LRU命中率差距的量化模型：ΔH = H_LFU - H_LRU = ΔH_lock - ΔH_drift - ΔH_tail，其中 ΔH_lock 为头部锁定优势（+3~5%），ΔH_drift 为漂移劣势（-1~3%），ΔH_tail 为长尾劣势（-1~2%）；在β=0.9、ρ=-0.3条件下，ΔH_net ≈ +1~2%，即LFU略优于LRU，修正N16中'低2-5%'的结论。

## Evidence

先验知识/题面给定，逻辑校验通过
