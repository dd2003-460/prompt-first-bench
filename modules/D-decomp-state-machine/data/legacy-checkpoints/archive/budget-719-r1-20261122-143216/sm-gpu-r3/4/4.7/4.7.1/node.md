# N119: 单卡（如RTX 5090）在 Qwen3-27B 模型上的最大有效并发数（Max Batch Size）计算公式为：Batch_max = floor((VRA

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

单卡（如RTX 5090）在 Qwen3-27B 模型上的最大有效并发数（Max Batch Size）计算公式为：Batch_max = floor((VRAM_total - VRAM_weights - VRAM_overhead) / VRAM_per_request_32K)，其中 VRAM_per_request_32K 需结合 N31 确定的架构参数计算得出，该值即为单卡失效的并发阈值。

## Corrected Claim

单卡（如RTX 5090）在 Qwen3-27B 模型上的最大有效并发数（Max Batch Size）计算公式为：Batch_max = floor((VRAM_total - VRAM_weights - VRAM_overhead) / VRAM_per_request_32K)，其中 VRAM_per_request_32K 需结合 N31 确定的架构参数计算得出，该值即为单卡失效的并发阈值。

## Evidence

父节点级核验未通过：有冗余（子节点在逻辑上是正交的，分别定义了公式中的不同变量项（权重、开销、单请求显存），且涵盖了父节点公式所需的所有关键参数，因此是完备的。然而，子节点 1 和 2 存在明显的结构冗余，它们本质上是同一个变量 `VRAM_weights` 在不同精度下的取值，应合并为一个节点或作为该变量的参数列表，而不是拆分为两个独立的同级节点。同样，子节点 4 也包含了 FP8 和 BF16 两种情况，结构上与子节点 1/2 保持一致但略显松散，建议统一处理。）
