# N22: 生成阶段（Decode）的吞吐量瓶颈公式为 Throughput (tokens/s) ≈ Memory Bandwidth (GB/s) / Model Si

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

生成阶段（Decode）的吞吐量瓶颈公式为 Throughput (tokens/s) ≈ Memory Bandwidth (GB/s) / Model Size in Memory (GB)，该比值直接决定了在给定显存带宽硬件上的最大生成速度上限。

## Corrected Claim

生成阶段（Decode）的吞吐量瓶颈公式为 Throughput (tokens/s) ≈ Memory Bandwidth (GB/s) / Model Size in Memory (GB)，该比值直接决定了在给定显存带宽硬件上的最大生成速度上限。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别展示了消费级、数据中心和非典型统一内存三种不同硬件架构下的具体工作点，彼此之间硬件平台和配置互不重叠（正交）。它们共同覆盖了公式中‘带宽’和‘模型大小’在不同现实场景下的典型取值，从而完整阐释了父节点关于吞吐瓶颈的论点（完备）。虽然它们都是公式的具体实例，但代表了不同的硬件类别和性能权衡维度（如量化vs无损、显存容量vs带宽），并非简单的参数变量重复，而是具有代表性的案例对比，因此不构成冗余。）

## Search Query

LLM inference decode phase memory bandwidth bound formula tokens per second
