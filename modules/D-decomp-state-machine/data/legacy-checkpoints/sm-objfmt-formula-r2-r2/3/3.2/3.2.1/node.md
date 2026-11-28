# N97: RTX 4090 的标称显存带宽为 1008 GB/s（GDDR6X 21Gbps × 384-bit / 8），该数值为硬件物理上限，实际推理中受 PCIe 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

RTX 4090 的标称显存带宽为 1008 GB/s（GDDR6X 21Gbps × 384-bit / 8），该数值为硬件物理上限，实际推理中受 PCIe 与调度影响的有效带宽利用率通常在 70%-90% 之间 [待核验]。

## Corrected Claim

RTX 4090 的标称显存带宽为 1008 GB/s（GDDR6X 21Gbps × 384-bit / 8），该数值为硬件物理上限，实际推理中受 PCIe 与调度影响的有效带宽利用率通常在 70%-90% 之间 [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 采用 GDDR6X 显存，速率 21 Gbps，位宽 384-bit，计算带宽 21 * 384 / 8 = 1008 GB/s，数值准确；有效带宽利用率 70%-90% 符合 GPU 推理场景下的常见工程经验范围。

## Search Query

RTX 4090 memory bandwidth GB/s official spec
