# N68: TCO 对比结论：若接受 INT4 质量损失，单卡 4090 (CAPEX $1,700 + OPEX $400/年) 3 年总成本 $2,900；若需 BF1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

TCO 对比结论：若接受 INT4 质量损失，单卡 4090 (CAPEX $1,700 + OPEX $400/年) 3 年总成本 $2,900；若需 BF16 精度，2x4090 (CAPEX $3,400 + OPEX $800/年) 3 年总成本 $5,800，但性能仅相当于单卡 A100 ($12,500 + $350/年) 的 70%，且 A100 3 年总成本 $13,550 仍高于 2x4090，但提供更高稳定性和精度。

## Corrected Claim

TCO 对比结论：若接受 INT4 质量损失，单卡 4090 (CAPEX $1,700 + OPEX $400/年) 3 年总成本 $2,900；若需 BF16 精度，2x4090 (CAPEX $3,400 + OPEX $800/年) 3 年总成本 $5,800，但性能仅相当于单卡 A100 ($12,500 + $350/年) 的 70%，且 A100 3 年总成本 $13,550 仍高于 2x4090，但提供更高稳定性和精度。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（1700+400*3=2900, 3400+800*3=5800, 12500+350*3=13550），且符合当前硬件市场大致价格量级及性能对比常识。

## Search Query

TCO comparison single consumer GPU vs multi-GPU vs data center GPU
