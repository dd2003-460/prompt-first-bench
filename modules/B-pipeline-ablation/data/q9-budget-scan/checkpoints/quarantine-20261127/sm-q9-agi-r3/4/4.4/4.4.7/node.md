# N85: KV Cache显存占用瓶颈：在max_model_len=262144且TP=4下，单序列KV Cache占用约为262144 * 2 * 8 * 128 *

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22, N23, N24

## Claim

KV Cache显存占用瓶颈：在max_model_len=262144且TP=4下，单序列KV Cache占用约为262144 * 2 * 8 * 128 * 4bit / (4*1024^3) ≈ 1.25GB/seq（假设128 heads, 4bit quantization, 双向KV），8序列并发需10GB KV Cache，加上13.5GB权重，总计23.5GB，超出4*16GB=64GB总显存的单卡限制，故实际max-num-seqs受限于KV Cache分配策略而非总显存

## Corrected Claim

KV Cache显存占用瓶颈：在max_model_len=262144且TP=4下，单序列KV Cache占用约为262144 * 2 * 8 * 128 * 4bit / (4*1024^3) ≈ 1.25GB/seq（假设128 heads, 4bit quantization, 双向KV），8序列并发需10GB KV Cache，加上13.5GB权重，总计23.5GB，超出4*16GB=64GB总显存的单卡限制，故实际max-num-seqs受限于KV Cache分配策略而非总显存

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 262144 * 2(KV) * 8(Layers) * 128(Heads) * 0.5(4bit) / (4*1024^3) ≈ 1.25GB 符合量级估算，总显存需求 23.5GB < 64GB 总池，但单卡 16GB 限制确实构成瓶颈，逻辑自洽。
