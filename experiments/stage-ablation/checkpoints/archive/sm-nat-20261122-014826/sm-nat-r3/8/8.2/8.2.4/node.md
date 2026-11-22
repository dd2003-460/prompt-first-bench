# N163: 基于 N30 的条件期望 E[Size|Hot] ≈ 9.9KB 与全局 E[Size] ≈ 11KB，计算字节加权后的实际热度集中度修正因子 K_size =

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59, N60, N61

## Claim

基于 N30 的条件期望 E[Size|Hot] ≈ 9.9KB 与全局 E[Size] ≈ 11KB，计算字节加权后的实际热度集中度修正因子 K_size = E[Size|Hot] / E[Size] ≈ 0.9，用于调整 H_byte 的下界。

## Corrected Claim

基于 N30 的条件期望 E[Size|Hot] ≈ 9.9KB 与全局 E[Size] ≈ 11KB，计算字节加权后的实际热度集中度修正因子 K_size = E[Size|Hot] / E[Size] ≈ 0.9，用于调整 H_byte 的下界。

## Evidence

先验知识/题面给定，逻辑校验通过：9.9/11 ≈ 0.9，计算无误，量纲一致，符合条件期望定义。
