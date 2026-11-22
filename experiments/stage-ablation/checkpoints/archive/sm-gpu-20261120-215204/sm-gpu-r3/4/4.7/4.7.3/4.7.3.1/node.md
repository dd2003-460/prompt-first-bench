# N327: Qwen3-27B 在 Tensor Parallelism (TP=2) 下，每层 Attention QKV 投影和 Output 投影产生的 AllRed

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116

## Claim

Qwen3-27B 在 Tensor Parallelism (TP=2) 下，每层 Attention QKV 投影和 Output 投影产生的 AllReduce 同步数据量为 2 * BatchSize * SeqLen * HiddenDim * BytesPerParam，对于 BatchSize=1, SeqLen=32768, HiddenDim=4096, BF16 (2 bytes)，单层 Attention 同步量约为 536 MB (0.54 GB)。

## Corrected Claim

Qwen3-27B 在 Tensor Parallelism (TP=2) 下，每层 Attention QKV 投影和 Output 投影产生的 AllReduce 同步数据量为 2 * BatchSize * SeqLen * HiddenDim * BytesPerParam，对于 BatchSize=1, SeqLen=32768, HiddenDim=4096, BF16 (2 bytes)，单层 Attention 同步量约为 536 MB (0.54 GB)。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程为 2 (QKV+Out) * 1 (Batch) * 32768 (Seq) * 4096 (Hidden) * 2 (Bytes) = 536,870,912 Bytes ≈ 512 MiB ≈ 0.54 GB，数值量级与逻辑自洽。
