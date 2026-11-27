# N264: 修正 N96 结论：由于 L2 缓存未命中且 GDDR6X 带宽充足，RTX 4090 在 NVFP4 下的实际推理速度上限应接近理论峰值 69.2 token

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

修正 N96 结论：由于 L2 缓存未命中且 GDDR6X 带宽充足，RTX 4090 在 NVFP4 下的实际推理速度上限应接近理论峰值 69.2 tokens/s（假设无其他瓶颈），而非 55.4 tokens/s；PCIe 延迟仅在多卡通信或 CPU 交互时显著，单卡推理中影响可忽略。

## Corrected Claim

修正 N96 结论：由于 L2 缓存未命中且 GDDR6X 带宽充足，RTX 4090 在 NVFP4 下的实际推理速度上限应接近理论峰值 69.2 tokens/s（假设无其他瓶颈），而非 55.4 tokens/s；PCIe 延迟仅在多卡通信或 CPU 交互时显著，单卡推理中影响可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：单卡推理中PCIe延迟通常可忽略，若L2未命中且显存带宽充足，推理速度主要受限于计算或显存带宽，接近理论峰值符合逻辑。
