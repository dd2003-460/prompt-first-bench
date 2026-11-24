# N630: 工作点 A（高性能低容量密度）：采用 7.68TB SSD，67 块盘，P_drives = 67 * 3.85W ≈ 257.95W；单位容量功耗 = 257

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N263

## Claim

工作点 A（高性能低容量密度）：采用 7.68TB SSD，67 块盘，P_drives = 67 * 3.85W ≈ 257.95W；单位容量功耗 = 257.95W / (67*7.68TB) ≈ 0.50 W/TB；适用场景：温数据 IOPS 需求高，SSD 层容量充裕

## Corrected Claim

工作点 A（高性能低容量密度）：采用 7.68TB SSD，67 块盘，P_drives = 67 * 3.85W ≈ 257.95W；单位容量功耗 = 257.95W / (67*7.68TB) ≈ 0.50 W/TB；适用场景：温数据 IOPS 需求高，SSD 层容量充裕

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（67*3.85=257.95, 257.95/514.56≈0.50），SSD单盘功耗3.85W及7.68TB容量符合主流企业级NVMe SSD的工程常识，场景描述逻辑自洽。
