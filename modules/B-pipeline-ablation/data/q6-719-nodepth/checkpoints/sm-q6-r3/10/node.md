# N140: 读写比例 (Read/Write Ratio) 对存储IOPS压力的影响：日均下载2TB (Read) vs 上传200GB (Write)，Read:Writ

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

读写比例 (Read/Write Ratio) 对存储IOPS压力的影响：日均下载2TB (Read) vs 上传200GB (Write)，Read:Write = 10:1。由于CDN主要承担读请求，写请求通常直连源站或对象存储，因此CDN节点的存储压力主要体现为读IOPS和带宽，而非写放大。若采用全闪存节点，读IOPS需求约为 (2TB / 3600s / 4h_peak) / 4KB ≈ 350k IOPS (峰值)，需确认硬件是否支持。

## Corrected Claim

读写比例 (Read/Write Ratio) 对存储IOPS压力的影响：日均下载2TB (Read) vs 上传200GB (Write)，Read:Write = 10:1。由于CDN主要承担读请求，写请求通常直连源站或对象存储，因此CDN节点的存储压力主要体现为读IOPS和带宽，而非写放大。若采用全闪存节点，假设峰值4小时承载日均流量，读IOPS需求约为 (2TB / 4h) / 4KB ≈ 35k IOPS (峰值)，需确认硬件是否支持。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别覆盖了计算修正（读）、写/缓存开销（写/逻辑层）和硬件对比（物理层），维度清晰且无重叠。虽然子节点1修正了父节点中的计算错误，但这属于必要的细节展开而非冗余，且最终结论在子节点3中统一汇总，逻辑闭环完整。）

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/668976764&rut=fd18abe381bd92255252092a26937446128ceb2a4937ec6ea80234712eba7c0f', 'type': 'ddg', 'title': '一文读懂：Iops、延迟和吞吐量等存储性能指标 - 知乎'}
