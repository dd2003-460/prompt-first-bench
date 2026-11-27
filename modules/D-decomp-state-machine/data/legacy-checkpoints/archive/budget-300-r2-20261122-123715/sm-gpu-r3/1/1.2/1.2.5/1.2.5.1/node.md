# N158: A10 24GB 的显存带宽为 600 GB/s (GDDR6 ECC)，而非 PCIe 带宽 64 GB/s；在 W4 量化下，Token 生成（Decode

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

A10 24GB 的显存带宽为 600 GB/s (GDDR6 ECC)，而非 PCIe 带宽 64 GB/s；在 W4 量化下，Token 生成（Decode）阶段的瓶颈是显存带宽而非 PCIe 带宽，理论吞吐上限 = 600 GB/s / 13.5 GB ≈ 44.4 tokens/s，实际受计算密度限制通常更低。

## Corrected Claim

A10 24GB 的显存带宽为 600 GB/s (GDDR6 ECC)，而非 PCIe 带宽 64 GB/s；在 W4 量化下，Token 生成（Decode）阶段的瓶颈是显存带宽而非 PCIe 带宽，理论吞吐上限 = 600 GB/s / 13.5 GB ≈ 44.4 tokens/s，实际受计算密度限制通常更低。

## Evidence

先验知识/题面给定，逻辑校验通过：A10 24GB 显存带宽确为 600 GB/s，W4 量化下 13.5GB 模型理论吞吐计算正确（600/13.5≈44.4），且 Decode 阶段受显存带宽限制符合 Roofline 模型原理。

## Search Query

NVIDIA A10 GPU memory bandwidth GDDR6 specs
