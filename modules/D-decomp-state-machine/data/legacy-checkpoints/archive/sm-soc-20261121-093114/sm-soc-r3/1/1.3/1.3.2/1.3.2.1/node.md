# N108: 阈值 σ_threshold 的估计：σ_threshold 为买家区分信号与噪声的最小感知差异，量化为 σ_threshold = k * σ_percept

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N34

## Claim

阈值 σ_threshold 的估计：σ_threshold 为买家区分信号与噪声的最小感知差异，量化为 σ_threshold = k * σ_perception，其中 k 为感知灵敏度系数，通常 k ∈ [1, 2]，需通过 A/B 测试确定具体值。

## Corrected Claim

阈值 σ_threshold 的估计：σ_threshold 为买家区分信号与噪声的最小感知差异，量化为 σ_threshold = k * σ_perception，其中 k 为感知灵敏度系数，通常 k ∈ [1, 2]，需通过 A/B 测试确定具体值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

perception threshold coefficient signal noise discrimination A/B test
