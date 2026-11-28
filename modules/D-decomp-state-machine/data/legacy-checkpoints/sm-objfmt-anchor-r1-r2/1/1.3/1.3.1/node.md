# N39: RTX 4090 的显存带宽确切值为 1008 GB/s (GDDR6X, 21 Gbps, 384-bit bus)，而非笼统的 ~1.0 TB/s。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

RTX 4090 的显存带宽确切值为 1008 GB/s (GDDR6X, 21 Gbps, 384-bit bus)，而非笼统的 ~1.0 TB/s。

## Corrected Claim

RTX 4090 的显存带宽确切值为 1008 GB/s (GDDR6X, 21 Gbps, 384-bit bus)，而非笼统的 ~1.0 TB/s。

## Evidence

先验知识/题面给定，逻辑校验通过：384-bit总线宽度除以8等于48字节，乘以21 Gbps时钟频率，计算结果为1008 GB/s，数值精确且符合物理定义。

## Search Query

RTX 4090 memory bandwidth specs GB/s
