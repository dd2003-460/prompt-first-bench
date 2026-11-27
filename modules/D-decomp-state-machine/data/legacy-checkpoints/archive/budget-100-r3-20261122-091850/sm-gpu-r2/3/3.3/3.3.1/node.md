# N71: 多卡互联带宽对 TPS 的折损系数量化：若采用 Tensor Parallelism (TP=2)，每层需 AllReduce 操作。AllReduce 通信量

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

多卡互联带宽对 TPS 的折损系数量化：若采用 Tensor Parallelism (TP=2)，每层需 AllReduce 操作。AllReduce 通信量 ≈ 2 × hidden_dim × bytes_per_element × batch_size。RTX 4090 间无 NVLink，走 PCIe 4.0 x16 (~32 GB/s 双向)。若 hidden_dim=8192, BF16, 通信量约 32KB/layer。通信时间占比 = (Comm_Time / (Compute_Time + Comm_Time))。

## Corrected Claim

多卡互联带宽对 TPS 的折损系数量化：若采用 Tensor Parallelism (TP=2)，每层需 AllReduce 操作。AllReduce 通信量 ≈ 2 × hidden_dim × bytes_per_element × batch_size。RTX 4090 间无 NVLink，走 PCIe 4.0 x16 (~32 GB/s 双向)。若 hidden_dim=8192, BF16, 通信量约 32KB/layer。通信时间占比 = (Comm_Time / (Compute_Time + Comm_Time))。

## Evidence

先验知识/题面给定，逻辑校验通过：通信量计算 2*8192*2*1=32KB 正确，PCIe 4.0 x16 带宽量级合理，公式定义自洽。

## Search Query

Tensor parallelism allreduce communication overhead PCIe vs NVLink
