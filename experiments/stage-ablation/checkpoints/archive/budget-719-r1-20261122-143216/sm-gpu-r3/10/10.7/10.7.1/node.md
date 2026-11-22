# N410: Batch Size=8 时，Qwen3-27B 在 2×RTX 4090 (PCIe Gen4) 上的通信开销占比计算公式：Overhead_8 = Comm

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N145

## Claim

Batch Size=8 时，Qwen3-27B 在 2×RTX 4090 (PCIe Gen4) 上的通信开销占比计算公式：Overhead_8 = Comm_Time / (8 * Compute_Time_1 + Comm_Time)，其中 Comm_Time 固定为 ~0.5ms (基于 N139 通信量 256KB 和 N140 带宽 32GB/s)，Compute_Time_1 为单 token 计算时间，该值用于验证 <15% 的阈值是否成立。

## Corrected Claim

Batch Size=8 时，Qwen3-27B 在 2×RTX 4090 (PCIe Gen4) 上的通信开销占比计算公式：Overhead_8 = Comm_Time / (8 * Compute_Time_1 + Comm_Time)，其中 Comm_Time 固定为 ~0.5ms (基于 N139 通信量 256KB 和 N140 带宽 32GB/s)，Compute_Time_1 为单 token 计算时间，该值用于验证 <15% 的阈值是否成立。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合并行计算中通信开销占比的定义（总通信时间/总时间），数值量级（0.5ms通信 vs 单token计算）在合理范围内，且source为knowledge，无需外部来源支持。
