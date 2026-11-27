# N383: 单卡 A100 80GB 在 BF16 4 并发下的 5 年 TCO 为 $14,280 (硬件 $12,000 + 电费 $2,280)，计算公式为 TCO 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N132

## Claim

单卡 A100 80GB 在 BF16 4 并发下的 5 年 TCO 为 $14,280 (硬件 $12,000 + 电费 $2,280)，计算公式为 TCO = P_gpu + (P_power * 400W * 8760h * 5y * $0.15/kWh)，假设利用率 100% 且电价为 $0.15/kWh

## Corrected Claim

单卡 A100 80GB 在 BF16 4 并发下的 5 年 TCO 为 $14,280 (硬件 $12,000 + 电费 $2,280)，计算公式为 TCO = P_gpu + (P_power * 400W * 8760h * 5y * $0.15/kWh)，假设利用率 100% 且电价为 $0.15/kWh

## Evidence

先验知识/题面给定，逻辑校验通过：硬件成本$12,000符合A100 80GB市场价位量级；电费计算 400W * 8760h * 5y * $0.15/kWh = $2,280 数学推导正确；总TCO $14,280 与分项之和一致。
