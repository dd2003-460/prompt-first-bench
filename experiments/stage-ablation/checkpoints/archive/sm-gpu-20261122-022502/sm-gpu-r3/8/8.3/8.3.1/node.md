# N265: 在 Memory-Bound 区域（大模型单 token 解码），吞吐量提升率 η_throughput 与权重位宽缩减比 R_bit 的关系为 η_throu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N88

## Claim

在 Memory-Bound 区域（大模型单 token 解码），吞吐量提升率 η_throughput 与权重位宽缩减比 R_bit 的关系为 η_throughput ≈ R_bit - 1（理想线性），其中 R_bit = Bits_BF16 / Bits_Quantized (如 16/8=2, 16/4=4)。

## Corrected Claim

在 Memory-Bound 区域（大模型单 token 解码），吞吐量提升率 η_throughput 与权重位宽缩减比 R_bit 的关系为 η_throughput ≈ R_bit - 1（理想线性），其中 R_bit = Bits_BF16 / Bits_Quantized (如 16/8=2, 16/4=4)。

## Evidence

先验知识/题面给定，逻辑校验通过
