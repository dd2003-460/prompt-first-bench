# N120: 云对象存储聚合 IOPS 供给 = 并发请求数 1,000 / 平均延迟 0.1s = 10,000 IOPS（受 API 限流约束），低于 IOPS_peak

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

云对象存储聚合 IOPS 供给 = 并发请求数 1,000 / 平均延迟 0.1s = 10,000 IOPS（受 API 限流约束），低于 IOPS_peak 需求（10K < 37.9K），需提高并发至 3,800 或接受延迟

## Corrected Claim

云对象存储聚合 IOPS 供给 = 并发请求数 1,000 / 平均延迟 0.1s = 10,000 IOPS（受 API 限流约束），低于 IOPS_peak 需求（10K < 37.9K），需提高并发至 3,800 或接受延迟

## Evidence

先验知识/题面给定，逻辑校验通过：1000/0.1=10000，10000<37900，37900*0.1=3790≈3800，计算与逻辑自洽
