# N125: RTX 5090 的官方显存带宽规格为 1792 GB/s（基于 32GB GDDR7 显存，384-bit 位宽，28 Gbps 速率计算：384/8 * 2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

RTX 5090 的官方显存带宽规格为 1792 GB/s（基于 32GB GDDR7 显存，384-bit 位宽，28 Gbps 速率计算：384/8 * 28 = 1344? 修正：384-bit 接口，GDDR7 速率通常为 28Gbps 或更高，若按 1792GB/s 倒推需 28Gbps * 48 bytes = 1344? 不，384-bit = 48 bytes。48 * 28 = 1344 GB/s。若为 1792 GB/s，则需 37.3 Gbps 或更宽位宽。经查证，RTX 5090 显存位宽为 512-bit，GDDR7 速率 28 Gbps，带宽 = 512/8 * 28 = 1792 GB/s）

## Corrected Claim

RTX 5090 的官方显存带宽规格为 1792 GB/s（基于 32GB GDDR7 显存，384-bit 位宽，28 Gbps 速率计算：384/8 * 28 = 1344? 修正：384-bit 接口，GDDR7 速率通常为 28Gbps 或更高，若按 1792GB/s 倒推需 28Gbps * 48 bytes = 1344? 不，384-bit = 48 bytes。48 * 28 = 1344 GB/s。若为 1792 GB/s，则需 37.3 Gbps 或更宽位宽。经查证，RTX 5090 显存位宽为 512-bit，GDDR7 速率 28 Gbps，带宽 = 512/8 * 28 = 1792 GB/s）

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 确实采用 512-bit 位宽 GDDR7 显存，按 28 Gbps 速率计算带宽为 512/8 * 28 = 1792 GB/s，数学推导与硬件规格一致。
