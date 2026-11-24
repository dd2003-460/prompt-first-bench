# N167: 在 T=150ms 阈值下，公有云CDN的P99延迟（约160ms）超标（ΔT = 160 - 150 = 10ms > 0），不合规；而自建POP的P99延迟

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

在 T=150ms 阈值下，公有云CDN的P99延迟（约160ms）超标（ΔT = 160 - 150 = 10ms > 0），不合规；而自建POP的P99延迟（约150ms）处于边界（ΔT = 0），需依赖具体缓存命中率 H_pop > 0.95 才能确保合规。

## Corrected Claim

在 T=150ms 阈值下，公有云CDN的P99延迟（约160ms）超标（ΔT = 160 - 150 = 10ms > 0），不合规；而自建POP的P99延迟（约150ms）处于边界（ΔT = 0），需依赖具体缓存命中率 H_pop > 0.95 才能确保合规。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别解释了公有云CDN超标和自建POP处于边界这两种不同场景下的根因，两者互不重叠且共同覆盖了父节点中提到的两个主要实体（公有云CDN和自建POP）及其对应的状态（超标、边界），没有冗余。）

## Search Query

CDN P99 latency threshold 150ms compliance
