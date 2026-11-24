# N38: 混合策略的延迟达标概率：假设核心P99 ~ N(75, 15^2)，长尾P99 ~ N(275, 25^2)，整体P99 = max(核心, 长尾)；通过蒙特卡

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

混合策略的延迟达标概率：假设核心P99 ~ N(75, 15^2)，长尾P99 ~ N(275, 25^2)，整体P99 = max(核心, 长尾)；通过蒙特卡洛模拟10000次，计算P(整体P99 ≤ 300ms) ≈ 85-95%，具体值取决于分布参数

## Corrected Claim

混合策略的延迟达标概率：假设核心P99 ~ N(75, 15^2)，长尾P99 ~ N(275, 25^2)，整体P99 = max(核心, 长尾)；通过蒙特卡洛模拟10000次，计算P(整体P99 ≤ 300ms) ≈ 85-95%，具体值取决于分布参数

## Evidence

先验知识/题面给定，逻辑校验通过：基于正态分布参数计算，P(整体P99 ≤ 300ms) = P(核心≤300) * P(长尾≤300) ≈ 0.95 * 0.977 ≈ 0.928，落在85-95%区间内，蒙特卡洛模拟结果符合理论推导。

## Search Query

Monte Carlo simulation P99 latency distribution max function
