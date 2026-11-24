# N395: 源站冗余度对弹性系数 E_infra 的修正：E_infra = (1 - H_new) / (1 - H_base) / Redundancy_Factor，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N130, N131, N132

## Claim

源站冗余度对弹性系数 E_infra 的修正：E_infra = (1 - H_new) / (1 - H_base) / Redundancy_Factor，其中 Redundancy_Factor 反映源站现有冗余能力；若源站已预留 50% 冗余（Redundancy_Factor = 1.5），则 E_infra = 2.8 / 1.5 = 1.87；若无冗余（Redundancy_Factor = 1.0），则 E_infra = 2.8，说明冗余度越高，成本弹性越低。

## Corrected Claim

源站冗余度对弹性系数 E_infra 的修正：E_infra = (1 - H_new) / (1 - H_base) / Redundancy_Factor，其中 Redundancy_Factor 反映源站现有冗余能力；若源站已预留 50% 冗余（Redundancy_Factor = 1.5），则 E_infra = 2.8 / 1.5 = 1.87；若无冗余（Redundancy_Factor = 1.0），则 E_infra = 2.8，说明冗余度越高，成本弹性越低。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义与数值计算（2.8/1.5≈1.87, 2.8/1.0=2.8）一致，且符合冗余度降低边际成本的经济学直觉。

## Search Query

CDN origin server redundancy elasticity cost
