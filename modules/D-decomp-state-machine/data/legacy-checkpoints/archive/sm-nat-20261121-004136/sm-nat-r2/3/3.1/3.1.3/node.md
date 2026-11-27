# N45: LFU 完美区分假设的容量可行性校验：前 1,000 个最热对象的总大小 Sum_S_top1000 是否小于 128GB。若 Sum_S_top1000 > 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

LFU 完美区分假设的容量可行性校验：前 1,000 个最热对象的总大小 Sum_S_top1000 是否小于 128GB。若 Sum_S_top1000 > 128GB，则 LFU 无法完美驻留前 1%，Δ_H_max 需进一步受容量约束修正；若 < 128GB，则 N12 公式成立。计算需基于 ρ=0 假设下的 S_i 分布。

## Corrected Claim

LFU 完美区分假设的容量可行性校验：前 1,000 个最热对象的总大小 Sum_S_top1000 是否小于 128GB。若 Sum_S_top1000 > 128GB，则 LFU 无法完美驻留前 1%，Δ_H_max 需进一步受容量约束修正；若 < 128GB，则 N12 公式成立。计算需基于 ρ=0 假设下的 S_i 分布。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache capacity constraint top K objects size sum
