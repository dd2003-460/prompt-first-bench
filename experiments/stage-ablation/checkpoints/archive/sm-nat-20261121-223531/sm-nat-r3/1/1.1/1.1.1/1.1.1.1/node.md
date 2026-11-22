# N90: s_min 的理论下界约束：s_min ≥ 1 Byte（或最小可寻址单元），若 s_min < 1 Byte 则违反物理存储最小单元定义。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

s_min 的理论下界约束：s_min ≥ 1 Byte（或最小可寻址单元），若 s_min < 1 Byte 则违反物理存储最小单元定义。

## Corrected Claim

s_min 的理论下界约束：s_min ≥ 1 Byte（或最小可寻址单元），若 s_min < 1 Byte 则违反物理存储最小单元定义。

## Evidence

先验知识/题面给定，逻辑校验通过：字节（Byte）是计算机存储和寻址的最小标准单位，小于1字节的存储单元在标准物理架构中不可独立寻址，因此 s_min ≥ 1 Byte 符合物理存储最小单元定义。
