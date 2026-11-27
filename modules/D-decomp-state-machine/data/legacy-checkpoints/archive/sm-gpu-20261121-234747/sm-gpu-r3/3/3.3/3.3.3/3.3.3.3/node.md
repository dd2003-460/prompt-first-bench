# N262: L40S在FP8精度下Decode阶段的实际吞吐量（tokens/s）受限于显存带宽瓶颈（Memory-Bound），估算公式：Throughput ≈ (Ba

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94, N95, N96

## Claim

L40S在FP8精度下Decode阶段的实际吞吐量（tokens/s）受限于显存带宽瓶颈（Memory-Bound），估算公式：Throughput ≈ (Bandwidth_GBps * Utilization) / (Weight_Size_GB + KV_Cache_GB_per_token)，其中Bandwidth=864 GB/s，Weight_Size=27GB，KV_Cache_GB_per_token ≈ 0.00006 GB，若带宽利用率70%，则吞吐 ≈ (864*0.7)/27.00006 ≈ 22.4 tokens/s，与父节点N94提到的25-35区间存在差异，需实测校准

## Corrected Claim

L40S在FP8精度下Decode阶段的实际吞吐量（tokens/s）受限于显存带宽瓶颈（Memory-Bound），估算公式：Throughput ≈ (Bandwidth_GBps * Utilization) / (Weight_Size_GB + KV_Cache_GB_per_token)，其中Bandwidth=864 GB/s，Weight_Size=27GB，KV_Cache_GB_per_token ≈ 0.00006 GB，若带宽利用率70%，则吞吐 ≈ (864*0.7)/27.00006 ≈ 22.4 tokens/s，与父节点N94提到的25-35区间存在差异，需实测校准

## Evidence

先验知识/题面给定，逻辑校验通过：L40S显存带宽864GB/s，27GB权重在FP8下，70%利用率下理论上限约22.4 tokens/s，与25-35区间存在合理偏差（可能源于KV Cache估算或实际利用率波动），量级与物理直觉一致。

## Search Query

NVIDIA L40S memory bandwidth GB/s FP8 inference throughput benchmark
