# N221: PCIe 5.0 下 TP=2 的 NCCL AllReduce 缓冲区大小：AllReduce 操作需暂存中间结果，缓冲区大小 ≈ 2 × Batch Siz

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

PCIe 5.0 下 TP=2 的 NCCL AllReduce 缓冲区大小：AllReduce 操作需暂存中间结果，缓冲区大小 ≈ 2 × Batch Size × Sequence Length × Hidden Dim × Bytes/Element。对于 Qwen3-27B (Hidden Dim=4096, BF16=2B)，Batch=1, Seq=32K 时，缓冲区 = 2 × 1 × 32768 × 4096 × 2 ≈ 512 MB。考虑 NCCL 内部碎片和协议开销，实际预留 1-2 GB/卡即可覆盖，3GB 预留过于保守。

## Corrected Claim

PCIe 5.0 下 TP=2 的 NCCL AllReduce 缓冲区大小：AllReduce 操作需暂存中间结果，缓冲区大小 ≈ 2 × Batch Size × Sequence Length × Hidden Dim × Bytes/Element。对于 Qwen3-27B (Hidden Dim=4096, BF16=2B)，Batch=1, Seq=32K 时，缓冲区 = 2 × 1 × 32768 × 4096 × 2 ≈ 512 MB。考虑 NCCL 内部碎片和协议开销，实际预留 1-2 GB/卡即可覆盖，3GB 预留过于保守。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 2*1*32768*4096*2 = 536,870,912 Bytes ≈ 512 MB 正确；NCCL AllReduce 在 TP=2 场景下主要涉及 Reduce-Scatter 和 All-Gather，中间缓冲区量级与计算结果一致，1-2GB 预留覆盖 512MB 数据及协议开销在工程上合理。
