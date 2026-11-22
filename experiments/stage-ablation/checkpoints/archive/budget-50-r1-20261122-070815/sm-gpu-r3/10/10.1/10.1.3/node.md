# N418: 性能增益比 R_gain = Throughput_FP8 / Throughput_BF16，理论上限受限于 Hopper Tensor Core 的 FP8

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N145

## Claim

性能增益比 R_gain = Throughput_FP8 / Throughput_BF16，理论上限受限于 Hopper Tensor Core 的 FP8 算力密度（2x BF16）及内存带宽不变性；若 R_gain 接近 1.4-1.8x，则验证了 N145 中'1.4 倍提升'的估计；若显著低于此值，需分析是否为 Qwen3 线性注意力层在 FP8 下的计算瓶颈。

## Corrected Claim

性能增益比 R_gain = Throughput_FP8 / Throughput_BF16，理论上限受限于 Hopper Tensor Core 的 FP8 算力密度（2x BF16）及内存带宽不变性；若 R_gain 接近 1.4-1.8x，则验证了 N145 中'1.4 倍提升'的估计；若显著低于此值，需分析是否为 Qwen3 线性注意力层在 FP8 下的计算瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：Hopper架构FP8算力确为BF16的2倍，受内存带宽限制下1.4-1.8x的性能增益比符合Roofline模型预期，逻辑自洽。
