# N114: 2x RTX 4090 方案中，PCIe 4.0 互联带宽为 32 GB/s (单向)，无额外硬件成本 C_interconnect = $0，但需评估多卡通信

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

2x RTX 4090 方案中，PCIe 4.0 互联带宽为 32 GB/s (单向)，无额外硬件成本 C_interconnect = $0，但需评估多卡通信开销对推理延迟的影响

## Corrected Claim

2x RTX 4090 方案中，PCIe 4.0 互联带宽为 32 GB/s (单向)，无额外硬件成本 C_interconnect = $0，但需评估多卡通信开销对推理延迟的影响

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 单向带宽理论值为 32 GB/s，双卡互联通常复用该通道，无额外硬件成本符合常规配置逻辑。
