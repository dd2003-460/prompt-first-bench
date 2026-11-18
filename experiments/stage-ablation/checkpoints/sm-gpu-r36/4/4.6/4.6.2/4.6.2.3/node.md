# N233: llama.cpp 在 RTX 4090 上运行 27B INT8 模型时，默认将权重拆分至 GPU/CPU，其吞吐量瓶颈受限于 PCIe 4.0 x16 带宽

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

llama.cpp 在 RTX 4090 上运行 27B INT8 模型时，默认将权重拆分至 GPU/CPU，其吞吐量瓶颈受限于 PCIe 4.0 x16 带宽 (~32 GB/s) 与 GPU 显存带宽 (~1 TB/s) 的比值，理论最大吞吐约为 min(Bandwidth_GPU, Bandwidth_Pcie) / Model_Size_Bytes，具体数值取决于 Offload 层数配置 (n_gpu_layers)。

## Corrected Claim

llama.cpp 在 RTX 4090 上运行 27B INT8 模型时，默认将权重拆分至 GPU/CPU，其吞吐量瓶颈受限于 PCIe 4.0 x16 带宽 (~32 GB/s) 与 GPU 显存带宽 (~1 TB/s) 的比值，理论最大吞吐约为 min(Bandwidth_GPU, Bandwidth_Pcie) / Model_Size_Bytes，具体数值取决于 Offload 层数配置 (n_gpu_layers)。

## Evidence

先验知识/题面给定，逻辑校验通过
