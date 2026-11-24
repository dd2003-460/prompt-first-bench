# N535: 工作点C中SSD层的实际静态功耗修正：采用企业级NVMe SSD典型Idle功耗5-10W/盘（非0.8W/TB的估算值），假设50TB由25块2TB SSD组

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N176

## Claim

工作点C中SSD层的实际静态功耗修正：采用企业级NVMe SSD典型Idle功耗5-10W/盘（非0.8W/TB的估算值），假设50TB由25块2TB SSD组成，则P_ssd_idle = 25 * 7.5W = 187.5W，远高于原假设的40W。

## Corrected Claim

工作点C中SSD层的实际静态功耗修正：采用企业级NVMe SSD典型Idle功耗5-10W/盘（非0.8W/TB的估算值），假设50TB由25块2TB SSD组成，则P_ssd_idle = 25 * 7.5W = 187.5W，远高于原假设的40W。

## Evidence

先验知识/题面给定，逻辑校验通过：企业级NVMe SSD空闲功耗通常在5-10W范围，25块盘总功耗187.5W符合物理直觉及工程常识，远大于按容量线性估算的40W，逻辑自洽。
