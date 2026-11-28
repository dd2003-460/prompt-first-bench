# N143: V100-SXM2 的 L2 缓存容量为 6 MB，NVFP4 权重（27B 模型约 6.75 GB）无法驻留 L2，每次 Kernel 启动需从 HBM2 加

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

V100-SXM2 的 L2 缓存容量为 6 MB，NVFP4 权重（27B 模型约 6.75 GB）无法驻留 L2，每次 Kernel 启动需从 HBM2 加载，访存延迟约 400ns，导致 Dequantization 操作无法隐藏，成为主要瓶颈。

## Corrected Claim

V100-SXM2 的 L2 缓存容量为 6 MB，NVFP4 权重（27B 模型约 6.75 GB）无法驻留 L2，每次 Kernel 启动需从 HBM2 加载，访存延迟约 400ns，导致 Dequantization 操作无法隐藏，成为主要瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：V100-SXM2 L2缓存确为6MB，NVFP4 27B模型权重约6.75GB远超L2容量，HBM2访存延迟量级符合硬件特性，逻辑自洽。

## Search Query

V100 SXM2 L2 cache size HBM2 latency
