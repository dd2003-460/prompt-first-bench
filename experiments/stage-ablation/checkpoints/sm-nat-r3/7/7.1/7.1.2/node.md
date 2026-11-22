# N266: 工作点 B（典型 CDN）：假设 r_max = 100 * r_min（常见热度分布范围），计算截断 Pareto(β=0.9) 的 C_req(0.1)，量

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N93

## Claim

工作点 B（典型 CDN）：假设 r_max = 100 * r_min（常见热度分布范围），计算截断 Pareto(β=0.9) 的 C_req(0.1)，量化头部 10% 对象覆盖的请求量比例，作为基准场景的命中率修正因子。

## Corrected Claim

工作点 B（典型 CDN）：假设 r_max = 100 * r_min，基于 Pareto(β=0.9) 分布计算头部 10% 对象覆盖的请求量比例，作为基准场景的命中率修正因子（具体数值需依据实际计算或权威数据源确认）。

## Evidence

[质询]该陈述包含具体的经验性假设（r_max = 100 * r_min）和特定的计算结果（C_req(0.1) 的具体数值隐含在“量化...比例”中，虽未给出具体数字，但作为基准场景的修正因子，其具体数值依赖于未提供的计算过程或外部数据）。作为 source=search 的节点，缺乏外部来源支持具体的数值结果或该特定假设的普遍适用性。 | 逻辑上，Pareto 分布用于描述 CDN 对象热度是合理的，且 r_max/r_min 的设定在量级上符合常见长尾分布特征。但根据经验事实排除条款，具体的参数假设和计算结果属于经验事实，且本轮检索无可用来源，无法验证具体数值或假设的权威性，故降级。

## Search Query

typical CDN request popularity Pareto beta 0.9 top 10 percent coverage ratio
