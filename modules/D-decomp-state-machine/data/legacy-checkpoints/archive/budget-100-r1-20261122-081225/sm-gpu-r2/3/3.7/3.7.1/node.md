# N119: A100 80GB 的 TDP 功耗取决于形态：SXM4 版本为 400W，PCIe 版本为 300W；N33 采用 400W 计算，需确认用户是否限定 SXM

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

A100 80GB 的 TDP 功耗取决于形态：SXM4 版本为 400W，PCIe 版本为 300W；N33 采用 400W 计算，需确认用户是否限定 SXM 形态。

## Corrected Claim

A100 80GB 的 TDP 功耗取决于形态：SXM4 版本为 400W，PCIe 版本为 300W；N33 采用 400W 计算，需确认用户是否限定 SXM 形态。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 SXM4 TDP 400W 与 PCIe 300W 为 NVIDIA 官方标准规格，数值量级合理且无内部矛盾。

## Search Query

NVIDIA A100 80GB SXM vs PCIe TDP watts
