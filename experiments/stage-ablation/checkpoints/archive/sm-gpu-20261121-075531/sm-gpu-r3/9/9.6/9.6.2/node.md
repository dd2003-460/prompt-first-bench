# N363: 在 TP=2 模式下，每步 (Step) 的总 AllReduce 通信量为 64 (层) * 8192 (Bytes/Step, FP16) = 524,28

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122

## Claim

在 TP=2 模式下，每步 (Step) 的总 AllReduce 通信量为 64 (层) * 8192 (Bytes/Step, FP16) = 524,288 Bytes/Step ≈ 0.5 MB/Step；若使用 FP8，则为 64 * 4096 = 262,144 Bytes/Step ≈ 0.25 MB/Step。

## Corrected Claim

在 TP=2 模式下，每步 (Step) 的总 AllReduce 通信量为 64 (层) * 8192 (Bytes/Step, FP16) = 524,288 Bytes/Step ≈ 0.5 MB/Step；若使用 FP8，则为 64 * 4096 = 262,144 Bytes/Step ≈ 0.25 MB/Step。

## Evidence

先验知识/题面给定，逻辑校验通过：64 * 8192 = 524,288 Bytes (0.5 MB) 且 64 * 4096 = 262,144 Bytes (0.25 MB)，计算无误，量级合理。
