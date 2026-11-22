# N395: MI300X 单卡 192GB 显存支持 32K 上下文的 KV Cache 容量验证：Qwen3-27B 64 层，GQA 8 KV heads，Head D

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N148

## Claim

MI300X 单卡 192GB 显存支持 32K 上下文的 KV Cache 容量验证：Qwen3-27B 64 层，GQA 8 KV heads，Head Dim 128，BF16 KV Cache 每 token 占用 = 2 * 64 * 8 * 128 * 2 bytes = 256 KB/token；32K tokens 总 KV Cache = 32768 * 256 KB = 8 GB；加上 54 GB 权重，总占用 62 GB < 192 GB，余量 130 GB 可支持并发 Batch Size 或更长上下文

## Corrected Claim

MI300X 单卡 192GB 显存支持 32K 上下文的 KV Cache 容量验证：Qwen3-27B 64 层，GQA 8 KV heads，Head Dim 128，BF16 KV Cache 每 token 占用 = 2 * 64 * 8 * 128 * 2 bytes = 256 KB/token；32K tokens 总 KV Cache = 32768 * 256 KB = 8 GB；加上 54 GB 权重，总占用 62 GB < 192 GB，余量 130 GB 可支持并发 Batch Size 或更长上下文

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算公式正确（2*64*8*128*2=256KB），总量估算合理（8GB+54GB<192GB）

## Search Query

Qwen3-27B KV cache size calculation 32k context GQA 8 heads
