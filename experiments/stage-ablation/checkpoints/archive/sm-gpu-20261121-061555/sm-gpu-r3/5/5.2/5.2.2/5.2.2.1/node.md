# N284: 2x RTX 4090 多卡系统满载时的总系统功耗（System_Power_Draw）= 2 * 450W (GPU TDP) + 150W (CPU/RAM

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

2x RTX 4090 多卡系统满载时的总系统功耗（System_Power_Draw）= 2 * 450W (GPU TDP) + 150W (CPU/RAM/Storage/Misc) ≈ 1050W，此值为 PSU 选型依据，决定 PSU 需具备 ≥1200W 额定功率。

## Corrected Claim

2x RTX 4090 多卡系统满载时的总系统功耗（System_Power_Draw）= 2 * 450W (GPU TDP) + 150W (CPU/RAM/Storage/Misc) ≈ 1050W，此值为 PSU 选型依据，决定 PSU 需具备 ≥1200W 额定功率。

## Evidence

先验知识/题面给定，逻辑校验通过：2x450W+150W=1050W，且1200W PSU符合80%负载选型原则
