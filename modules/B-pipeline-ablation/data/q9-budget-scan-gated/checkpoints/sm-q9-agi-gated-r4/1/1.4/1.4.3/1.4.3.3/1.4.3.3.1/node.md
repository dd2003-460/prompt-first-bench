# N118: V100-SXM2-16GB 服务器若配备 NVSwitch，4 卡间通信走 NVLink3（带宽 300 GB/s，延迟 ~2 μs）；若无 NVSwitch

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

V100-SXM2-16GB 服务器若配备 NVSwitch，4 卡间通信走 NVLink3（带宽 300 GB/s，延迟 ~2 μs）；若无 NVSwitch 而经 PCIe 3.0 x16 互联，有效带宽降为 16 GB/s，延迟增加至 ~10 μs，需通过 nvidia-smi topo -m 命令确认实际拓扑，再决定 B_eff 取值。

## Corrected Claim

V100-SXM2-16GB 服务器若配备 NVSwitch，4 卡间通信走 NVLink3（带宽 300 GB/s，延迟 ~2 μs）；若无 NVSwitch 而经 PCIe 3.0 x16 互联，有效带宽降为 16 GB/s，延迟增加至 ~10 μs，需通过 nvidia-smi topo -m 命令确认实际拓扑，再决定 B_eff 取值。

## Evidence

[质询]NVLink 3.0 的单向带宽通常为 25 GB/s，双向为 50 GB/s，单卡总带宽 300 GB/s 是合理的（6条链路*50GB/s），但‘4卡间通信走NVLink3’的表述略显模糊，因为NVSwitch提供的是全互联，任意两卡间带宽受限于单卡端口聚合带宽，而非简单的‘4卡间’总和。不过，300 GB/s 通常指单卡对外总带宽，符合 V100 SXM2 规格。 | 先验知识/题面给定，逻辑校验通过。V100 SXM2 配备 NVSwitch 时，每卡拥有 6 个 NVLink 3.0 连接，每个连接双向带宽 50 GB/s，总带宽 300 GB/s，符合 NVIDIA 官方规格。PCIe 3.0 x16 理论带宽 16 GB/s，实际有效带宽略低，延迟显著高于 NVLink，符合硬件常识。nvidia-smi topo -m 是标准拓扑查询命令。

## Search Query

nvidia-smi topo -m V100 SXM2 NVSwitch PCIe topology
