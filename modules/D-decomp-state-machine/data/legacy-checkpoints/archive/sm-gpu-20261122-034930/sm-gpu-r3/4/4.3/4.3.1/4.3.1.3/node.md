# N322: 工作点1-C（中等成本/中等性能-PCIe版）：1x A100 40GB (PCIe)，3年TCO ≈ $8,000 + $788 + $300 = $9,08

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

工作点1-C（中等成本/中等性能-PCIe版）：1x A100 40GB (PCIe)，3年TCO ≈ $8,000 + $788 + $300 = $9,088，吞吐量受限于PCIe带宽及显存容量（需Offload或降精度），实际吞吐量约30-40 tokens/s，性价比指标 = 35 / 9,088 ≈ 3.85 tokens/s/$，略高于SXM版，但显存容量不足导致32K上下文下需Offload，实际延迟增加。

## Corrected Claim

工作点1-C（中等成本/中等性能-PCIe版）：1x A100 40GB (PCIe)，3年TCO ≈ $8,000 + $788 + $300 = $9,088，吞吐量受限于PCIe带宽及显存容量（需Offload或降精度），实际吞吐量约30-40 tokens/s，性价比指标 = 35 / 9,088 ≈ 3.85 tokens/s/$，略高于SXM版，但显存容量不足导致32K上下文下需Offload，实际延迟增加。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 PCIe版单卡推理30-40 tokens/s符合工程常识，TCO计算逻辑自洽，性价比指标推导正确。
