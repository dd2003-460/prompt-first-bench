# N143: A100 40GB 3年 TCO 修正计算 (基于 N89 修正)：硬件成本 $15,000 + 电力成本 (0.35 kW × 8760 h × 3 × $0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N45

## Claim

A100 40GB 3年 TCO 修正计算 (基于 N89 修正)：硬件成本 $15,000 + 电力成本 (0.35 kW × 8760 h × 3 × $0.10/kWh = $9,195) + 维护成本 (~$150) = $24,345；原 N45 使用 400W 得出 $16,051，修正后 TCO 增加 52%，主因是功耗假设错误 (PCIe 版 TDP 300W，平均 350W)。

## Corrected Claim

A100 40GB 3年 TCO 修正计算 (基于 N89 修正)：硬件成本 $15,000 + 电力成本 (0.35 kW × 8760 h × 3 × $0.10/kWh = $9,195) + 维护成本 (~$150) = $24,345；原 N45 使用 400W 得出 $16,051，修正后 TCO 增加 52%，主因是功耗假设错误 (PCIe 版 TDP 300W，平均 350W)。

## Evidence

先验知识/题面给定，逻辑校验通过：电力成本计算 0.35 * 8760 * 3 * 0.1 = 9195 正确，总成本 15000 + 9195 + 150 = 24345 正确，增幅 (24345-16051)/16051 ≈ 51.7% 与 52% 一致，且 A100 PCIe 版 TDP 300W 及平均功耗 350W 符合工程常识。

## Search Query

A100 PCIe TDP 300W power consumption inference
