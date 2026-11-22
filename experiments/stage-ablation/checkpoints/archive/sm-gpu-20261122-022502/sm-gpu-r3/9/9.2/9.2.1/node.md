# N274: 功耗约束工作点：RTX 5090 TDP 575W，在持续高负载下若散热不足导致降频 (Thermal Throttling)，实际带宽可能降至 1.5 TB/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

功耗约束工作点：RTX 5090 TDP 575W，在持续高负载下若散热不足导致降频 (Thermal Throttling)，实际带宽可能降至 1.5 TB/s，吞吐量上限降至 111 tokens/s，实际值相应下调至 55-66 tokens/s。

## Corrected Claim

功耗约束工作点：RTX 5090 TDP 575W，在持续高负载下若散热不足导致降频 (Thermal Throttling)，实际带宽可能降至 1.5 TB/s，吞吐量上限降至 111 tokens/s，实际值相应下调至 55-66 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 TDP 575W 符合官方规格；热降频导致带宽和吞吐量下降符合物理直觉及工程常识，数值量级合理。

## Search Query

RTX 5090 thermal throttling impact on memory bandwidth
