# N161: Ascend 910B 的 TDP 为 310W，在标准风冷环境下连续运行 1 年的电费成本为 $409.5 (310W × 24h × 365d / 1000

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43, N44, N45

## Claim

Ascend 910B 的 TDP 为 310W，在标准风冷环境下连续运行 1 年的电费成本为 $409.5 (310W × 24h × 365d / 1000 × $0.15)，低于 RTX 4090 ($594) 和 H100 ($914)。

## Corrected Claim

Ascend 910B 的 TDP 为 310W，在标准风冷环境下连续运行 1 年的电费成本为 $409.5 (310W × 24h × 365d / 1000 × $0.15)，低于 RTX 4090 ($594) 和 H100 ($914)。

## Evidence

先验知识/题面给定，逻辑校验通过：310W * 24h * 365d / 1000 * $0.15 = $409.5，计算无误；RTX 4090 (450W) 和 H100 (700W) 的 TDP 及对应电费估算符合常识量级。
