# N89: 1×A100 40GB 方案的 TCO 计算中，电力成本部分需修正：A100 PCIe 版本 TDP 为 300W（非 400W，SXM 版为 400W），若使

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

1×A100 40GB 方案的 TCO 计算中，电力成本部分需修正：A100 PCIe 版本 TDP 为 300W（非 400W，SXM 版为 400W），若使用 PCIe 版，3 年电力成本 = 0.3kW × 8760h × 3 × $0.10 = $788，总 TCO 修正为 $15,788。

## Corrected Claim

1×A100 40GB 方案的 TCO 计算中，电力成本部分需修正：A100 PCIe 版本 TDP 为 300W（非 400W，SXM 版为 400W），若使用 PCIe 版，3 年电力成本 = 0.3kW × 8760h × 3 × $0.10 = $788，总 TCO 修正为 $15,788。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 PCIe TDP 300W 符合硬件规格常识，电力成本计算 0.3kW * 8760h * 3 * $0.10 = $788.4 取整为 $788 合理，总 TCO 修正逻辑自洽。
