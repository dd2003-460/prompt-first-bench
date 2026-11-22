# N146: 工作点 B (中匹配率-中等待)：假设 M_rate = 0.5, E[T_wait|NoMatch] = 45天, E[T_decision] = 2天，计算

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

工作点 B (中匹配率-中等待)：假设 M_rate = 0.5, E[T_wait|NoMatch] = 45天, E[T_decision] = 2天，计算 E[T_cycle] = 0.5 * 45 + 0.5 * 2 = 23.5 天，对应中等流量、15-25% 溢价场景，分析该点是否为当前均衡的主要构成部分。

## Corrected Claim

工作点 B (中匹配率-中等待)：假设 M_rate = 0.5, E[T_wait|NoMatch] = 45天, E[T_decision] = 2天，计算 E[T_cycle] = 0.5 * 45 + 0.5 * 2 = 23.5 天，对应中等流量、15-25% 溢价场景，分析该点是否为当前均衡的主要构成部分。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 0.5*45 + 0.5*2 = 23.5 正确，且符合全期望公式逻辑。

## Search Query

expected cycle time calculation medium match rate moderate waiting time
