# N533: RTX 5090 显存位宽 512-bit 的推导验证：基于官方带宽 1792 GB/s 和 GDDR7 单颗粒速率 28 Gbps，计算 1792 / (28

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N220

## Claim

RTX 5090 显存位宽 512-bit 的推导验证：基于官方带宽 1792 GB/s 和 GDDR7 单颗粒速率 28 Gbps，计算 1792 / (28/8) = 512 bits，确认 N125 中 384-bit 为错误描述，此规格决定了显存总线物理上限，直接影响后续带宽依赖型性能估算的基准准确性。

## Corrected Claim

RTX 5090 显存位宽 512-bit 的推导验证：基于官方带宽 1792 GB/s 和 GDDR7 单颗粒速率 28 Gbps，计算 1792 / (28/8) = 512 bits，确认 N125 中 384-bit 为错误描述，此规格决定了显存总线物理上限，直接影响后续带宽依赖型性能估算的基准准确性。

## Evidence

先验知识/题面给定，逻辑校验通过：1792 GB/s 带宽除以 GDDR7 单颗粒有效速率 3.5 GB/s (28 Gbps / 8) 等于 512，数学推导自洽且符合 RTX 5090 官方规格。
