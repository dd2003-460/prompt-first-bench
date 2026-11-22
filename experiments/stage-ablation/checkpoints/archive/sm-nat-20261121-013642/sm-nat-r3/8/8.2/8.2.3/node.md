# N247: Gap = H_MIN - H_LRU ≈ 0.92 - 0.78 = 0.14 (14 个百分点)，该差距主要源于 MIN 算法能保留高 r_i/s_i 比值

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N85

## Claim

Gap = H_MIN - H_LRU ≈ 0.92 - 0.78 = 0.14 (14 个百分点)，该差距主要源于 MIN 算法能保留高 r_i/s_i 比值的长尾小对象，而 LRU 易被大对象驱逐，导致字节效率损失约 14%。

## Corrected Claim

Gap = H_MIN - H_LRU ≈ 0.92 - 0.78 = 0.14 (14 个百分点)，该差距主要源于 MIN 算法能保留高 r_i/s_i 比值的长尾小对象，而 LRU 易被大对象驱逐，导致字节效率损失约 14%。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（0.92-0.78=0.14），且MIN算法基于引用频率/大小比保留长尾小对象、LRU易受大对象干扰导致字节效率损失的机制符合缓存理论常识。
