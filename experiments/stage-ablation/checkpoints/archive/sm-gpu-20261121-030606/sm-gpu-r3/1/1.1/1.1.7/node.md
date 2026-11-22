# N86: RTX 4090 FP8 推理吞吐量估算：1008 GB/s / (27GB 权重 + 4.7GB KV) ≈ 32.4 tokens/s，基于带宽受限假设

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

RTX 4090 FP8 推理吞吐量估算：1008 GB/s / (27GB 权重 + 4.7GB KV) ≈ 32.4 tokens/s，基于带宽受限假设

## Corrected Claim

RTX 4090 FP8 推理吞吐量估算：1008 GB/s / (27GB 权重 + 4.7GB KV) ≈ 32.4 tokens/s，基于带宽受限假设

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1关注数据量（权重/KV大小）的精确性，子节点2关注计算模型（带宽 vs 算力/开销）的精确性，两者维度不同且互补，无重复或矛盾。覆盖了吞吐量估算中主要的数据侧和计算侧修正因素。）

## Search Query

RTX 4090 FP8 LLM inference throughput tokens per second
