# N431: 多卡方案性价比修正逻辑：对于双卡方案（如 2x RTX 5090），其有效吞吐量 Effective_Throughput = Theoretical_Thro

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

多卡方案性价比修正逻辑：对于双卡方案（如 2x RTX 5090），其有效吞吐量 Effective_Throughput = Theoretical_Throughput * (1 - Communication_Overhead_Rate)，其中 Communication_Overhead_Rate 基于 PCIe 互联带宽与 AllReduce 通信量计算得出。性价比指标需使用 Effective_Thresholdput 而非理论峰值，以反映互联瓶颈对实际产出的折损。

## Corrected Claim

多卡方案性价比修正逻辑：对于双卡方案（如 2x RTX 5090），其有效吞吐量 Effective_Throughput = Theoretical_Throughput * (1 - Communication_Overhead_Rate)，其中 Communication_Overhead_Rate 基于 PCIe 互联带宽与 AllReduce 通信量计算得出。性价比指标需使用 Effective_Thresholdput 而非理论峰值，以反映互联瓶颈对实际产出的折损。

## Evidence

检索失败: no sources from any channel (all 5 failed)
