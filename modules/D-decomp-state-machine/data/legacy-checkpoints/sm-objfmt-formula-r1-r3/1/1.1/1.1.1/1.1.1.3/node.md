# N126: 2x RTX 4090 方案的性能折损系数：由于 PCIe 4.0 x8 带宽（~64 GB/s）远低于显存带宽，在多卡并行推理（如 Tensor Parall

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

2x RTX 4090 方案的性能折损系数：由于 PCIe 4.0 x8 带宽（~64 GB/s）远低于显存带宽，在多卡并行推理（如 Tensor Parallelism）中，All-Reduce 通信开销会导致有效吞吐量降至单卡理论值的 60%-75%（取决于 Batch Size 和序列长度），这意味着尽管总显存翻倍，其每 token 延迟改善并非线性，而是受限于互联瓶颈，这是其相对于单卡大显存方案（如 5090）的主要劣势。

## Corrected Claim

2x RTX 4090 方案的性能折损系数：由于 PCIe 4.0 x8 带宽（~64 GB/s）远低于显存带宽，在多卡并行推理（如 Tensor Parallelism）中，All-Reduce 通信开销会导致有效吞吐量降至单卡理论值的 60%-75%（取决于 Batch Size 和序列长度），这意味着尽管总显存翻倍，其每 token 延迟改善并非线性，而是受限于互联瓶颈，这是其相对于单卡大显存方案（如 5090）的主要劣势。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x8 带宽（~64 GB/s）确实远低于 HBM 显存带宽（~1 TB/s），在 Tensor Parallelism 中 All-Reduce 通信开销显著，导致多卡效率低于线性扩展，60%-75% 的效率区间符合工程经验与物理限制。
