# N209: 若采用'权重卸载 + 层间流水线'架构，GPU 仅保留当前计算层及少量 KV Cache，CPU 负责存储其余权重；此时 PCIe 传输的是权重块（而非激活值）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53, N54, N55

## Claim

若采用'权重卸载 + 层间流水线'架构，GPU 仅保留当前计算层及少量 KV Cache，CPU 负责存储其余权重；此时 PCIe 传输的是权重块（而非激活值），每层权重大小约为 (27B / 64 layers) * 2 bytes ≈ 0.84 GB (BF16)，传输 1 层权重耗时 ≈ 26 ms (32 GB/s)，若计算时间 > 26 ms 则可隐藏传输延迟，需验证 Qwen3-27B 单层计算时间是否足以覆盖 PCIe 传输开销。

## Corrected Claim

若采用'权重卸载 + 层间流水线'架构，GPU 仅保留当前计算层及少量 KV Cache，CPU 负责存储其余权重；此时 PCIe 传输的是权重块（而非激活值），每层权重大小约为 (27B / 64 layers) * 2 bytes ≈ 0.84 GB (BF16)，传输 1 层权重耗时 ≈ 26 ms (32 GB/s)，若计算时间 > 26 ms 则可隐藏传输延迟，需验证 Qwen3-27B 单层计算时间是否足以覆盖 PCIe 传输开销。

## Evidence

先验知识/题面给定，逻辑校验通过：27B/64层*2字节≈0.84GB，0.84GB/32GB/s≈26ms，计算与传输量级匹配，逻辑自洽。
