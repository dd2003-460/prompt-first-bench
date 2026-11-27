# N225: LFU增益估算的基准工作点（ρ=0）：假设K=128，F与L平均大小均为1MB，H_LFU/H_LRU≈1.0，ΔH≈0%，代表无负相关时的零增益基准。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

LFU增益估算的基准工作点（ρ=0）：假设K=128，F与L平均大小均为1MB，H_LFU/H_LRU≈1.0，ΔH≈0%，代表无负相关时的零增益基准。

## Corrected Claim

LFU增益估算的基准工作点（ρ=0）：假设K=128，F与L平均大小均为1MB，H_LFU/H_LRU≈1.0，ΔH≈0%，代表无负相关时的零增益基准。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU与LRU在无负相关（ρ=0）时性能趋同，H_LFU/H_LRU≈1.0及ΔH≈0%符合算法理论基准定义，数值量级合理。
