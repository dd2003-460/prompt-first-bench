# N362: N130 2x4090 (W4) 实际吞吐量的带宽瓶颈验证：理论峰值 = 1008 GB/s / 13.5 GB = 74.6 Tokens/s；考虑 W4 量

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

N130 2x4090 (W4) 实际吞吐量的带宽瓶颈验证：理论峰值 = 1008 GB/s / 13.5 GB = 74.6 Tokens/s；考虑 W4 量化解码效率 (~50% 带宽利用率) 和 PCIe 同步开销，实际稳定吞吐 ~28-35 Tokens/s；需确认是否为单并发 (Batch=1) 场景。

## Corrected Claim

N130 2x4090 (W4) 实际吞吐量的带宽瓶颈验证：理论峰值 = 1008 GB/s / 13.5 GB = 74.6 Tokens/s；考虑 W4 量化解码效率 (~50% 带宽利用率) 和 PCIe 同步开销，实际稳定吞吐 ~28-35 Tokens/s；需确认是否为单并发 (Batch=1) 场景。

## Evidence

先验知识/题面给定，逻辑校验通过：理论峰值计算正确（1008/13.5≈74.6），W4量化下50%带宽利用率及PCIe开销导致的实际吞吐（28-35 Tokens/s）符合工程经验量级，逻辑自洽。
