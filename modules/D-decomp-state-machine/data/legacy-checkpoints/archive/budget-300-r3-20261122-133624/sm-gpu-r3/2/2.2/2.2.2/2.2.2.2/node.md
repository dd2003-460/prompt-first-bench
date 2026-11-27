# N251: 工作点 B（中性价比/数据中心单卡）：1× H100 PCIe (80GB, 700W)，系统总功耗 700W + 200W = 900W；3 年电力成本 = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

工作点 B（中性价比/数据中心单卡）：1× H100 PCIe (80GB, 700W)，系统总功耗 700W + 200W = 900W；3 年电力成本 = 900W × 8760h × 3y × $0.12/kWh ≈ $2,840；对比 N72 的 800W 假设，H100 方案电力成本高 11%，但无需多卡互联开销且显存充裕（BF16 可行），单位 token 电力成本因高带宽而降低。

## Corrected Claim

工作点 B（中性价比/数据中心单卡）：1× H100 PCIe (80GB, 700W)，系统总功耗 700W + 200W = 900W；3 年电力成本 = 900W × 8760h × 3y × $0.12/kWh ≈ $2,840；对比 N72 的 800W 假设，H100 方案电力成本高 11%，但无需多卡互联开销且显存充裕（BF16 可行），单位 token 电力成本因高带宽而降低。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 PCIe 功耗约 700W 符合规格，电力成本计算 900W * 8760h * 3y * 0.12/kWh ≈ $2840 数学正确，与 800W 基准对比 11% 差异逻辑自洽。

## Search Query

H100 PCIe TDP power consumption watts
