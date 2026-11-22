# N68: 多卡总电力消耗 = (单卡 TDP × 卡数) + 系统基础功耗 + 互联组件功耗，例如 2×RTX 4090 总功耗约 1050W (450W×2 + 150

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16, N17, N18

## Claim

多卡总电力消耗 = (单卡 TDP × 卡数) + 系统基础功耗 + 互联组件功耗，例如 2×RTX 4090 总功耗约 1050W (450W×2 + 150W)，2×A100 SXM 总功耗约 950W (400W×2 + 150W)，需代入 TCO 公式计算年电费。

## Corrected Claim

多卡总电力消耗 = (单卡 TDP × 卡数) + 系统基础功耗 + 互联组件功耗，例如 2×RTX 4090 总功耗约 1050W (450W×2 + 150W)，2×A100 SXM 总功耗约 950W (400W×2 + 150W)，需代入 TCO 公式计算年电费。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP 450W 与 A100 SXM TDP 400W 符合硬件规格常识，系统基础功耗 150W 量级合理，公式逻辑自洽。
