# N210: 跨网接入惩罚项 ΔT_cross_net = 15ms，当用户运营商与 CDN 节点接入运营商不一致时（中国三大运营商跨网场景），P99 延迟增加 15ms（基

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

跨网接入惩罚项 ΔT_cross_net = 15ms，当用户运营商与 CDN 节点接入运营商不一致时（中国三大运营商跨网场景），P99 延迟增加 15ms（基于 N184/N192 的 10-20ms 区间取中值），需叠加到基础 RTT 上

## Corrected Claim

跨网接入惩罚项 ΔT_cross_net = 15ms，当用户运营商与 CDN 节点接入运营商不一致时（中国三大运营商跨网场景），P99 延迟增加 15ms（基于 N184/N192 的 10-20ms 区间取中值），需叠加到基础 RTT 上

## Evidence

先验知识/题面给定，逻辑校验通过
