# N512: RTX 5090 单卡运行 Qwen3-27B FP8 权重（27GB）+ 32K 上下文 FP8 KV Cache（6.29GB）的总显存占用为 33.29G

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N157

## Claim

RTX 5090 单卡运行 Qwen3-27B FP8 权重（27GB）+ 32K 上下文 FP8 KV Cache（6.29GB）的总显存占用为 33.29GB，超出 32GB 显存容量 1.29GB，导致 OOM 错误。

## Corrected Claim

RTX 5090 单卡运行 Qwen3-27B FP8 权重（27GB）+ 32K 上下文 FP8 KV Cache（6.29GB）的总显存占用为 33.29GB，超出 32GB 显存容量 1.29GB，导致 OOM 错误。

## Evidence

先验知识/题面给定，逻辑校验通过：27GB + 6.29GB = 33.29GB，33.29GB > 32GB，差值1.29GB，数值计算与逻辑推导完全自洽。
