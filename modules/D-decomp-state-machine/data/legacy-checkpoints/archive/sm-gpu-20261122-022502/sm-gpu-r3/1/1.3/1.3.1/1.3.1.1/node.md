# N124: Apple M2 Ultra 192GB 在 24/7 连续推理负载下的稳态功耗为 45-60W（峰值 120W），3年总电力成本约为 $100-150（基于 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

Apple M2 Ultra 192GB 在 24/7 连续推理负载下的稳态功耗为 45-60W（峰值 120W），3年总电力成本约为 $100-150（基于 $0.15/kWh），远低于 GPU 方案（$600-1000+）。

## Corrected Claim

Apple M2 Ultra 192GB 在 24/7 连续推理负载下的稳态功耗估计在 45-60W 区间（峰值可能更高），3年总电力成本约为 $100-150（基于 $0.15/kWh 及特定负载假设），通常低于同等性能 GPU 方案。

## Evidence

[质询]稳态功耗45-60W及峰值120W的具体数值缺乏公开基准测试支持，且3年总成本计算隐含了极高的电价或特定的负载持续率假设，与常规数据中心或家庭用电场景下的典型估算存在偏差，属于未经证实的经验性数据。 | 先验知识/题面给定，逻辑校验通过（量纲与量级在物理上合理，无内部矛盾），但作为经验事实缺乏直接来源支持，故降级。

## Search Query

Apple M2 Ultra Mac Studio sustained power consumption idle load watts
