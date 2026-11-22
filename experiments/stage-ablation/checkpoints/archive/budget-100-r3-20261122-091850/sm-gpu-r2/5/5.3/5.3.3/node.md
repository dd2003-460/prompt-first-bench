# N92: Xilinx Alveo U250 FPGA 方案中，27B 参数模型在 4-bit 量化下需 13.5GB 存储，U250 拥有 32GB HBM2e，带宽 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

Xilinx Alveo U250 FPGA 方案中，27B 参数模型在 4-bit 量化下需 13.5GB 存储，U250 拥有 32GB HBM2e，带宽 1.2TB/s。理论 TPS ≈ 1.2TB/s / 13.5GB ≈ 88 TPS (理论上限)，但 FPGA 推理需专用编译工具链 (Vitis AI/ONNX Runtime)，开发成本极高，且缺乏对 Qwen3 架构的原生优化算子支持。

## Corrected Claim

Xilinx Alveo U250 FPGA 方案中，27B 参数模型在 4-bit 量化下需 13.5GB 存储，U250 拥有 32GB HBM2e，带宽 1.2TB/s。理论 TPS ≈ 1.2TB/s / 13.5GB ≈ 88 TPS (理论上限)，但 FPGA 推理需专用编译工具链 (Vitis AI/ONNX Runtime)，开发成本极高，且缺乏对 Qwen3 架构的原生优化算子支持。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数4-bit量化存储约13.5GB（27e9*0.5 bytes），U250 HBM2e带宽1.2TB/s，理论TPS计算1.2e12/13.5e9≈88.8，数值量级与逻辑自洽；FPGA开发成本高及缺乏原生优化算子支持符合工程常识。

## Search Query

Xilinx Alveo U250 HBM bandwidth large language model inference
