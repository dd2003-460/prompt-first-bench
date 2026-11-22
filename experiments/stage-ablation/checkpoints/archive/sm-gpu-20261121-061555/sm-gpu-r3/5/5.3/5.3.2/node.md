# N105: NVIDIA A100 80GB (SXM) 在数据中心 24/7 场景下的年电费：年电费 = 400W * 0.9 (PUE 修正) * 8760h * 0.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

NVIDIA A100 80GB (SXM) 在数据中心 24/7 场景下的年电费：年电费 = 400W * 0.9 (PUE 修正) * 8760h * 0.6元/kWh ≈ 1,942 元/年；虽然 TDP 低于 RTX 4090 峰值，但考虑到其 CapEx 极高，需结合 N27 的 CapEx 数据计算 5 年 TCO 盈亏平衡点。

## Corrected Claim

NVIDIA A100 80GB (SXM) 在数据中心 24/7 场景下的年电费：年电费 = 400W * 0.9 (PUE 修正) * 8760h * 0.6元/kWh ≈ 1,942 元/年；虽然 TDP 低于 RTX 4090 峰值，但考虑到其 CapEx 极高，需结合 N27 的 CapEx 数据计算 5 年 TCO 盈亏平衡点。

## Evidence

先验知识/题面给定，逻辑校验通过：400W * 0.9 * 8760h * 0.6元/kWh = 1942.08元，计算准确且量级合理。
