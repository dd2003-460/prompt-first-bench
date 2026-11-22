# N217: TP=2 推理中通信延迟占单步总延迟的比例公式：Comm_Overhead_Ratio = (Comm_Bytes / Effective_PCIe_Bandw

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

TP=2 推理中通信延迟占单步总延迟的比例公式：Comm_Overhead_Ratio = (Comm_Bytes / Effective_PCIe_Bandwidth) / (Compute_Time_per_Layer + Comm_Time_per_Layer)，需结合 N142 带宽和实测 Compute_Time 计算，若 Ratio > 10% 则 PCIe 成为显著瓶颈。

## Corrected Claim

TP=2 推理中通信延迟占单步总延迟的比例公式：Comm_Overhead_Ratio = (Comm_Bytes / Effective_PCIe_Bandwidth) / (Compute_Time_per_Layer + Comm_Time_per_Layer)，需结合 N142 带宽和实测 Compute_Time 计算，若 Ratio > 10% 则 PCIe 成为显著瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

tensor parallelism communication overhead ratio pcie vs nvlink llm inference
