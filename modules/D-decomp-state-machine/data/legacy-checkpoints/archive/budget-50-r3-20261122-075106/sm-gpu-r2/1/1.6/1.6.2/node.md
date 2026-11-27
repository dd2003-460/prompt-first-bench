# N64: 在 2×A100 80GB (PCIe 4.0) 方案中，若启用 NVLink 桥接 (若主板支持，通常不支持)，带宽提升至 600GB/s，通信延迟降至 0.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

在 2×A100 80GB (PCIe 4.0) 方案中，若启用 NVLink 桥接 (若主板支持，通常不支持)，带宽提升至 600GB/s，通信延迟降至 0.64μs/step；若仅用 PCIe，延迟仍为 12μs/step，但 A100 的 TPOT 本身较低 (14-20ms)，通信占比仍 <0.1%

## Corrected Claim

在 2×A100 80GB (PCIe 4.0) 方案中，若启用 NVLink 桥接 (若主板支持，通常不支持)，带宽提升至 600GB/s，通信延迟降至 0.64μs/step；若仅用 PCIe，延迟仍为 12μs/step，但 A100 的 TPOT 本身较低 (14-20ms)，通信占比仍 <0.1%

## Evidence

先验知识/题面给定，逻辑校验通过：A100 NVLink带宽600GB/s及PCIe延迟量级符合硬件规格，TPOT 14-20ms下通信占比<0.1%的估算在逻辑上自洽。
