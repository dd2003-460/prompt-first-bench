# N244: PCIe Gen4 x16 通信瓶颈量化验证：Qwen3-27B TP=2 每 token 通信量约 1.34 MB (N139)，在 32 GB/s 有效带宽

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N86

## Claim

PCIe Gen4 x16 通信瓶颈量化验证：Qwen3-27B TP=2 每 token 通信量约 1.34 MB (N139)，在 32 GB/s 有效带宽下通信耗时约 42 µs/token，若计算耗时低于此值，则系统进入通信受限状态，吞吐量上限被锁死在 ~24 tokens/s (1/42µs)。

## Corrected Claim

PCIe Gen4 x16 通信瓶颈量化验证：Qwen3-27B TP=2 每 token 通信量约 1.34 MB (N139)，在 32 GB/s 有效带宽下通信耗时约 42 µs/token，若计算耗时低于此值，则系统进入通信受限状态，吞吐量上限被锁死在 ~24 tokens/s (1/42µs)。

## Evidence

先验知识/题面给定，逻辑校验通过：1.34 MB / 32 GB/s ≈ 41.875 µs，取整为 42 µs；1 / 42 µs ≈ 23.8 tokens/s，取整为 ~24 tokens/s。数值量级与计算逻辑自洽。

## Search Query

PCIe Gen4 bandwidth tensor parallelism communication overhead latency
