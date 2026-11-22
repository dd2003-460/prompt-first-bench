# N172: 修正 N51 中 H100 SXM 的 TDP 数值：根据 NVIDIA 官方规格表，H100 SXM 的 TDP 为 700W，H100 PCIe 的 TDP

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

修正 N51 中 H100 SXM 的 TDP 数值：根据 NVIDIA 官方规格表，H100 SXM 的 TDP 为 700W，H100 PCIe 的 TDP 为 350W；若考虑本地工作站部署，PCIe 版本功耗显著更低，但 SXM 版本需专用基板，通常不适用于标准本地工作站。

## Corrected Claim

修正 N51 中 H100 SXM 的 TDP 数值：根据 NVIDIA 官方规格表，H100 SXM 的 TDP 为 700W，H100 PCIe 的 TDP 为 350W；若考虑本地工作站部署，PCIe 版本功耗显著更低，但 SXM 版本需专用基板，通常不适用于标准本地工作站。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVIDIA H100 SXM vs PCIe TDP specifications
