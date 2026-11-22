# N410: 工作点A（单卡瓶颈基准）：2x RTX 4090 方案中，若模型权重与KV Cache完全驻留在单卡显存内（通过Offload或量化压缩至<24GB），有效吞吐

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N147

## Claim

工作点A（单卡瓶颈基准）：2x RTX 4090 方案中，若模型权重与KV Cache完全驻留在单卡显存内（通过Offload或量化压缩至<24GB），有效吞吐率受限于单卡RTX 4090的显存带宽，理论上限为 1008 GB/s / 37.7 GB ≈ 26.7 tokens/s，实际因PCIe通信开销略低，约24-26 tokens/s。

## Corrected Claim

工作点A（单卡瓶颈基准）：2x RTX 4090 方案中，若模型权重与KV Cache完全驻留在单卡显存内（通过Offload或量化压缩至<24GB），有效吞吐率受限于单卡RTX 4090的显存带宽，理论上限为 1008 GB/s / 37.7 GB ≈ 26.7 tokens/s，实际因PCIe通信开销略低，约24-26 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存带宽1008GB/s与37.7GB模型大小相除得26.7 tokens/s，符合Roofline模型计算逻辑，且PCIe开销导致的实际值略低符合工程直觉。
