# N161: 故障期间的用户体验损失成本C_outage = (L_P99_outage - T_target) * k_penalty * DAU * T_outage_d

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

故障期间的用户体验损失成本C_outage = (L_P99_outage - T_target) * k_penalty * DAU * T_outage_duration，其中L_P99_outage在故障期间可能飙升至500ms-1s（回源或排队），T_outage_duration为平均故障持续时间（MTTD+MTTR），该成本需纳入总成本模型，通常占年度总成本的1-5%，影响策略选择

## Corrected Claim

故障期间的用户体验损失成本C_outage = (L_P99_outage - T_target) * k_penalty * DAU * T_outage_duration，其中L_P99_outage在故障期间可能飙升至500ms-1s（回源或排队），T_outage_duration为平均故障持续时间（MTTD+MTTR），该成本需纳入总成本模型，通常占年度总成本的1-5%，影响策略选择

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN outage cost user experience loss calculation MTTD MTTR
