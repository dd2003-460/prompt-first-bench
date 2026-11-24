# N111: 队列延迟 Q_delay 的 M/M/1 模型估算：Q_delay = (ρ / (μ * (1 - ρ)))，其中 ρ 为服务器利用率，μ 为服务率（1/平均

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22, N23, N24

## Claim

队列延迟 Q_delay 的 M/M/1 模型估算：Q_delay = (ρ / (μ * (1 - ρ)))，其中 ρ 为服务器利用率，μ 为服务率（1/平均服务时间）；当 ρ=0.8 且平均服务时间 5ms 时，Q_delay ≈ 20ms，显著影响 P99 延迟

## Corrected Claim

队列延迟 Q_delay 的 M/M/1 模型估算：Q_delay = (ρ / (μ * (1 - ρ)))，其中 ρ 为服务器利用率，μ 为服务率（1/平均服务时间）；当 ρ=0.8 且平均服务时间 5ms 时，Q_delay ≈ 20ms，显著影响 P99 延迟

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/1 队列平均等待时间公式为 Wq = ρ/(μ(1-ρ))，代入 ρ=0.8, μ=1/5ms=0.2ms⁻¹ 计算得 0.8/(0.2*0.2)=20ms，数值与逻辑均正确。

## Search Query

M/M/1 queueing delay formula CDN edge node
