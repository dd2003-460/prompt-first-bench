# N261: INT4 (AWQ) 精度下总内存需求修正值：Weights (13.5GB) + KV_Cache (4.30GB) + Overhead (3GB) = 2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83, N84, N85

## Claim

INT4 (AWQ) 精度下总内存需求修正值：Weights (13.5GB) + KV_Cache (4.30GB) + Overhead (3GB) = 20.80 GB。该数值低于 RTX 4090 的 24GB 显存上限，剩余可用显存为 24 - 20.80 = 3.20 GB。此余量足以覆盖操作系统驱动占用（~0.5GB）及临时缓冲区，确认 RTX 4090 在 INT4 下可运行 32K 上下文。

## Corrected Claim

INT4 (AWQ) 精度下总内存需求修正值：Weights (13.5GB) + KV_Cache (4.30GB) + Overhead (3GB) = 20.80 GB。该数值低于 RTX 4090 的 24GB 显存上限，剩余可用显存为 24 - 20.80 = 3.20 GB。此余量足以覆盖操作系统驱动占用（~0.5GB）及临时缓冲区，确认 RTX 4090 在 INT4 下可运行 32K 上下文。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（13.5+4.3+3=20.8，24-20.8=3.2），且3.2GB余量覆盖0.5GB驱动及临时缓冲区的工程估算符合常识。
