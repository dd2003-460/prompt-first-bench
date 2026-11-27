# N63: 在 2×RTX 4090 (PCIe 4.0) 方案中，张量并行每层通信量 8KB (BF16)，总通信量 384KB/step，PCIe 4.0 带宽 32G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

在 2×RTX 4090 (PCIe 4.0) 方案中，张量并行每层通信量 8KB (BF16)，总通信量 384KB/step，PCIe 4.0 带宽 32GB/s 下通信延迟为 384e3 / 32e9 ≈ 12μs/step，占总 TPOT (33-50ms) 的比例 <0.1%，可忽略不计

## Corrected Claim

在 2×RTX 4090 (PCIe 4.0) 方案中，张量并行每层通信量 8KB (BF16)，总通信量 384KB/step，PCIe 4.0 带宽 32GB/s 下通信延迟为 384e3 / 32e9 ≈ 12μs/step，占总 TPOT (33-50ms) 的比例 <0.1%，可忽略不计

## Evidence

先验知识/题面给定，逻辑校验通过：2×GPU张量并行每层通信量8KB（BF16）符合典型Transformer层间激活/梯度同步量级；总通信量384KB/step（假设48层或等效聚合）与单步延迟12μs（384KB/32GB/s）计算一致；12μs相对于33-50ms的TPOT占比确实<0.1%，结论合理。
