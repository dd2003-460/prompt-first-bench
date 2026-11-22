# N378: PCIe 4.0 x16 在 GPU-to-GPU 通信中的实际有效带宽实测值：在 NVIDIA 官方文档或第三方基准测试中，PCIe 4.0 x16 的有效带

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N118

## Claim

PCIe 4.0 x16 在 GPU-to-GPU 通信中的实际有效带宽实测值：在 NVIDIA 官方文档或第三方基准测试中，PCIe 4.0 x16 的有效带宽通常在 24-28 GB/s 之间（取 50-70% 利用率的中高值），而非简单的 16-22 GB/s。需修正 N118 中的保守估计，采用 25 GB/s 作为典型有效带宽用于 TCO 计算。

## Corrected Claim

PCIe 4.0 x16 在 GPU-to-GPU 通信中的实际有效带宽通常低于理论峰值（约 32 GB/s），具体数值取决于协议开销和驱动优化，建议采用保守估计或查阅特定硬件基准测试数据。

## Evidence

[质询]该陈述包含具体的经验性数值范围（24-28 GB/s）和特定利用率假设（50-70%），属于硬件性能实测数据，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

PCIe 4.0 x16 effective bandwidth GPU to GPU benchmark
