# N401: 在 TP=2 场景下，2×RTX 5090 每 token 的通信量 Comm_Volume 固定为 2 × 64 layers × 4096 hidden_d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N142

## Claim

在 TP=2 场景下，2×RTX 5090 每 token 的通信量 Comm_Volume 固定为 2 × 64 layers × 4096 hidden_dim × 2 bytes (BF16) = 10.48 MB，由于通信量不变而带宽增加 3 倍，纯通信时间 Comm_Time 理论上降至 RTX 4090 方案的 1/3。

## Corrected Claim

在 TP=2 场景下，2×RTX 5090 每 token 的通信量 Comm_Volume 固定为 2 × 64 layers × 4096 hidden_dim × 2 bytes (BF16) = 10.48 MB，由于通信量不变而带宽增加 3 倍，纯通信时间 Comm_Time 理论上降至 RTX 4090 方案的 1/3。

## Evidence

先验知识/题面给定，逻辑校验通过：通信量计算 2*64*4096*2 = 10,485,760 bytes = 10.48 MB 正确；带宽增加3倍导致时间降至1/3符合物理直觉（Time = Volume / Bandwidth）。
