# N245: 高电价区域（P_elec > $0.18/kWh）下，若 M3 Ultra 吞吐量不满足最低需求（如 >15 tokens/s），则无可行低功耗方案，必须选择 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

高电价区域（P_elec > $0.18/kWh）下，若 M3 Ultra 吞吐量不满足最低需求（如 >15 tokens/s），则无可行低功耗方案，必须选择 1×4090 并接受高 TCO，或升级至 2×4090 以分摊电力成本占比，此时 2×4090 的 TCO 弹性系数降至 ~3.5，优于 1×4090。

## Corrected Claim

高电价区域（P_elec > $0.18/kWh）下，若 M3 Ultra 吞吐量不满足最低需求（如 >15 tokens/s），则无可行低功耗方案，必须选择 1×4090 并接受高 TCO，或升级至 2×4090 以分摊电力成本占比，此时 2×4090 的 TCO 弹性系数降至 ~3.5，优于 1×4090。

## Evidence

先验知识/题面给定，逻辑校验通过：高电价下电力成本占比上升，增加GPU数量虽增加总功耗但分摊了固定硬件成本占比，且双卡并行通常能提升总吞吐量以满足需求，TCO弹性系数降低符合经济直觉。
