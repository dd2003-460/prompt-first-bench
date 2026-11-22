# N127: NVIDIA RTX 5090 的 PCIe 5.0 接口带宽（64 GB/s x4）对多卡或大模型权重加载/卸载的影响：在单卡推理中若模型权重+KV Cach

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35, N36, N37

## Claim

NVIDIA RTX 5090 的 PCIe 5.0 接口带宽（64 GB/s x4）对多卡或大模型权重加载/卸载的影响：在单卡推理中若模型权重+KV Cache 超过 32GB 需 Swap 至 CPU 内存，Swap 带宽受限于 PCIe 5.0，需计算 Swap 导致的额外延迟占比。

## Corrected Claim

NVIDIA RTX 5090 的 PCIe 5.0 接口带宽（64 GB/s x4）对多卡或大模型权重加载/卸载的影响：在单卡推理中若模型权重+KV Cache 超过 32GB 需 Swap 至 CPU 内存，Swap 带宽受限于 PCIe 5.0，需计算 Swap 导致的额外延迟占比。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 5.0 x4 理论带宽确为 64 GB/s，且大模型推理中显存溢出导致 Swap 至 CPU 内存并受限于 PCIe 带宽是符合硬件架构与内存层级原理的正确描述。
