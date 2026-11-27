# N10: 多卡互联拓扑成本：消费级多卡（2x RTX 4090）所需的PCIe通道损耗系数（通常1.0x vs 0.5x带宽）及额外机箱/电源成本（约$200-$500）

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

多卡互联拓扑成本：消费级多卡（2x RTX 4090）所需的PCIe通道损耗系数（通常1.0x vs 0.5x带宽）及额外机箱/电源成本（约$200-$500），对比数据中心多卡（NVLink）的带宽优势（600GB/s+）与溢价。

## Corrected Claim

多卡互联拓扑成本：消费级多卡（2x RTX 4090）所需的PCIe通道损耗系数（通常1.0x vs 0.5x带宽）及额外机箱/电源成本（约$200-$500），对比数据中心多卡（NVLink）的带宽优势（600GB/s+）与溢价。

## Evidence

先验知识/题面给定，逻辑校验通过：消费级PCIe 4.0 x16带宽约32GB/s，x8减半符合0.5x描述；NVLink 4.0/5.0带宽确实在600GB/s以上；多卡机箱电源成本$200-$500符合市场常识。
