# N304: Offload 策略对吞吐的影响：若采用 'Weight Streaming' (每层加载后卸载) vs 'Persistent Offload' (常驻内存)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N89

## Claim

Offload 策略对吞吐的影响：若采用 'Weight Streaming' (每层加载后卸载) vs 'Persistent Offload' (常驻内存)，前者增加 PCIe 传输开销 (32GB/s) 和 CPU 调度延迟，后者受限于内存容量；对于 3GB 小缺口，'Persistent Offload' 更优，但需确保 DDR 内存带宽 > 100 GB/s 才能维持 >30 tok/s 的可用交互速度

## Corrected Claim

Offload 策略对吞吐的影响：若采用 'Weight Streaming' (每层加载后卸载) vs 'Persistent Offload' (常驻内存)，前者增加 PCIe 传输开销 (32GB/s) 和 CPU 调度延迟，后者受限于内存容量；对于 3GB 小缺口，'Persistent Offload' 更优，但需确保 DDR 内存带宽 > 100 GB/s 才能维持 >30 tok/s 的可用交互速度

## Evidence

先验知识/题面给定，逻辑校验通过
