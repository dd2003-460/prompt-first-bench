# N419: AMD Ryzen 9 7950X3D 在 DDR5-6000 双通道下的理论内存带宽约为 96 GB/s，实测有效带宽约为 80-85 GB/s，该带宽是 C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N151

## Claim

AMD Ryzen 9 7950X3D 在 DDR5-6000 双通道下的理论内存带宽约为 96 GB/s，实测有效带宽约为 80-85 GB/s，该带宽是 CPU 推理 Qwen3-27B (Q4_K_M, ~15GB) 的 Decode 速度上限决定因素。

## Corrected Claim

AMD Ryzen 9 7950X3D 在 DDR5-6000 双通道下的理论内存带宽约为 96 GB/s，实测有效带宽约为 80-85 GB/s，该带宽是 CPU 推理 Qwen3-27B (Q4_K_M, ~15GB) 的 Decode 速度上限决定因素。

## Evidence

先验知识/题面给定，逻辑校验通过：DDR5-6000双通道理论带宽为6000MT/s×8B×2=96GB/s，实测80-85GB/s符合工程常识；对于15GB的Q4_K_M模型，Decode阶段受限于内存带宽，该带宽确为速度上限决定因素。
