# N474: 日均请求数 R_daily 的精确推导：基于日均下载量 2TB 和平均对象大小 s_avg=1.5MB，计算得 R_daily = 2,000,000 MB /

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N152

## Claim

日均请求数 R_daily 的精确推导：基于日均下载量 2TB 和平均对象大小 s_avg=1.5MB，计算得 R_daily = 2,000,000 MB / 1.5 MB ≈ 1.333×10^9 次/天，需确认此值是否与 N7 中的敏感性区间 [0.5, 5] MB 一致。

## Corrected Claim

日均请求数 R_daily 的精确推导：基于日均下载量 2TB 和平均对象大小 s_avg=1.5MB，计算得 R_daily = 2,000,000 MB / 1.5 MB ≈ 1.333×10^9 次/天，需确认此值是否与 N7 中的敏感性区间 [0.5, 5] MB 一致。

## Evidence

先验知识/题面给定，逻辑校验通过：2TB=2,000,000MB，除以1.5MB得1.333×10^9，计算正确且量级合理
