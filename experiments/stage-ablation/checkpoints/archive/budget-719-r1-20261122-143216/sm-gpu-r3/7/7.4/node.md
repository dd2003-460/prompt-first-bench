# N132: AMD MI300X 显存带宽为 5.3 TB/s，远超 RTX 5090 (1.79 TB/s)，在 Decode 阶段理论吞吐量上限更高，但实际效率受 RO

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32, N33, N34

## Claim

AMD MI300X 显存带宽为 5.3 TB/s，远超 RTX 5090 (1.79 TB/s)，在 Decode 阶段理论吞吐量上限更高，但实际效率受 ROCm 软件栈成熟度影响，需对比实测 tokens/s 与理论带宽比值的偏差。

## Corrected Claim

AMD MI300X 显存带宽为 5.3 TB/s，远超 RTX 5090 (1.79 TB/s)，在 Decode 阶段理论吞吐量上限更高，但实际效率受 ROCm 软件栈成熟度影响，需对比实测 tokens/s 与理论带宽比值的偏差。

## Evidence

先验知识/题面给定，逻辑校验通过：AMD MI300X 官方规格确为 5.3 TB/s HBM3 带宽，RTX 5090 为 1.79 TB/s GDDR7 带宽，数值量级准确；Decode 阶段受内存带宽限制的理论推导符合计算机体系结构基本原理；ROCm 软件栈成熟度影响实际效率属于公认的工程事实，逻辑自洽。

## Search Query

AMD MI300X vs RTX 5090 LLM decode throughput ROCm efficiency
