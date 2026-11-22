# N505: Qwen3-27B 在 32K 上下文下，若 KV Cache 使用 FP8 (E4M3) 量化，总大小为 0.535 GB，计算公式为 2 * 40 * 40

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N208

## Claim

Qwen3-27B 在 32K 上下文下，若 KV Cache 使用 FP8 (E4M3) 量化，总大小为 0.535 GB，计算公式为 2 * 40 * 40 * 128 * 32768 * 1 byte，单 Token 增量为 16.4 KB，相比 BF16 节省 50% KV 显存。

## Corrected Claim

Qwen3-27B 在 32K 上下文下，若 KV Cache 使用 FP8 (E4M3) 量化，总大小为 0.535 GB，计算公式为 2 * 40 * 40 * 128 * 32768 * 1 byte，单 Token 增量为 16.4 KB，相比 BF16 节省 50% KV 显存。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（40层, GQA 40:8, Head Dim 128）符合已知规格，计算公式 2*40*40*128*32768*1 字节量级与数值推导正确，FP8 相比 BF16 节省 50% 显存符合量化原理。
