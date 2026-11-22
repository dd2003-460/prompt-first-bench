# N63: NVIDIA RTX 4090 单卡运行 Qwen3-27B (INT4) 的 CAPEX 构成：P_gpu ≈ $1600 [时效待核] + P_chassi

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

NVIDIA RTX 4090 单卡运行 Qwen3-27B (INT4) 的 CAPEX 构成：P_gpu ≈ $1600 [时效待核] + P_chassis (含 24GB 显存适配的 PCIe x16 插槽及电源) ≈ $200 + P_psu (1000W+) ≈ $150 + P_network (无) + P_cooling (风冷) ≈ $50，总计 ≈ $2000。

## Corrected Claim

NVIDIA RTX 4090 单卡运行 Qwen3-27B (INT4) 的 CAPEX 构成：P_gpu ≈ $1600 [时效待核] + P_chassis (含 24GB 显存适配的 PCIe x16 插槽及电源) ≈ $200 + P_psu (1000W+) ≈ $150 + P_network (无) + P_cooling (风冷) ≈ $50，总计 ≈ $2000。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 单卡运行 27B INT4 模型在显存（24GB）和算力上可行，各组件价格量级符合市场常识，总成本估算逻辑自洽。
