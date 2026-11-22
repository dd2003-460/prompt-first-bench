# N425: RTX 3090 Ti 在 CPU Offload 配置下的可行性分析：若将部分 KV Cache 卸载到 CPU 内存（如 32GB DDR5），PCIe 4

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N142

## Claim

RTX 3090 Ti 在 CPU Offload 配置下的可行性分析：若将部分 KV Cache 卸载到 CPU 内存（如 32GB DDR5），PCIe 4.0 x16 带宽 64 GB/s 成为瓶颈，Decode 阶段每 token 需从 CPU 读取 KV Cache 数据，假设 50% KV Cache 在 CPU，则额外通信时间 = (4 GB / 2) / 64 GB/s = 0.03125 ms/token，相比 GPU 计算时间 ~20 ms/token，通信开销占比 < 0.2%，可忽略；但 CPU 内存容量需 ≥ 4 GB，且需验证 CPU 内存延迟对 Prefill 阶段的影响。

## Corrected Claim

RTX 3090 Ti 在 CPU Offload 配置下的可行性分析：若将部分 KV Cache 卸载到 CPU 内存（如 32GB DDR5），PCIe 4.0 x16 带宽 64 GB/s 成为瓶颈，Decode 阶段每 token 需从 CPU 读取 KV Cache 数据，假设 50% KV Cache 在 CPU，则额外通信时间 = (4 GB / 2) / 64 GB/s = 0.03125 ms/token，相比 GPU 计算时间 ~20 ms/token，通信开销占比 < 0.2%，可忽略；但 CPU 内存容量需 ≥ 4 GB，且需验证 CPU 内存延迟对 Prefill 阶段的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 带宽 64 GB/s 符合标准规格；计算 (4GB/2)/64GB/s = 0.03125ms 数学正确；0.03125ms 远小于 20ms，占比 <0.2% 结论合理；CPU 内存容量需求与延迟影响分析符合系统架构常识。
