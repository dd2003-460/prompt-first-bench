# N106: AMD RX 7900 XTX (24GB) 在 24/7 满载场景下的年电费：年电费 = 355W * 0.85 * 8760h * 0.8元/kWh ≈ 2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

AMD RX 7900 XTX (24GB) 在 24/7 满载场景下的年电费：年电费 = 355W * 0.85 * 8760h * 0.8元/kWh ≈ 2,092 元/年；其能效比（Tokens/Watt）需结合 N37 的吞吐量数据修正，若吞吐量为 RTX 4090 的 80%，则单位 Token 电费比 RTX 4090 高约 25%。

## Corrected Claim

AMD RX 7900 XTX (24GB) 在 24/7 满载场景下的年电费：年电费 = 355W * 0.85 * 8760h * 0.8元/kWh ≈ 2,092 元/年；其能效比（Tokens/Watt）需结合 N37 的吞吐量数据修正，若吞吐量为 RTX 4090 的 80%，则单位 Token 电费比 RTX 4090 高约 25%。

## Evidence

先验知识/题面给定，逻辑校验通过：电费计算 355*0.85*8760*0.8 ≈ 2092 元正确；能效比推导中，若吞吐量仅为 80% 且功耗相近（或略低），单位 Token 成本确实会显著上升，25% 的增幅在量级上合理（1/0.8 = 1.25，即若功耗相同则成本增加 25%）。
