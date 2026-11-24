# N559: 同网跨省 RTT 的骨干网路由质量修正项 ΔT_backbone (ms)：电信骨干网（ChinaNet）跨省 P99 延迟通常比联通（ChinaUnicom）

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N183

## Claim

同网跨省 RTT 的骨干网路由质量修正项 ΔT_backbone (ms)：电信骨干网（ChinaNet）跨省 P99 延迟通常比联通（ChinaUnicom）低 5-10ms，移动（ChinaMobile）在跨省高负载时段 P99 延迟比电信高 10-20ms，该差异源于骨干网带宽冗余度与 QoS 策略不同。

## Corrected Claim

同网跨省 RTT 的骨干网路由质量修正项 ΔT_backbone (ms)：电信骨干网（ChinaNet）跨省 P99 延迟通常优于联通（ChinaUnicom），移动（ChinaMobile）在跨省高负载时段 P99 延迟通常高于电信，该差异源于骨干网带宽冗余度与 QoS 策略不同。

## Evidence

[质询]具体数值区间（5-10ms, 10-20ms）属于经验性观测数据，缺乏实时或特定历史时期的权威基准测试支持，且不同时期、不同省份间差异巨大，固定区间可能不准确。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

China Telecom vs China Unicom vs China Mobile cross-province backbone RTT P99 latency comparison 2023 2024
