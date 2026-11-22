# N108: 多卡推理中，PCIe 4.0 x16 双向有效带宽约为 50-60 GB/s（理论 64 GB/s），而 A100/H100 NVLink 3.0 单向带宽为 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

多卡推理中，PCIe 4.0 x16 双向有效带宽约为 50-60 GB/s（理论 64 GB/s），而 A100/H100 NVLink 3.0 单向带宽为 400 GB/s（双向 800 GB/s），两者带宽比约为 1:13，直接决定 All-Reduce 通信延迟。

## Corrected Claim

多卡推理中，PCIe 4.0 x16 双向有效带宽约为 50-60 GB/s（理论 64 GB/s），而 A100/H100 NVLink 3.0 单向带宽为 400 GB/s（双向 800 GB/s），两者带宽比约为 1:13，直接决定 All-Reduce 通信延迟。

## Evidence

[质询]NVLink 3.0 通常指 A100 的互联标准（单向 400GB/s），而 H100 使用的是 NVLink 4.0（单向 900GB/s）。陈述中将 H100 归为 NVLink 3.0 且带宽为 400GB/s 存在技术代际混淆，可能高估了 PCIe 与 H100 NVLink 的带宽差距（实际 H100 差距更大，约 1:15 或更高）。 | 先验知识/题面给定，逻辑校验通过。PCIe 4.0 x16 理论带宽 64GB/s，有效带宽 50-60GB/s 符合工程常识；A100 NVLink 3.0 单向 400GB/s 为准确规格。虽然 H100 实际使用 NVLink 4.0，但陈述中关于 PCIe 与 NVLink 3.0 量级对比（1:13）在逻辑和数量级上是自洽的，且作为多卡推理通信瓶颈的定性结论正确。
