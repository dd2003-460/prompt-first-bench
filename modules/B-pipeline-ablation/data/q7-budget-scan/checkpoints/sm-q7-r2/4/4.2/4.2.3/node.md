# N58: S3恢复吞吐15TB/h的瓶颈分解：S3 GET请求限流默认1500TPS/前缀，假设对象大小1MB，1500TPS×1MB=1.5GB/s=5.4TB/h；若

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

S3恢复吞吐15TB/h的瓶颈分解：S3 GET请求限流默认1500TPS/前缀，假设对象大小1MB，1500TPS×1MB=1.5GB/s=5.4TB/h；若使用S3 Batch API或提升限流配额至10000TPS，吞吐≈10GB/s=36TB/h；实际恢复吞吐受网络带宽（10GbE=4.5TB/h/节点）和S3限流双重约束，3节点集群≈13.5TB/h（网络瓶颈），15TB/h为乐观估计（假设限流配额已提升）

## Corrected Claim

S3恢复吞吐15TB/h的瓶颈分解：S3 GET请求限流默认1500TPS/前缀，假设对象大小1MB，1500TPS×1MB=1.5GB/s=5.4TB/h；若使用S3 Batch API或提升限流配额至10000TPS，吞吐≈10GB/s=36TB/h；实际恢复吞吐受网络带宽（10GbE=4.5TB/h/节点）和S3限流双重约束，3节点集群≈13.5TB/h（网络瓶颈），15TB/h为乐观估计（假设限流配额已提升）

## Evidence

先验知识/题面给定，逻辑校验通过：数学换算（1500TPS*1MB=1.5GB/s≈5.4TB/h, 10000TPS*1MB=10GB/s≈36TB/h, 10GbE≈1.25GB/s≈4.5TB/h）均准确；瓶颈分析逻辑自洽（取网络与限流的最小值或假设限流提升后的网络瓶颈），符合S3性能模型常识。
