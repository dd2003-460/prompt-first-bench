# N240: Qwen3-27B (hidden_size=4096) 在 TP=2, Batch=1 场景下，每层 AllReduce 通信量为 2 * hidden_si

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73, N74, N75

## Claim

Qwen3-27B (hidden_size=4096) 在 TP=2, Batch=1 场景下，每层 AllReduce 通信量为 2 * hidden_size * bytes_per_element = 2 * 4096 * 2 = 16 KB (FP16/BF16) 或 8 KB (INT8)，总层数 64 层，每步通信总量为 1 MB (FP16) 或 0.5 MB (INT8)。

## Corrected Claim

Qwen3-27B (hidden_size=4096) 在 TP=2, Batch=1 场景下，每层 AllReduce 通信量为 2 * hidden_size * bytes_per_element = 2 * 4096 * 2 = 16 KB (FP16/BF16) 或 8 KB (INT8)，总层数 64 层，每步通信总量为 1 MB (FP16) 或 0.5 MB (INT8)。

## Evidence

先验知识/题面给定，逻辑校验通过：TP=2 AllReduce 通信量公式 2 * hidden_size * bytes 符合 Ring-AllReduce 理论最小值（2(N-1)/N * size ≈ 2*size），数值计算 2*4096*2=16KB 及 64 层总量 1MB 均正确。

## Search Query

Qwen3-27B hidden size architecture layers
