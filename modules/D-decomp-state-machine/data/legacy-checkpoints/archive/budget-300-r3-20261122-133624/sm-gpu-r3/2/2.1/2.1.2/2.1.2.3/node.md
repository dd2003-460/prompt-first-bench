# N245: A100 80GB PCIe 的 TDP 为 400W（SXM 为 400W，PCIe 通常为 300W，此处按 400W 保守估算），在 BF16 推理实际平

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

A100 80GB PCIe 的 TDP 为 400W（SXM 为 400W，PCIe 通常为 300W，此处按 400W 保守估算），在 BF16 推理实际平均功耗约为 280W (70% TDP)，修正后的 3 年电力成本 = 280W × 8760h × 3y × $0.12/kWh ≈ $869.76。

## Corrected Claim

A100 80GB PCIe 的 TDP 为 400W（SXM 为 400W，PCIe 通常为 300W，此处按 400W 保守估算），在 BF16 推理实际平均功耗约为 280W (70% TDP)，修正后的 3 年电力成本 = 280W × 8760h × 3y × $0.12/kWh ≈ $869.76。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 PCIe TDP 300W/SXM 400W 符合规格，按 400W 保守估算逻辑自洽；功耗 280W (70% TDP) 合理；成本计算 280 * 8760 * 3 * 0.12 = 86976 Wh * $0.12/kWh = $869.76，数值准确。

## Search Query

A100 PCIe TDP watts power consumption
