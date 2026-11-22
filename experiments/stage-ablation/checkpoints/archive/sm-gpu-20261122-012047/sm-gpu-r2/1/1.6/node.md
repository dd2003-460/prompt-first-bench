# N11: NVIDIA 数据中心卡（H100/A100）与消费级卡（RTX 4090/5090）在 CUDA 架构兼容性上无差异，均支持 BF16/FP8/INT8 推理

- **status**: pending
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

父节点级核验未通过：不完备（子节点正交性良好，分别聚焦于互联带宽和计算精度支持两个不同维度。但完备性不足：父节点明确声称‘CUDA 架构兼容性上无差异’，而子节点2指出 H100 和 RTX 4090 在 FP8 加速支持上存在硬件差异（H100 支持 FP8，RTX 4090 仅支持 INT8），这直接与父节点的‘无差异’结论矛盾，导致父节点的核心论点未被正确覆盖或解释。此外，父节点提到的‘均支持 BF16’在子节点中未体现。）
