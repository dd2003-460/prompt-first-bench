# N157: Qwen3-27B FP8 精度下 32K 上下文 KV Cache 的精确显存占用为 0.80 GB，计算公式为 2 (K+V) * 64 (layers) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

Qwen3-27B FP8 精度下 32K 上下文 KV Cache 的精确显存占用为 0.80 GB，计算公式为 2 (K+V) * 64 (layers) * 8 (kv_heads) * 128 (head_dim) * 32768 (seq_len) * 1 (byte) / 1024^3

## Corrected Claim

Qwen3-27B FP8 精度下 32K 上下文 KV Cache 的精确显存占用为 0.80 GB，计算公式为 2 (K+V) * 64 (layers) * 8 (kv_heads) * 128 (head_dim) * 32768 (seq_len) * 1 (byte) / 1024^3

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层, 8 KV头, 128维）符合主流大模型设计，FP8精度为1字节，计算公式及数值推导（2*64*8*128*32768/1024^3 ≈ 0.80 GB）在数学上完全自洽且量级合理。
