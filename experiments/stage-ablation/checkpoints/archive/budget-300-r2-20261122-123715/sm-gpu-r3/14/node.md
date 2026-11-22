# N384: 硬件候选集筛选边界逻辑：排除显存带宽 < 500 GB/s 的GPU（如RTX 4060 Ti 16GB, 272 GB/s），因其在W4量化下理论上限 < 3

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

硬件候选集筛选边界逻辑：排除显存带宽 < 500 GB/s 的GPU（如RTX 4060 Ti 16GB, 272 GB/s），因其在W4量化下理论上限 < 30 tok/s，且显存容量不足导致必须Offload，TCO/吞吐比劣于任何24GB+方案；排除无成熟推理框架支持的架构（如Intel Arc, 缺乏vLLM/TensorRT-LLM稳定支持）。

## Corrected Claim

硬件候选集筛选边界逻辑：排除显存带宽 < 500 GB/s 的GPU（如RTX 4060 Ti 16GB, 272 GB/s），因其在W4量化下理论上限 < 30 tok/s，且显存容量不足导致必须Offload，TCO/吞吐比劣于任何24GB+方案；排除无成熟推理框架支持的架构（如Intel Arc, 缺乏vLLM/TensorRT-LLM稳定支持）。

## Evidence

检索失败: no sources from any channel (all 5 failed)
