# N121: H100 80GB 的 TDP 功耗同样取决于形态：SXM5 版本为 700W，PCIe 版本为 350W；N34 采用 700W 计算，需确认用户是否限定 S

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

H100 80GB 的 TDP 功耗同样取决于形态：SXM5 版本为 700W，PCIe 版本为 350W；N34 采用 700W 计算，需确认用户是否限定 SXM 形态。

## Corrected Claim

H100 80GB 的 TDP 功耗同样取决于形态：SXM5 版本为 700W，PCIe 版本为 350W；N34 采用 700W 计算，需确认用户是否限定 SXM 形态。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 TDP 700W 与 PCIe 350W 为 NVIDIA 官方公开规格，数值量级与形态差异符合工程常识，逻辑自洽。

## Search Query

NVIDIA H100 80GB SXM vs PCIe TDP watts
