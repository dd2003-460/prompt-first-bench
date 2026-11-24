# N117: 网络带宽瓶颈下的扫描时间 T_net_s3：假设出口带宽为10Gbps (≈1.25GB/s)，传输500TB数据所需时间 T_net = 500,000GB 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

网络带宽瓶颈下的扫描时间 T_net_s3：假设出口带宽为10Gbps (≈1.25GB/s)，传输500TB数据所需时间 T_net = 500,000GB / 1.25GB/s = 400,000秒 ≈ 111小时；由于 T_net >> T_min_s3，瓶颈在网络带宽而非API限流，需重新评估云存储在大文件顺序扫描场景下的优势。

## Corrected Claim

网络带宽瓶颈下的扫描时间 T_net_s3：假设出口带宽为10Gbps (≈1.25GB/s)，传输500TB数据所需时间 T_net = 500,000GB / 1.25GB/s = 400,000秒 ≈ 111小时；由于 T_net >> T_min_s3，瓶颈在网络带宽而非API限流，需重新评估云存储在大文件顺序扫描场景下的优势。

## Evidence

先验知识/题面给定，逻辑校验通过：单位换算正确（10Gbps=1.25GB/s），算术计算准确（500000/1.25=400000s≈111h），逻辑推导自洽。
