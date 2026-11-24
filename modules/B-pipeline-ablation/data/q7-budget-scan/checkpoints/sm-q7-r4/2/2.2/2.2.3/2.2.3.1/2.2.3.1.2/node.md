# N536: 工作点C中HDD层的实际静态功耗修正：采用企业级HDD典型Idle功耗6W/盘（非0.4W/TB的估算值），假设450TB由28块16TB HDD组成，则P_h

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N176

## Claim

工作点C中HDD层的实际静态功耗修正：采用企业级HDD典型Idle功耗6W/盘（非0.4W/TB的估算值），假设450TB由28块16TB HDD组成，则P_hdd_idle = 28 * 6W = 168W，与原假设的180W基本一致但需明确盘数假设。

## Corrected Claim

工作点C中HDD层的实际静态功耗修正：采用企业级HDD典型Idle功耗6W/盘（非0.4W/TB的估算值），假设450TB由28块16TB HDD组成，则P_hdd_idle = 28 * 6W = 168W，与原假设的180W基本一致但需明确盘数假设。

## Evidence

先验知识/题面给定，逻辑校验通过：28块16TB硬盘总容量448TB≈450TB，单盘6W Idle功耗符合企业级HDD典型范围，计算28*6=168W无误，与180W偏差在合理误差范围内。
