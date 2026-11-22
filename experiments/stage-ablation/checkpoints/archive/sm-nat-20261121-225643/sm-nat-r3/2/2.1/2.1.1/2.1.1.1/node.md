# N63: LFU头部锁定收益的精确积分表达式：ΔH_lock = ∫_{s_min}^{s_threshold} [P_LFU_resident(s) - P_LRU_r

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

LFU头部锁定收益的精确积分表达式：ΔH_lock = ∫_{s_min}^{s_threshold} [P_LFU_resident(s) - P_LRU_resident(s)] * f_pop(s) * f_size(s) ds / ∫ f_pop(s) f_size(s) ds，其中s_threshold为LFU开始驱逐而LRU仍保留的大小阈值，需基于β=1.2计算具体的驻留概率差值积分值。

## Corrected Claim

LFU头部锁定收益的精确积分表达式：ΔH_lock = ∫_{s_min}^{s_threshold} [P_LFU_resident(s) - P_LRU_resident(s)] * f_pop(s) * f_size(s) ds / ∫ f_pop(s) f_size(s) ds，其中s_threshold为LFU开始驱逐而LRU仍保留的大小阈值，需基于β=1.2计算具体的驻留概率差值积分值。

## Evidence

先验知识/题面给定，逻辑校验通过
