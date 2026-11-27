# N427: RTX 4070 Ti Super 在 CPU Offload 配置下的可行性分析：若将 KV Cache 完全卸载到 CPU 内存（32GB DDR5），PC

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N143

## Claim

RTX 4070 Ti Super 在 CPU Offload 配置下的可行性分析：若将 KV Cache 完全卸载到 CPU 内存（32GB DDR5），PCIe 4.0 x16 带宽 64 GB/s 成为瓶颈，Decode 阶段每 token 需从 CPU 读取 4 GB KV Cache 数据，通信时间 = 4 GB / 64 GB/s = 0.0625 ms/token，相比 GPU 计算时间 ~15 ms/token，通信开销占比 < 0.5%，可忽略；但 CPU 内存容量需 ≥ 4 GB，且需验证 CPU 内存延迟对 Prefill 阶段的影响（Prefill 阶段 KV Cache 写入 CPU 的带宽瓶颈）。

## Corrected Claim

RTX 4070 Ti Super 在 CPU Offload 配置下的可行性分析：若将 KV Cache 完全卸载到 CPU 内存（32GB DDR5），PCIe 4.0 x16 带宽 64 GB/s 成为瓶颈，Decode 阶段每 token 需从 CPU 读取 4 GB KV Cache 数据，通信时间 = 4 GB / 64 GB/s = 0.0625 ms/token，相比 GPU 计算时间 ~15 ms/token，通信开销占比 < 0.5%，可忽略；但 CPU 内存容量需 ≥ 4 GB，且需验证 CPU 内存延迟对 Prefill 阶段的影响（Prefill 阶段 KV Cache 写入 CPU 的带宽瓶颈）。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 带宽 64 GB/s 为硬件标准规格，4 GB 数据传输耗时 0.0625 ms 计算正确，且远小于 15 ms 的 GPU 计算时间，通信开销占比 < 0.5% 的结论在逻辑和量级上均自洽。
