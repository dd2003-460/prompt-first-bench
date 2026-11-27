# N99: PCIe 5.0 vs NVLink 900 GB/s 的通信延迟比值：在相同数据量下，PCIe 5.0 (64 GB/s) 的延迟是 NVLink (900 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

PCIe 5.0 vs NVLink 900 GB/s 的通信延迟比值：在相同数据量下，PCIe 5.0 (64 GB/s) 的延迟是 NVLink (900 GB/s) 的 14.06 倍 (900/64)；若NVLink下通信占比<1% (即<0.1ms/step)，则PCIe 5.0下通信占比约为 14% (1% * 14.06)，这将显著改变TP=2在PCIe平台上的可行性结论，可能使其不再优于单卡大显存方案。

## Corrected Claim

PCIe 5.0 vs NVLink 900 GB/s 的通信延迟比值：在相同数据量下，PCIe 5.0 (64 GB/s) 的延迟是 NVLink (900 GB/s) 的 14.06 倍 (900/64)；若NVLink下通信占比<1% (即<0.1ms/step)，则PCIe 5.0下通信占比约为 14% (1% * 14.06)，这将显著改变TP=2在PCIe平台上的可行性结论，可能使其不再优于单卡大显存方案。

## Evidence

先验知识/题面给定，逻辑校验通过：900/64=14.0625，1%*14.06≈14.06%，数值计算与逻辑推导自洽。

## Search Query

PCIe 5.0 bandwidth vs NVLink 900GB/s latency ratio tensor parallelism
