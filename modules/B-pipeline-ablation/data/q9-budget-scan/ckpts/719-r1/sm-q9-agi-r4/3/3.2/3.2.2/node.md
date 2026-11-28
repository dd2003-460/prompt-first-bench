# N53: 单张 V100-16GB 可用显存扣除模型权重（NVFP4 ~3.4GB/卡）和激活值/临时缓冲区（~2-4GB）后，剩余约 8-10GB 用于 KV Cach

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

单张 V100-16GB 可用显存扣除模型权重（NVFP4 ~3.4GB/卡）和激活值/临时缓冲区（~2-4GB）后，剩余约 8-10GB 用于 KV Cache，FP8 下每 Token 每层 KV 占用若为 32KB，则单卡可容纳约 256K-512K Tokens 的 KV Cache（理论上限，实际受 PagedAttention 块大小限制）。

## Corrected Claim

单张 V100-16GB 可用显存扣除模型权重（NVFP4 ~3.4GB/卡）和激活值/临时缓冲区（~2-4GB）后，剩余约 8-10GB 用于 KV Cache，FP8 下每 Token 每层 KV 占用若为 32KB，则单卡可容纳约 256K-512K Tokens 的 KV Cache（理论上限，实际受 PagedAttention 块大小限制）。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 10 column 5 (char 848)
