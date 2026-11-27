# N546: Intel Arc A770 对 Qwen3-27B 不可行的根本原因是显存容量不足（16GB < 13.5GB 权重 + 2GB 开销 + 最小 KV Cac

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N189

## Claim

Intel Arc A770 对 Qwen3-27B 不可行的根本原因是显存容量不足（16GB < 13.5GB 权重 + 2GB 开销 + 最小 KV Cache），而非算力或带宽瓶颈，因此其 FP16/INT4 吞吐量数据对本题目标模型无直接参考意义

## Corrected Claim

Intel Arc A770 对 Qwen3-27B 不可行的根本原因是显存容量不足（16GB < 13.5GB 权重 + 2GB 开销 + 最小 KV Cache），而非算力或带宽瓶颈，因此其 FP16/INT4 吞吐量数据对本题目标模型无直接参考意义

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 在 FP16 下权重约 54GB，INT4 下约 13.5GB，加上 KV Cache 和运行时开销，16GB 显存确实无法容纳，故显存不足是根本瓶颈，算力/带宽非主要限制因素。
