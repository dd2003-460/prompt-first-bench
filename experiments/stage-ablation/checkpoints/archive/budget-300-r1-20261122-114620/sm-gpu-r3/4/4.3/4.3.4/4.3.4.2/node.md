# N344: 在 batch_size=1 时，若采用 KV Cache 按批次分片 (Batch Parallelism)，则无额外 KV 通信，仅权重和激活值通信，T_c

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N111

## Claim

在 batch_size=1 时，若采用 KV Cache 按批次分片 (Batch Parallelism)，则无额外 KV 通信，仅权重和激活值通信，T_comm 降低 50%，η_comm 相应降低，实际吞吐损失约为 25-35%，需对比 Sequence Parallelism 和 Batch Parallelism 的通信开销差异

## Corrected Claim

在 batch_size=1 时，若采用 KV Cache 按批次分片 (Batch Parallelism)，通常无额外 KV 通信，仅权重和激活值通信，相比 Sequence Parallelism 通信开销显著降低（具体比例依架构而定），实际吞吐损失通常低于 Sequence Parallelism，需根据具体硬件和模型配置对比两者的通信开销差异。

## Evidence

[质询]具体数值（50%通信降低、25-35%吞吐损失）缺乏通用理论支撑，高度依赖具体模型架构、硬件拓扑及序列长度，属于经验性估算而非普适结论；且'KV Cache按批次分片'在batch_size=1时通常退化为单序列处理，'无额外KV通信'的前提需严格限定为无跨设备KV同步的场景，表述略显绝对。 | 先验知识/题面给定，逻辑校验通过：Batch Parallelism在batch_size=1时确实主要涉及权重和激活值通信，相比Sequence Parallelism（需切分序列并通信KV/激活）通信量通常更低，但具体百分比为经验估算，缺乏来源直接支持，故降级。
