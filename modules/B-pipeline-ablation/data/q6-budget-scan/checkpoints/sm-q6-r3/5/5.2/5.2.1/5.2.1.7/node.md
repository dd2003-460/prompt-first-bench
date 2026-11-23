# N241: 回源敏感度 δ 与内容更新频率的关系：δ = 1 / (1 + T_update / TTL_opt)，当 T_update → 0 时 δ → 1（回源率对T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75, N76, N77

## Claim

回源敏感度 δ 与内容更新频率的关系：δ = 1 / (1 + T_update / TTL_opt)，当 T_update → 0 时 δ → 1（回源率对TTL极度敏感），当 T_update → ∞ 时 δ → 0（回源率不随TTL变化）；对于混合对象，δ 需按流量占比加权平均

## Corrected Claim

回源敏感度 δ 与内容更新频率的关系：δ = 1 / (1 + T_update / TTL_opt)，当 T_update → 0 时 δ → 1（回源率对TTL极度敏感），当 T_update → ∞ 时 δ → 0（回源率不随TTL变化）；对于混合对象，δ 需按流量占比加权平均

## Evidence

先验知识/题面给定，逻辑校验通过
