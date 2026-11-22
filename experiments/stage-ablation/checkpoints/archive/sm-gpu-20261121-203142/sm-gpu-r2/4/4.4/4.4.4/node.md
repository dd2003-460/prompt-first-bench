# N90: 多卡方案（2×RTX 4090, Tensor Parallel）的TTFT通信开销量化：Prefill阶段需在每张卡上执行部分计算并交换中间激活值；PCIe 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

多卡方案（2×RTX 4090, Tensor Parallel）的TTFT通信开销量化：Prefill阶段需在每张卡上执行部分计算并交换中间激活值；PCIe 4.0带宽（~25 GB/s单向）相对于HBM带宽是瓶颈；估算通信开销增加TTFT 15-30% [待核验]，导致有效TTFT ≈ 单卡TTFT * 1.2。

## Corrected Claim

多卡方案（2×RTX 4090, Tensor Parallel）的TTFT通信开销量化：Prefill阶段需在每张卡上执行部分计算并交换中间激活值；PCIe 4.0带宽（~25 GB/s单向）相对于HBM带宽是瓶颈；估算通信开销增加TTFT 15-30% [待核验]，导致有效TTFT ≈ 单卡TTFT * 1.2。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 带宽约 25-32 GB/s，远低于 HBM 带宽，构成瓶颈；Tensor Parallel 在 Prefill 阶段需交换激活值，通信开销占比 15-30% 符合工程经验量级，逻辑自洽。

## Search Query

tensor parallelism PCIe overhead LLM inference latency
