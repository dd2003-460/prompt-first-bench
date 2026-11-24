# N542: 核心区域 P99 延迟贡献权重分解：W_p99_core = Σ(w_i * L_p99_i) / Σ(w_i) 对于 i ∈ Core_Cities，其中 w

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N176

## Claim

核心区域 P99 延迟贡献权重分解：W_p99_core = Σ(w_i * L_p99_i) / Σ(w_i) 对于 i ∈ Core_Cities，其中 w_i 为各城市请求占比，L_p99_i 为该城市用户 P99 延迟；由于核心区域用户占 80%，其延迟对整体 P99 的加权影响为 0.8 * L_p99_core_avg，而长尾区域 0.2 * L_p99_tail_avg；此分解用于评估核心区域优化对整体 P99 的杠杆效应。

## Corrected Claim

核心区域 P99 延迟贡献权重分解：W_p99_core = Σ(w_i * L_p99_i) / Σ(w_i) 对于 i ∈ Core_Cities，其中 w_i 为各城市请求占比，L_p99_i 为该城市用户 P99 延迟；由于核心区域用户占 80%，其延迟对整体 P99 的加权影响为 0.8 * L_p99_core_avg，而长尾区域 0.2 * L_p99_tail_avg；此分解用于评估核心区域优化对整体 P99 的杠杆效应。

## Evidence

先验知识/题面给定，逻辑校验通过
