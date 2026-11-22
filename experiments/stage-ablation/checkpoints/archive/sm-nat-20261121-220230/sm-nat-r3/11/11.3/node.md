# N297: 字节覆盖率 Byte_Coverage 的最终量化值：Byte_Coverage = S_resident / S_total，结合 N104 的分母和 N10

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N102

## Claim

字节覆盖率 Byte_Coverage 的最终量化值：Byte_Coverage = S_resident / S_total，结合 N104 的分母和 N105 的分子计算，预计值在 2.3% 左右，需验证是否因负相关 ρ=-0.3 导致驻留集合实际平均大小偏离纯大小排序假设（若热度负相关，LRU 可能驱逐部分小但冷的对象，保留稍大但热的对象，导致 S_resident 略高于纯最小 K 个对象的总和）。

## Corrected Claim

字节覆盖率 Byte_Coverage 的最终量化值：Byte_Coverage = S_resident / S_total，结合 N104 的分母和 N105 的分子计算，预计值在 2.3% 左右，需验证是否因负相关 ρ=-0.3 导致驻留集合实际平均大小偏离纯大小排序假设（若热度负相关，LRU 可能驱逐部分小但冷的对象，保留稍大但热的对象，导致 S_resident 略高于纯最小 K 个对象的总和）。

## Evidence

先验知识/题面给定，逻辑校验通过
