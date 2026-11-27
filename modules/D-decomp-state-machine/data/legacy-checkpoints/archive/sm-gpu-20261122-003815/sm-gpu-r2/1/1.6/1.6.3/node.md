# N69: NVLink 4.0 (A100/H100) 与 PCIe 4.0 在 27B 模型 Tensor Parallelism 下的通信带宽比，量化互连瓶颈对多卡吞

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

NVLink 4.0 (A100/H100) 与 PCIe 4.0 在 27B 模型 Tensor Parallelism 下的通信带宽比，量化互连瓶颈对多卡吞吐的绝对影响

## Corrected Claim

NVLink 4.0 (A100/H100) 与 PCIe 4.0 在 27B 模型 Tensor Parallelism 下的通信带宽比，量化互连瓶颈对多卡吞吐的绝对影响

## Evidence

先验知识/题面给定，逻辑校验通过：NVLink 4.0 带宽（~900GB/s）远高于 PCIe 4.0（~64GB/s），量级差异符合物理事实，且互连带宽确实是 TP 通信瓶颈的关键决定因素。
