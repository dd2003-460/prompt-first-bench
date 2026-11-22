# N138: S_signal 的边界条件：当 σ_S^2 > σ_threshold^2 时，信号噪声过大，买家无法有效区分正负信号，决策时间缩短效果减半，需估计 σ_th

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N44

## Claim

S_signal 的边界条件：当 σ_S^2 > σ_threshold^2 时，信号噪声过大，买家无法有效区分正负信号，决策时间缩短效果减半，需估计 σ_threshold^2 的具体数值，验证当前市场 σ_S^2 是否低于该阈值，否则信号机制失效。

## Corrected Claim

S_signal 的边界条件：当 σ_S^2 > σ_threshold^2 时，信号噪声过大，买家无法有效区分正负信号，决策时间缩短效果减半，需估计 σ_threshold^2 的具体数值，验证当前市场 σ_S^2 是否低于该阈值，否则信号机制失效。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

signal noise threshold variance boundary condition decision time shortening effectiveness
