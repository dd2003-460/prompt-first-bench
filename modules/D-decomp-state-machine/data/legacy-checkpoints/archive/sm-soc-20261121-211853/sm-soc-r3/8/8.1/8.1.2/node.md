# N161: 偏离度D的稳健性修正：为避免极端离群值（如挂价0元或天价）扭曲P95，需先对D进行Winsorize处理（截断在1st和99th百分位），再计算P95。修正后的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

偏离度D的稳健性修正：为避免极端离群值（如挂价0元或天价）扭曲P95，需先对D进行Winsorize处理（截断在1st和99th百分位），再计算P95。修正后的P95与原始P95的差值ΔP95若超过2%，则需重新校准触发线。

## Corrected Claim

偏离度D的稳健性修正：为避免极端离群值（如挂价0元或天价）扭曲P95，需先对D进行Winsorize处理（截断在1st和99th百分位），再计算P95。修正后的P95与原始P95的差值ΔP95若超过2%，则需重新校准触发线。

## Evidence

先验知识/题面给定，逻辑校验通过：Winsorize处理极端离群值以保护分位数计算是统计学标准稳健性做法，逻辑自洽且量级合理。
