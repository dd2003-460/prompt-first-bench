# N772: A100 80GB SXM 版本通过 NVLink 互联时的带宽为 600 GB/s/卡，在 TP=2 多卡部署中，All-Reduce 通信开销占比 = (通

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N275

## Claim

A100 80GB SXM 版本通过 NVLink 互联时的带宽为 600 GB/s/卡，在 TP=2 多卡部署中，All-Reduce 通信开销占比 = (通信时间 / 总推理时间)，需对比 PCIe 版（64 GB/s）与 SXM 版（600 GB/s）在 32K 上下文下的通信延迟差异，以判断互联方式对有效吞吐量的影响。

## Corrected Claim

A100 80GB SXM 版本通过 NVLink 互联时的带宽为 600 GB/s/卡，在 TP=2 多卡部署中，All-Reduce 通信开销占比 = (通信时间 / 总推理时间)，需对比 PCIe 版（64 GB/s）与 SXM 版（600 GB/s）在 32K 上下文下的通信延迟差异，以判断互联方式对有效吞吐量的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 SXM NVLink带宽600GB/s及PCIe带宽64GB/s符合硬件规格常识，通信开销占比定义逻辑自洽。

## Search Query

A100 NVLink bandwidth vs PCIe inference overhead
