# N121: LFU 与 Belady 差距下界（保守估计）：假设 LFU 能捕获 80% 的 Belady 最优性能，即 H_LFU ≈ 0.8 * H_Belady + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

LFU 与 Belady 差距下界（保守估计）：假设 LFU 能捕获 80% 的 Belady 最优性能，即 H_LFU ≈ 0.8 * H_Belady + 0.2 * H_LRU，则差距 H_Belady - H_LFU ≈ 0.2 * (H_Belady - H_LRU)，需基于 N46 和 N45 的结果计算具体百分点

## Corrected Claim

LFU 与 Belady 差距下界（保守估计）：假设 LFU 能捕获 80% 的 Belady 最优性能，即 H_LFU ≈ 0.8 * H_Belady + 0.2 * H_LRU，则差距 H_Belady - H_LFU ≈ 0.2 * (H_Belady - H_LRU)，需基于 N46 和 N45 的结果计算具体百分点

## Evidence

先验知识/题面给定，逻辑校验通过
