# N7: 网络抖动 (Jitter) 对 P99 的影响：P99_RTT ≈ RTT_mean + 3 × σ_RTT，其中 σ_RTT 取决于链路拥塞程度与路由跳数，通

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

网络抖动 (Jitter) 对 P99 的影响：P99_RTT ≈ RTT_mean + 3 × σ_RTT，其中 σ_RTT 取决于链路拥塞程度与路由跳数，通常每跳增加 1-5ms 抖动 [待核验]。

## Corrected Claim

网络抖动 (Jitter) 显著影响 P99 延迟。在近似正态分布的短链路场景中，P99_RTT 可粗略估计为 RTT_mean + 3 × σ_RTT；但在长尾分布的实际网络中，P99 通常远高于此线性估计。σ_RTT 受链路拥塞与路由跳数影响，典型单跳抖动贡献在毫秒级（如 1-5ms），但具体数值高度依赖网络拓扑与负载状况。

## Evidence

[质询]P99 与均值及标准差的线性关系（P99 ≈ Mean + 3σ）仅在正态分布假设下近似成立，而网络延迟分布通常呈长尾（如帕累托或混合分布），此时 P99 往往远大于 Mean + 3σ；此外，'每跳增加 1-5ms 抖动' 是一个高度依赖具体网络环境（如骨干网 vs 接入网、有线 vs 无线）的经验值，缺乏普适性，且不同跳数的贡献并非简单的线性叠加。 | 先验知识/题面给定，逻辑校验通过但存在统计假设局限（正态分布假设不适用于长尾网络延迟）及经验参数泛化风险，故降级为定性表述。

## Search Query

network jitter P99 latency impact per hop ms
