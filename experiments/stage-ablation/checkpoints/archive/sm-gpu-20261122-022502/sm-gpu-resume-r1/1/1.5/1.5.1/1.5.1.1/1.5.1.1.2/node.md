# N524: 在 Tensor Parallelism (TP=2) 下，每层通信量包括 Attention 输出 All-Reduce (268 MB) 和 MLP 中间层

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N161

## Claim

在 Tensor Parallelism (TP=2) 下，每层通信量包括 Attention 输出 All-Reduce (268 MB) 和 MLP 中间层 All-Reduce (268 MB)，单层总通信量约为 536 MB。

## Corrected Claim

在 Tensor Parallelism (TP=2) 下，每层通信量包括 Attention 输出 All-Reduce (268 MB) 和 MLP 中间层 All-Reduce (268 MB)，单层总通信量约为 536 MB。

## Evidence

先验知识/题面给定，逻辑校验通过
