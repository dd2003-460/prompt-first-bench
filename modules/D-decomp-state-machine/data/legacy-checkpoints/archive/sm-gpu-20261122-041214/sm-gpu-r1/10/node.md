# N48: 利用率因子 (Utilization Factor) 假设：对于本地工作站单用户场景，GPU 利用率通常远低于数据中心（假设 20-30%），因为存在空闲时间。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

利用率因子 (Utilization Factor) 假设：对于本地工作站单用户场景，GPU 利用率通常远低于数据中心（假设 20-30%），因为存在空闲时间。在 TCO 计算中，若按 100% 负载计算会低估实际单位成本，需引入 0.2-0.3 的利用率系数修正总吞吐量 [待核验]。

## Corrected Claim

利用率因子 (Utilization Factor) 假设：对于本地工作站单用户场景，GPU 利用率通常远低于数据中心（具体数值视工作负载而定，常显著低于满载），因为存在空闲时间。在 TCO 计算中，若按 100% 负载计算会低估实际单位成本，需引入利用率系数修正总吞吐量。

## Evidence

[质询]具体数值范围（20-30%）属于经验性估计，缺乏普遍适用的标准或权威数据支持，不同工作负载下差异巨大，且来源仅定义了概念而未提供该特定场景的数值。 | 来源[1]仅定义了利用率因子的概念（使用时间与总时间之比），未提供本地工作站GPU利用率的具体数值范围（20-30%）；该数值为经验事实，逻辑上合理（单用户空闲时间多）但缺乏直接来源支持，故降级。

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Utilization_factor&rut=e7ab52560207d94f1c119bf67cd51e34f906bbb058e5c00e244fba5a31300eb9', 'type': 'ddg', 'title': 'Utilization factor - Wikipedia'}
