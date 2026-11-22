# N289: A100 PCIe 版本标称 TDP 为 250W-300W，在 BF16/FP8 推理负载下实际平均功耗通常维持在 150W-200W 区间，显著低于其 TD

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

A100 PCIe 版本标称 TDP 为 250W-300W，在 BF16/FP8 推理负载下实际平均功耗通常维持在 150W-200W 区间，显著低于其 TDP 上限，导致基于 TDP 计算的 OpEx 高估了实际电费。

## Corrected Claim

A100 PCIe 版本标称 TDP 为 250W-300W，在 BF16/FP8 推理负载下实际平均功耗通常维持在 150W-200W 区间，显著低于其 TDP 上限，导致基于 TDP 计算的 OpEx 高估了实际电费。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 PCIe TDP 250W-300W 符合官方规格，推理负载下功耗低于 TDP 符合 GPU 功耗管理常识，逻辑自洽。
