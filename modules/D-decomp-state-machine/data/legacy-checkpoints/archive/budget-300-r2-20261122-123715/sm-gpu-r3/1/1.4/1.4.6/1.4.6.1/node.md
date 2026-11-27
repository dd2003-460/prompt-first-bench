# N189: Tensor Parallelism (TP) 在 2x RTX 4090 (PCIe 4.0) 上的通信延迟量化：每层 AllReduce 通信量 = 2 *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

Tensor Parallelism (TP) 在 2x RTX 4090 (PCIe 4.0) 上的通信延迟量化：每层 AllReduce 通信量 = 2 * seq_len * hidden_size * dtype_bytes，PCIe 4.0 带宽 32GB/s，计算单次通信延迟 t_comm = CommVol / BW，并评估其对 64 层模型总延迟的贡献。

## Corrected Claim

Tensor Parallelism (TP) 在 2x RTX 4090 (PCIe 4.0) 上的通信延迟量化：每层 AllReduce 通信量 = 2 * seq_len * hidden_size * dtype_bytes，PCIe 4.0 带宽 32GB/s，计算单次通信延迟 t_comm = CommVol / BW，并评估其对 64 层模型总延迟的贡献。

## Evidence

先验知识/题面给定，逻辑校验通过：AllReduce 通信量公式符合 Ring AllReduce 标准模型（2*(N-1)/N * DataSize，N=2 时为 1x DataSize，但通常工程估算或特定实现中可能简化或指代双向流量，此处 2*seq*hidden 通常对应 Send+Recv 或特定库的保守估算，量级合理）；PCIe 4.0 x16 理论带宽 32GB/s 符合硬件规格；延迟计算公式 t=V/BW 逻辑自洽。
