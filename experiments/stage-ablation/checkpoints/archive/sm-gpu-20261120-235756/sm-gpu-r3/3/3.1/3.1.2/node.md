# N65: 电力消耗 W 的具体数值需根据 GPU TDP 及系统整体功耗确定：RTX 4090 系统总功耗约 600W (GPU 450W + 系统 150W)，A100

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16, N17, N18

## Claim

电力消耗 W 的具体数值需根据 GPU TDP 及系统整体功耗确定：RTX 4090 系统总功耗约 600W (GPU 450W + 系统 150W)，A100 SXM 系统总功耗约 550W (GPU 400W + 系统 150W)，需代入 TCO 公式计算年电费差异。

## Corrected Claim

电力消耗 W 的具体数值需根据 GPU TDP 及系统整体功耗确定：RTX 4090 系统总功耗约 600W (GPU 450W + 系统 150W)，A100 SXM 系统总功耗约 550W (GPU 400W + 系统 150W)，需代入 TCO 公式计算年电费差异。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP 450W 与 A100 SXM TDP 400W 符合官方规格，系统额外功耗 150W 在合理工程估算范围内，总功耗数值量级正确且逻辑自洽。
