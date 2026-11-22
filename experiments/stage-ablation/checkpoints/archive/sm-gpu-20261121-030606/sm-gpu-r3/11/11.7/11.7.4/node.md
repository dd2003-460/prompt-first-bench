# N409: 双 RTX 4090 在 INT8 精度下的理论吞吐量 51.4 tokens/s 未考虑 PCIe 5.0 互联带宽限制（~63 GB/s）导致的 AllRe

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N167

## Claim

双 RTX 4090 在 INT8 精度下的理论吞吐量 51.4 tokens/s 未考虑 PCIe 5.0 互联带宽限制（~63 GB/s）导致的 AllReduce 通信开销，需引入通信效率因子（通常 0.6-0.8）修正实际吞吐量。

## Corrected Claim

双 RTX 4090 在 INT8 精度下的理论吞吐量 51.4 tokens/s 未考虑 PCIe 5.0 互联带宽限制（~63 GB/s）导致的 AllReduce 通信开销，需引入通信效率因子（通常 0.6-0.8）修正实际吞吐量。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 5.0 x16 双向带宽约 63-64 GB/s，双卡 AllReduce 通信开销确实显著，引入 0.6-0.8 效率因子符合工程经验；51.4 tokens/s 作为理论上限未计通信开销在逻辑上自洽。
