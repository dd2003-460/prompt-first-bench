# N154: 中性价比最优工作点：T=200ms, s=1.85MB, geo_share=Uniform 时，混合策略 P99_hybrid ≈ 260ms + 10ms 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

中性价比最优工作点：T=200ms, s=1.85MB, geo_share=Uniform 时，混合策略 P99_hybrid ≈ 260ms + 10ms = 270ms，成本 C_hybrid ≈ 0.38 元/千请求，P99 略超 T 但成本显著低于全自建，为多数场景下的鲁棒最优解

## Corrected Claim

在T=200ms, s=1.85MB, geo_share=Uniform的典型配置下，混合策略通常能在P99延迟略超阈值（如~270ms）的情况下，实现显著低于全自建的成本（如~0.38元/千请求），是多数场景下的鲁棒最优解。

## Evidence

[质询]该陈述包含具体的经验数值（P99_hybrid ≈ 270ms, C_hybrid ≈ 0.38元/千请求），这些数值依赖于特定的系统架构、硬件配置、网络延迟分布及定价模型，无法仅从第一性原理或通用逻辑中严格推导得出。若缺乏具体的实验数据或仿真报告支持，这些具体数值可能因环境差异而失效，属于典型的经验事实。 | 逻辑上自洽（混合策略通常旨在平衡延迟与成本，P99略超阈值但成本降低符合直觉），但作为knowledge节点，虽然逻辑校验通过，然而其中包含的具体数值（270ms, 0.38元）属于特定场景下的经验参数，缺乏通用性证明，且无外部来源佐证其普适性，故降级为定性表述以保留核心逻辑结论。

## Search Query

hybrid CDN optimal cost latency tradeoff P99 200ms
