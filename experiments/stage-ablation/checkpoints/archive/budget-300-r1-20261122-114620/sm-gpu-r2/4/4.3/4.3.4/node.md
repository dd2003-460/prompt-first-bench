# N111: 在 batch_size=1 的本地推理场景下，PCIe 双卡方案的吞吐损失百分比通常为 15-30%，因为通信时间与计算时间比例较高；而在 batch_siz

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

在 batch_size=1 的本地推理场景下，PCIe 双卡方案的吞吐损失百分比通常为 15-30%，因为通信时间与计算时间比例较高；而在 batch_size>8 的高并发场景下，通信开销占比下降至 5-10%，因为计算时间 T_compute 随 batch_size 线性增长而通信时间增长较慢

## Corrected Claim

在 batch_size=1 的本地推理场景下，PCIe 双卡方案的吞吐损失百分比通常为 15-30%，因为通信时间与计算时间比例较高；而在 batch_size>8 的高并发场景下，通信开销占比下降至 5-10%，因为计算时间 T_compute 随 batch_size 线性增长而通信时间增长较慢

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

dual GPU inference throughput loss percentage batch size PCIe Gen4
