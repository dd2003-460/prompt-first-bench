# N145: 工作点 A (高匹配率-低等待)：假设 M_rate = 0.8, E[T_wait|NoMatch] = 30天, E[T_decision] = 1天，计算

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

工作点 A (高匹配率-低等待)：假设 M_rate = 0.8, E[T_wait|NoMatch] = 30天, E[T_decision] = 1天，计算 E[T_cycle] = 0.2 * 30 + 0.8 * 1 = 6.8 天，对应高流量、低溢价场景，验证是否短于市场平均周期。

## Corrected Claim

工作点 A (高匹配率-低等待)：假设 M_rate = 0.8, E[T_wait|NoMatch] = 30天, E[T_decision] = 1天，计算 E[T_cycle] = 0.2 * 30 + 0.8 * 1 = 6.8 天，对应高流量、低溢价场景，验证是否短于市场平均周期。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 0.2*30 + 0.8*1 = 6.8 正确，且符合全期望公式逻辑。

## Search Query

expected cycle time calculation high match rate low waiting time
