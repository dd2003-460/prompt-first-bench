# N11: NVIDIA 数据中心卡（H100/A100）与消费级卡（RTX 4090/5090）在 CUDA 架构兼容性上无差异，均支持 BF16/FP8/INT8 推理

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

NVIDIA 数据中心卡（H100/A100）与消费级卡（RTX 4090/5090）在 CUDA 架构兼容性上无差异，均支持 BF16/FP8/INT8 推理，但消费级卡缺乏 NVLink 互联，多卡扩展时 PCIe 带宽成为瓶颈。

## Corrected Claim

NVIDIA 数据中心卡（H100/A100）与消费级卡（RTX 4090/5090）在 CUDA 架构兼容性上无差异，均支持 BF16/FP8/INT8 推理，但消费级卡缺乏 NVLink 互联，多卡扩展时 PCIe 带宽成为瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过
