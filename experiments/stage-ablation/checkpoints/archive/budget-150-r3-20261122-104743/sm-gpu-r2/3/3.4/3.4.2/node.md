# N112: 2×RTX 4090 方案中，若采用 Pipeline Parallelism（按层切分），通信开销为每生成 1 token 传输一次 KV Cache（6.1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

2×RTX 4090 方案中，若采用 Pipeline Parallelism（按层切分），通信开销为每生成 1 token 传输一次 KV Cache（6.144 GB），单次通信延迟为 195 ms，计算过程为 6.144 GB / 31.5 GB/s

## Corrected Claim

2×RTX 4090 方案中，若采用 Pipeline Parallelism（按层切分），通信开销为每生成 1 token 传输一次 KV Cache（6.144 GB），单次通信延迟为 195 ms，计算过程为 6.144 GB / 31.5 GB/s

## Evidence

先验知识/题面给定，逻辑校验通过：6.144 GB / 31.5 GB/s ≈ 0.195 s = 195 ms，数值计算自洽，符合 PCIe 4.0 x16 双向带宽约 31.5 GB/s 的工程常识。
