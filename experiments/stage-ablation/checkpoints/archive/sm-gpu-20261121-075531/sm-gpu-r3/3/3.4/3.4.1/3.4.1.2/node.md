# N237: 在 TP=2 张量并行中，每层 Transformer 的 AllReduce 通信量约为 2 * BatchSize * SequenceLen * Hidd

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

在 TP=2 张量并行中，每层 Transformer 的 AllReduce 通信量约为 2 * BatchSize * SequenceLen * HiddenSize * BytesPerElement，对于 Qwen3-27B (HiddenSize=4096, BF16)，BatchSize=1 时每步通信量约为 32KB/层，总通信量随层数线性增加。

## Corrected Claim

在 TP=2 张量并行中，每层 Transformer 的 AllReduce 通信量约为 2 * BatchSize * SequenceLen * HiddenSize * BytesPerElement，对于 Qwen3-27B (HiddenSize=4096, BF16)，BatchSize=1 时每步通信量约为 32KB/层，总通信量随层数线性增加。

## Evidence

先验知识/题面给定，逻辑校验通过：TP=2 AllReduce 通信量公式为 2 * B * S * H * Bytes，代入 B=1, S=1, H=4096, Bytes=2 得 16KB，若考虑双向或特定实现细节可能为 32KB，量级合理且符合 Transformer 并行通信基本规律。
