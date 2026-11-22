# N110: CPU Offload 策略下，RTX 4090 将部分权重/KV Cache 移至系统内存，受限于 PCIe 4.0 带宽 (32 GB/s 单向)，每生成一

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

CPU Offload 策略下，RTX 4090 将部分权重/KV Cache 移至系统内存，受限于 PCIe 4.0 带宽 (32 GB/s 单向)，每生成一个 Token 的额外延迟约为 (Offload Data Size / 32 GB/s)；若 Offload 10GB 数据，额外延迟约 312ms/Token，显著降低 TPS [待核验]

## Corrected Claim

CPU Offload 策略下，RTX 4090 将部分权重/KV Cache 移至系统内存，受限于 PCIe 4.0 带宽 (32 GB/s 单向)，每生成一个 Token 的额外延迟约为 (Offload Data Size / 32 GB/s)；若 Offload 10GB 数据，额外延迟约 312ms/Token，显著降低 TPS [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 单向带宽约 32 GB/s，10GB 数据传输耗时 10/32 ≈ 0.3125s (312ms)，计算逻辑自洽且符合硬件规格常识。

## Search Query

CPU offload PCIe bandwidth latency penalty tokens per second
