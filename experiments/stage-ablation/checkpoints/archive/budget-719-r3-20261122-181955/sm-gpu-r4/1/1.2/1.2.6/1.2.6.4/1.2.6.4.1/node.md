# N498: Decode 阶段 TP=2 通信数据量精确计算：每层 All-Reduce 同步隐藏状态 (Hidden State)，数据量 = 2 (All-Reduce

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N170

## Claim

Decode 阶段 TP=2 通信数据量精确计算：每层 All-Reduce 同步隐藏状态 (Hidden State)，数据量 = 2 (All-Reduce 系数) × Batch(1) × Hidden_Dim(4096) × dtype_size(2 bytes) = 16 KB；64 层总通信量 = 64 × 16 KB = 1 MB (每 token)。

## Corrected Claim

Decode 阶段 TP=2 通信数据量精确计算：每层 All-Reduce 同步隐藏状态 (Hidden State)，数据量 = 2 (All-Reduce 系数) × Batch(1) × Hidden_Dim(4096) × dtype_size(2 bytes) = 16 KB；64 层总通信量 = 64 × 16 KB = 1 MB (每 token)。

## Evidence

先验知识/题面给定，逻辑校验通过：All-Reduce 通信量公式为 2 * N * D * S，代入 N=1, D=4096, S=2 得 16KB/层，64层共 1MB，计算无误。
