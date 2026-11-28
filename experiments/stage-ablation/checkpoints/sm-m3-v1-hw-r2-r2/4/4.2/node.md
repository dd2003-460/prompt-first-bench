# N18: 纯本地模式月度运营成本 $C_{local}$：电力成本约为 0.04 USD/kWh × 300W(平均功耗) × 24h × 30d ≈ 8.64 USD/

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

纯本地模式月度运营成本 $C_{local}$：电力成本约为 0.04 USD/kWh × 300W(平均功耗) × 24h × 30d ≈ 8.64 USD/月，忽略折旧与运维人力

## Corrected Claim

纯本地模式月度运营成本 $C_{local}$：电力成本约为 0.04 USD/kWh × 300W(平均功耗) × 24h × 30d ≈ 8.64 USD/月，忽略折旧与运维人力

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 0.04 * 300 * 24 * 30 = 8640 Wh * 0.04 USD/kWh = 8.64 USD，数值量级与算术逻辑均正确。

## Search Query

Tesla V100 SXM2 average power consumption vLLM idle vs active
