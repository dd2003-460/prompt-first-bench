# N120: NVIDIA L40S (AD102) 的 GDDR6 显存带宽计算公式为：384-bit 位宽 × 22.4 Gbps 有效速率 = 864 GB/s；该数值

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

NVIDIA L40S (AD102) 的 GDDR6 显存带宽计算公式为：384-bit 位宽 × 22.4 Gbps 有效速率 = 864 GB/s；该数值源自 NVIDIA 官方规格表，确认 N29 中带宽数据准确。

## Corrected Claim

NVIDIA L40S (AD102) 的 GDDR6 显存带宽计算公式为：384-bit 位宽 × 18 Gbps 有效速率 = 864 GB/s；该数值源自 NVIDIA 官方规格表，确认 N29 中带宽数据准确。

## Evidence

先验知识/题面给定，逻辑校验通过：384-bit 位宽除以 8 等于 48 字节，48 乘以 22.4 Gbps 等于 1075.2 Gbps，即 107.52 GB/s？不对，重新计算：384 / 8 = 48 bytes. 48 * 22.4 = 1075.2 Gbps? 不，单位是 Gbps (Gigabits per second). 48 bytes * 22.4 Gbps / 8 bits/byte? 不，带宽公式通常是 (位宽/8) * 速率. 384/8 = 48. 48 * 22.4 = 1075.2 GB/s? 等等，L40S 的显存带宽官方数据是 864 GB/s. 让我们反推：864 GB/s * 8 / 384 = 18 Gbps. 或者 864 / (384/8) = 864 / 48 = 18 Gbps. 题目中给出的速率是 22.4 Gbps. 22.4 * 48 = 1075.2 GB/s. 这与 864 GB/s 不符. 

让我仔细检查 NVIDIA L40S 的规格.
NVIDIA L40S 使用 GDDR6 显存.
位宽: 384-bit.
带宽: 864 GB/s.
计算: 864 GB/s / (384/8) bytes = 864 / 48 = 18 Gbps.
所以有效速率应该是 18 Gbps.
题目中声称速率是 22.4 Gbps.
22.4 Gbps 是 GDDR6 常见的速率之一 (例如 14 Gbps, 16 Gbps, 18 Gbps, 20 Gbps, 22.4 Gbps 等).
如果速率是 22.4 Gbps，带宽应该是 1075.2 GB/s.
如果带宽是 864 GB/s，速率应该是 18 Gbps.

NVIDIA 官方 L40S 规格表显示:
Memory: 48 GB GDDR6
Memory Bandwidth: 864 GB/s

因此，题目中的陈述 "384-bit 位宽 × 22.4 Gbps 有效速率 = 864 GB/s" 在数学上是错误的 (48 * 22.4 != 864)，且参数 (22.4 Gbps) 与结果 (864 GB/s) 不匹配。正确的速率应为 18 Gbps。

这是一个硬逻辑错误/数值错误。
