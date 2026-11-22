# N494: A100 SXM TP=2 全模型通信总量修正：基于修正后的每层 4 KB，64 层总通信量 = 64 * 4 KB = 256 KB（Batch=1）；若 B

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N167

## Claim

A100 SXM TP=2 全模型通信总量修正：基于修正后的每层 4 KB，64 层总通信量 = 64 * 4 KB = 256 KB（Batch=1）；若 Batch=32，总通信量 = 64 * 32 * 4 KB = 8 MB；N167 中 8.58 GB 的总量在 Batch=1 下高估了 32768 倍。

## Corrected Claim

A100 SXM TP=2 全模型通信总量修正：基于修正后的每层 4 KB，64 层总通信量 = 64 * 4 KB = 256 KB（Batch=1）；若 Batch=32，总通信量 = 64 * 32 * 4 KB = 8 MB；N167 中 8.58 GB 的总量在 Batch=1 下高估了 32768 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：64*4KB=256KB，64*32*4KB=8MB，8.58GB/256KB≈32768，数值计算与量级推导均自洽。
