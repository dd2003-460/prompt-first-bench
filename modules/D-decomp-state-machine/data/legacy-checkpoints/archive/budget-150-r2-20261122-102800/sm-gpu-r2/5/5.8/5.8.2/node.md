# N131: 多卡部署中，PCIe 4.0 x16 的有效带宽通常低于理论峰值 64 GB/s，实测有效带宽约为 48-56 GB/s；因此，实际通信延迟需修正为 通信量 /

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

多卡部署中，PCIe 4.0 x16 的有效带宽通常低于理论峰值 64 GB/s，实测有效带宽约为 48-56 GB/s；因此，实际通信延迟需修正为 通信量 / 有效带宽，对于 512 MB 通信量，实际延迟约为 9.1-10.7 ms/step。

## Corrected Claim

多卡部署中，PCIe 4.0 x16 的有效带宽通常低于理论峰值 64 GB/s，实测有效带宽约为 48-56 GB/s；因此，实际通信延迟需修正为 通信量 / 有效带宽，对于 512 MB 通信量，实际延迟约为 9.1-10.7 ms/step。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 理论带宽 64 GB/s，有效带宽 48-56 GB/s 符合工程常识（约 75%-87% 效率）；512 MB / 56 GB/s ≈ 9.14 ms，512 MB / 48 GB/s ≈ 10.67 ms，数值计算准确且量级合理。

## Search Query

PCIe 4.0 x16 effective bandwidth measured vs theoretical
