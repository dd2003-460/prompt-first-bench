# N174: 地理分布变动的边界条件：当核心区域流量占比 P_core < 60% 时，自建POP的固定成本摊销 C_fixed_per_req 无法被足够高的缓存命中率抵消

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N44

## Claim

地理分布变动的边界条件：当核心区域流量占比 P_core < 60% 时，自建POP的固定成本摊销 C_fixed_per_req 无法被足够高的缓存命中率抵消，混合策略的总成本 C_total_mix 将高于全公有云策略，此时应放弃混合策略。

## Corrected Claim

地理分布变动的边界条件：当核心区域流量占比 P_core 低于特定临界值（该值取决于缓存命中率、固定成本摊销及公有云单价，通常需通过成本模型计算得出，而非固定为 60%）时，自建 POP 的固定成本摊销 C_fixed_per_req 无法被足够高的缓存命中率抵消，混合策略的总成本 C_total_mix 将高于全公有云策略，此时应放弃混合策略。

## Evidence

[质询]60% 是一个具体的经验阈值，缺乏通用的理论推导支持，不同业务场景（如缓存命中率、带宽成本、POP 建设成本）下该临界值会显著波动，直接断言 60% 为通用边界条件存在过度泛化风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Hybrid CDN break-even point core region traffic ratio
