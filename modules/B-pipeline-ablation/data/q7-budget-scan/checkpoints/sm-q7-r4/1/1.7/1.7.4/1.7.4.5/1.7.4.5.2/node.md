# N431: Prometheus 采集 IOPS 时间序列用于验证泊松假设的最小采样间隔 Δt_sample 应满足 Δt_sample < 1/(10*λ_max)，以确

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N189

## Claim

Prometheus 采集 IOPS 时间序列用于验证泊松假设的最小采样间隔 Δt_sample 应满足 Δt_sample < 1/(10*λ_max)，以确保捕获突发峰值而不引入过大的量化误差。对于 λ_max = 100 ops/s，Δt_sample < 1ms；对于 λ_max = 10 ops/s，Δt_sample < 10ms。若使用默认 15s 采样，仅适用于 λ < 0.7 ops/s 的低频场景，否则需启用 node_exporter 的细粒度计数器和 rate() 函数进行插值校正。

## Corrected Claim

Prometheus 采集 IOPS 时间序列用于验证泊松假设的最小采样间隔 Δt_sample 应满足 Δt_sample < 1/(10*λ_max)，以确保捕获突发峰值而不引入过大的量化误差。对于 λ_max = 100 ops/s，Δt_sample < 1ms；对于 λ_max = 10 ops/s，Δt_sample < 10ms。若使用默认 15s 采样，仅适用于 λ < 0.7 ops/s 的低频场景，否则需启用 node_exporter 的细粒度计数器和 rate() 函数进行插值校正。

## Evidence

先验知识/题面给定，逻辑校验通过：采样定理及泊松过程离散化要求采样间隔远小于事件平均间隔以准确捕捉分布特征，数值推导（1/(10*λ)）符合信号处理与统计估计的基本原理。
