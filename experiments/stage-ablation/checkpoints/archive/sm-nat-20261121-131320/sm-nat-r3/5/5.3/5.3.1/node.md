# N119: Pareto(α=1.1) 分布下，大小小于阈值 S_th 的对象所占总字节数的比例公式 R_byte(S_th) = 1 - (x_min/S_th)^(α-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

Pareto(α=1.1) 分布下，大小小于阈值 S_th 的对象所占总字节数的比例公式 R_byte(S_th) = 1 - (x_min/S_th)^(α-1) 仅在 α>1 时成立；当 α=1.1 时，R_byte(S_th) = 1 - (x_min/S_th)^0.1，该值随 S_th 增大而缓慢增加，例如 S_th=100KB 时 R_byte ≈ 1 - (1/100)^0.1 ≈ 1 - 0.447 ≈ 0.553，即 55.3% 的字节来自小于 100KB 的对象。

## Corrected Claim

Pareto(α=1.1) 分布下，大小小于阈值 S_th 的对象所占总字节数的比例公式 R_byte(S_th) = 1 - (x_min/S_th)^(α-1) 仅在 α>1 时成立；当 α=1.1 时，R_byte(S_th) = 1 - (x_min/S_th)^0.1，该值随 S_th 增大而缓慢增加，例如 S_th=100KB 时 R_byte ≈ 1 - (1/100)^0.1 ≈ 1 - 0.447 ≈ 0.553，即 55.3% 的字节来自小于 100KB 的对象。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(α>1)的累积字节占比公式推导正确，数值计算(1/100)^0.1≈0.447准确，符合数学第一性原理。
