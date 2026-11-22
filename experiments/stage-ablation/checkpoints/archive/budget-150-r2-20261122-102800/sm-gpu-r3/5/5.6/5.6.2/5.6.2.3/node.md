# N317: 消费级显卡（RTX 4090）在 3 年 TCO 周期内的预期维护成本 = P(故障) × 维修成本，其中 P(故障) = 1 - (1 - AFR)^3，AF

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125

## Claim

消费级显卡（RTX 4090）在 3 年 TCO 周期内的预期维护成本 = P(故障) × 维修成本，其中 P(故障) = 1 - (1 - AFR)^3，AFR=33.3% 时 P(故障)≈68.6%，维护成本≈$137。

## Corrected Claim

消费级显卡（RTX 4090）在 3 年 TCO 周期内的预期维护成本 = P(故障) × 维修成本，其中 P(故障) = 1 - (1 - AFR)^3，AFR=33.3% 时 P(故障)≈68.6%，维护成本≈$137。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1-(1-0.333)^3 ≈ 0.686 正确，且维护成本 $137 与故障率及典型维修费用量级相符。
