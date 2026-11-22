# N60: 层切分策略对通信量的影响：若采用 Tensor Parallelism (TP)，每层需 All-Reduce，通信量为 2 × Hidden_Size × B

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

层切分策略对通信量的影响：若采用 Tensor Parallelism (TP)，每层需 All-Reduce，通信量为 2 × Hidden_Size × Batch_Size × Bytes_per_token；若采用 Pipeline Parallelism (PP)，仅层间传递激活值，通信量为 Hidden_Size × Batch_Size × Bytes_per_token；TP 通信量是 PP 的 2 倍，但 TP 延迟更低。

## Corrected Claim

层切分策略对通信量的影响：若采用 Tensor Parallelism (TP)，每层需 All-Reduce，通信量为 2 × Hidden_Size × Batch_Size × Bytes_per_token；若采用 Pipeline Parallelism (PP)，仅层间传递激活值，通信量为 Hidden_Size × Batch_Size × Bytes_per_token；TP 通信量是 PP 的 2 倍，但 TP 延迟更低。

## Evidence

先验知识/题面给定，逻辑校验通过
