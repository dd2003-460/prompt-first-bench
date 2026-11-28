# N80: V100 内存带宽基准：单卡 V100-SXM2 的 HBM2 内存带宽为 900 GB/s，4 卡聚合带宽为 3600 GB/s，这是长上下文推理中 KV C

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

V100 内存带宽基准：单卡 V100-SXM2 的 HBM2 内存带宽为 900 GB/s，4 卡聚合带宽为 3600 GB/s，这是长上下文推理中 KV Cache 读取速度的硬上限。

## Corrected Claim

V100 内存带宽基准：单卡 V100-SXM2 的 HBM2 内存带宽为 900 GB/s，4 卡聚合带宽为 3600 GB/s，这是长上下文推理中 KV Cache 读取速度的硬上限。

## Evidence

父节点级核验未通过：不完备（父节点明确限定范围为“单卡”和“4卡聚合”的HBM2内存带宽（本地显存访问），旨在说明KV Cache读取的硬上限。然而，唯一的子节点讨论的是“NVLink互联带宽”及TP=4下的通信瓶颈，这属于GPU间数据传输（Inter-GPU Communication）范畴，而非本地内存带宽（Local Memory Bandwidth）。子节点偏离了父节点的核心主题（本地内存带宽 vs 互联带宽），未能覆盖父节点关于“HBM2具体规格验证”或“KV Cache如何受限于此带宽”的关键方面，反而引入了一个虽然相关但属于不同维度的概念（通信延迟vs内存带宽）。因此，从严格分解角度看，子节点未正确支撑或细化父节点的特定论点，导致完备性缺失。）

## Search Query

Tesla V100 SXM2 HBM2 memory bandwidth specifications
