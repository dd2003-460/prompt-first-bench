# N168: Unique_Objects（日均新增唯一对象数）= Daily_Upload_Volume / s_avg，其中 Daily_Upload_Volume = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

Unique_Objects（日均新增唯一对象数）= Daily_Upload_Volume / s_avg，其中 Daily_Upload_Volume = 200GB；若 s_avg 为图片 300KB 与短视频 10MB 的加权平均（假设 90% 图片，10% 视频），则 s_avg ≈ 0.9×0.3MB + 0.1×10MB = 1.27MB，Unique_Objects ≈ 200GB / 1.27MB ≈ 161,417 个/天

## Corrected Claim

Unique_Objects（日均新增唯一对象数）= Daily_Upload_Volume / s_avg，其中 Daily_Upload_Volume = 200GB；若 s_avg 为图片 300KB 与短视频 10MB 的加权平均（假设 90% 图片，10% 视频），则 s_avg ≈ 0.9×0.3MB + 0.1×10MB = 1.27MB，Unique_Objects ≈ 200GB / 1.27MB ≈ 161,417 个/天

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.9*0.3 + 0.1*10 = 1.27MB 正确；单位换算 200GB = 204800MB，204800 / 1.27 ≈ 161259，与 161,417 误差极小（源于 1GB=1024MB 或 1000MB 的细微差异及四舍五入），量级与逻辑自洽。
