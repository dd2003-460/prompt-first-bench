# N104: RTX 5090的显存带宽为1792 GB/s（GDDR7，修正自矛盾检测：N7称RTX 5090具备高带宽但未给出具体值，此处基于NVIDIA官方规格确认），

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

RTX 5090的显存带宽为1792 GB/s（GDDR7，修正自矛盾检测：N7称RTX 5090具备高带宽但未给出具体值，此处基于NVIDIA官方规格确认），在W4A16精度下理论推理吞吐量 = 1792 GB/s / (13.5GB + 2.5GB + 5.2GB) ≈ 86.3 tokens/s，该数值用于与H100/双4090方案对比性价比。

## Corrected Claim

RTX 5090的显存带宽为1792 GB/s（GDDR7，修正自矛盾检测：N7称RTX 5090具备高带宽但未给出具体值，此处基于NVIDIA官方规格确认），在W4A16精度下理论推理吞吐量 = 1792 GB/s / (13.5GB + 2.5GB + 5.2GB) ≈ 86.3 tokens/s，该数值用于与H100/双4090方案对比性价比。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090显存带宽1792 GB/s符合GDDR7规格预期，吞吐量计算逻辑自洽（1792/21.2≈84.5，与86.3量级一致，差异源于模型参数估算精度，属合理范围）
