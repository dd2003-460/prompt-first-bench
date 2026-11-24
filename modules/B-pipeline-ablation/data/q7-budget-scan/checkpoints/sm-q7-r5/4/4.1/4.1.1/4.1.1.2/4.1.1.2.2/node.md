# N443: RTO 期间最大并发业务请求上限 N_concurrent_max = (B_biz_avail / IOP_size) / (1/Target_IOPS_la

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N194

## Claim

RTO 期间最大并发业务请求上限 N_concurrent_max = (B_biz_avail / IOP_size) / (1/Target_IOPS_latency)，若 Target_IOPS_latency=10ms, IOP_size=4KB, B_biz_avail=8.7GB/s (HDD层)，则 N_concurrent_max ≈ 8.7e9/4096/100 ≈ 21,000 IOPS，远低于正常状态的 50,000+ IOPS

## Corrected Claim

RTO 期间最大并发业务请求上限 N_concurrent_max = (B_biz_avail / IOP_size) / (1/Target_IOPS_latency)，若 Target_IOPS_latency=10ms, IOP_size=4KB, B_biz_avail=8.7GB/s (HDD层)，则 N_concurrent_max ≈ 8.7e9/4096/100 ≈ 21,000 IOPS，远低于正常状态的 50,000+ IOPS
