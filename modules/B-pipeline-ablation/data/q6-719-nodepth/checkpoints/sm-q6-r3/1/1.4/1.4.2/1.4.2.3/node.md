# N180: 请求数与对象大小的耦合验证：若 R_total = 100M 次/天，s_avg = 3.6MB，则理论下载量为 360TB/天，与题面 2TB/天 严重不符，

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

请求数与对象大小的耦合验证：若 R_total = 100M 次/天，s_avg = 3.6MB，则理论下载量为 360TB/天，与题面 2TB/天 严重不符，表明题面数据隐含了高缓存命中率（Hit_Rate > 99%）或 R_per_user 实际远低于 20，需重新校准 R_per_user 或确认缓存命中率假设

## Corrected Claim

请求数与对象大小的耦合验证：若 R_total = 100M 次/天，s_avg = 3.6MB，则理论下载量为 360TB/天，与题面 2TB/天 严重不符，表明题面数据隐含了高缓存命中率（Hit_Rate > 99%）或 R_per_user 实际远低于 20，需重新校准 R_per_user 或确认缓存命中率假设

## Evidence

先验知识/题面给定，逻辑校验通过：100,000,000 * 3.6MB = 360,000,000MB = 360TB，与2TB/天存在巨大差异，推导出的缓存命中率需求（>99.4%）在逻辑上自洽且符合高缓存场景的工程直觉。
