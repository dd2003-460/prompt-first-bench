# N359: 网络带宽瓶颈对并发的约束：若客户端出口带宽为 10Gbps（有效 1.25GB/s），且平均对象大小为 128KB，则单请求带宽占用 = 128KB / 0.0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N131, N132, N133

## Claim

网络带宽瓶颈对并发的约束：若客户端出口带宽为 10Gbps（有效 1.25GB/s），且平均对象大小为 128KB，则单请求带宽占用 = 128KB / 0.055s ≈ 2.3MB/s；1,000 并发所需带宽 = 1000 × 2.3MB/s = 2.3GB/s，超过 1.25GB/s 出口带宽，实际并发受限为 1.25GB/s / 2.3MB/s ≈ 543 个

## Corrected Claim

网络带宽瓶颈对并发的约束：若客户端出口带宽为 10Gbps（有效 1.25GB/s），且平均对象大小为 128KB，则单请求带宽占用 = 128KB / 0.055s ≈ 2.3MB/s；1,000 并发所需带宽 = 1000 × 2.3MB/s = 2.3GB/s，超过 1.25GB/s 出口带宽，实际并发受限为 1.25GB/s / 2.3MB/s ≈ 543 个

## Evidence

先验知识/题面给定，逻辑校验通过：10Gbps=1.25GB/s，128KB/0.055s≈2.3MB/s，1.25GB/s/2.3MB/s≈543，计算无误

## Search Query

S3 concurrent requests bandwidth limit 10Gbps
