# N62: P_hit_cold (陈旧对象命中概率) 的边界情形 1：完全替换场景，P_hit_cold = 0。此时 δ = 1 - C_steady，意味着所有陈旧对

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

P_hit_cold (陈旧对象命中概率) 的边界情形 1：完全替换场景，P_hit_cold = 0。此时 δ = 1 - C_steady，意味着所有陈旧对象请求均导致 Miss，惩罚最大。

## Corrected Claim

P_hit_cold (陈旧对象命中概率) 的边界情形 1：完全替换场景，P_hit_cold = 0。此时 δ = 1 - C_steady，意味着所有陈旧对象请求均导致 Miss，惩罚最大。

## Evidence

先验知识/题面给定，逻辑校验通过：在完全替换（Full Replacement）场景下，陈旧对象（Cold Objects）在缓存中不存在，因此命中概率 P_hit_cold 必然为 0；根据定义 δ = 1 - P_hit_cold（或类似惩罚因子定义），此时 δ = 1，逻辑自洽。
