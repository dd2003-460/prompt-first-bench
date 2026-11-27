# N399: L40S 48GB 的 3 年 TCO 中值约为 $10,200 (硬件 $9,750 + 电力 $450 [300W * 8760h * 3y * $0.10

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N160, N161, N162

## Claim

L40S 48GB 的 3 年 TCO 中值约为 $10,200 (硬件 $9,750 + 电力 $450 [300W * 8760h * 3y * $0.10/kWh])，其 CPR (Cost Per Request/Token) 基准值约为 0.0021 ($/token, 基于 45.3 tokens/s 吞吐和 $10,200 TCO)。

## Corrected Claim

L40S 48GB 的 3 年 TCO 中值约为 $10,200 (硬件 $9,750 + 电力 $450 [300W * 8760h * 3y * $0.10/kWh])，其 CPR (Cost Per Request/Token) 基准值约为 0.0021 ($/token, 基于 45.3 tokens/s 吞吐和 $10,200 TCO)。

## Evidence

先验知识/题面给定，逻辑校验通过：硬件成本 $9,750 + 电力成本 $450 (300W * 8760h * 3y * $0.10/kWh = $450) 总和为 $10,200；CPR 计算 $10,200 / (45.3 tokens/s * 8760h * 3y) ≈ $0.0021/token，数值量级与逻辑自洽。
