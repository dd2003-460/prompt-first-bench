# N152: 境外流量处理策略的延迟代价量化：通过境内节点服务境外用户导致的P99延迟增加量 ΔL_overseas ≈ 75ms（取区间50-100ms中位值），该增量直接

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

境外流量处理策略的延迟代价量化：通过境内节点服务境外用户导致的P99延迟增加量 ΔL_overseas ≈ 75ms（取区间50-100ms中位值），该增量直接叠加到基础延迟L_base上，需评估是否导致P99 > T_target，若T_target=200ms且L_base=100ms，则ΔL_overseas=75ms使P99达到175ms，仍在阈值内，但若L_base=150ms则P99=225ms>200ms，触发违约

## Corrected Claim

境外流量处理策略的延迟代价量化：通过境内节点服务境外用户导致的P99延迟增加量 ΔL_overseas ≈ 75ms（取区间50-100ms中位值），该增量直接叠加到基础延迟L_base上，需评估是否导致P99 > T_target，若T_target=200ms且L_base=100ms，则ΔL_overseas=75ms使P99达到175ms，仍在阈值内，但若L_base=150ms则P99=225ms>200ms，触发违约

## Evidence

先验知识/题面给定，逻辑校验通过：算术推导（100+75=175<200, 150+75=225>200）正确，延迟叠加模型符合网络工程基本直觉，且作为knowledge节点无需外部来源支持。
