# N589: 部署多线 BGP 后，跨网延迟惩罚 ΔT_cross 的剩余值 ΔT_bgp_residual 约为 5-8ms，主要源于运营商内部路由优化而非物理路径，导致 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N192

## Claim

部署多线 BGP 后，跨网延迟惩罚 ΔT_cross 的剩余值 ΔT_bgp_residual 约为 5-8ms，主要源于运营商内部路由优化而非物理路径，导致 P99 延迟从 '同网+15ms' 降至 '同网+5ms'。

## Corrected Claim

部署多线 BGP 后，跨网延迟惩罚 ΔT_cross 的剩余值 ΔT_bgp_residual 通常显著降低（具体数值视网络环境而定），主要源于运营商内部路由优化，从而降低 P99 延迟。

## Evidence

[质询]该陈述包含具体的经验数值（5-8ms, 15ms, 5ms），属于网络工程中的经验事实，无法从第一性原理严格推导，且缺乏来源支持具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

BGP multi-line access residual cross-network latency penalty China CDN
