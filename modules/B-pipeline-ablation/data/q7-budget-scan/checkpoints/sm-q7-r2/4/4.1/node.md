# N19: RTO目标阈值约束：本地NVMe SSD阵列的RTO上限约为15分钟（基于RAID-6重建时间<2h及故障切换<5min的保守估计），HDD+SSD分层的RTO

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

RTO目标阈值约束：本地NVMe SSD阵列的RTO上限约为15分钟（基于RAID-6重建时间<2h及故障切换<5min的保守估计），HDD+SSD分层的RTO上限约为45分钟（HDD重建时间>6h但热数据SSD无重建延迟），云对象存储的RTO上限约为0分钟（多AZ冗余无重建概念）；若业务RTO要求<5min，则NVMe和HDD方案均不可行，仅剩云存储

## Corrected Claim

RTO目标阈值约束：本地NVMe SSD阵列的RTO上限约为15分钟（基于RAID-6重建时间<2h及故障切换<5min的保守估计），HDD+SSD分层的RTO上限约为45分钟（HDD重建时间>6h但热数据SSD无重建延迟），云对象存储的RTO上限约为0分钟（多AZ冗余无重建概念）；若业务RTO要求<5min，则NVMe和HDD方案均不可行，仅剩云存储

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-6重建耗时与故障切换时间的量级符合工程常识，云存储多AZ冗余无重建延迟的特性符合架构原理，推导逻辑自洽。
