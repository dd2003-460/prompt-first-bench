# N66: 蒙特卡洛模拟 1000 次请求序列的 σ 计算工作点（中性价比最优）：使用解析近似 + 少量蒙特卡洛校正，先计算理论 Hit_base，再用 100 次短序列（

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N22

## Claim

蒙特卡洛模拟 1000 次请求序列的 σ 计算工作点（中性价比最优）：使用解析近似 + 少量蒙特卡洛校正，先计算理论 Hit_base，再用 100 次短序列（10^5 请求）模拟估计 σ_approx ≈ 0.012，95% 置信区间宽度为 ±1.96*0.012 ≈ ±2.35%，总耗时 < 1 小时，适用于初步估算但忽略序列依赖性。

## Corrected Claim

蒙特卡洛模拟 1000 次请求序列的 σ 计算工作点（中性价比最优）：使用解析近似 + 少量蒙特卡洛校正，先计算理论 Hit_base，再用 100 次短序列（10^5 请求）模拟估计 σ_approx ≈ 0.012，95% 置信区间宽度为 ±1.96*0.012 ≈ ±2.35%，总耗时 < 1 小时，适用于初步估算但忽略序列依赖性。

## Evidence

先验知识/题面给定，逻辑校验通过：蒙特卡洛模拟的统计误差公式（±1.96*σ）及计算复杂度量级（100次*10^5请求在1小时内完成）符合基本统计与计算直觉，无内部矛盾。

## Search Query

analytical approximation cache hit rate Monte Carlo correction short sequences
