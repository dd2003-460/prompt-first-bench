# N100: Decode 阶段的显存读取总量 R_decode = Weight_Size_bytes + KV_Cache_bytes_per_token * (seq_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

Decode 阶段的显存读取总量 R_decode = Weight_Size_bytes + KV_Cache_bytes_per_token * (seq_len - 1)。对于 Qwen3-27B BF16，Weight_Size ≈ 54GB，KV_Cache 每 token 增量 ≈ 32KB (基于 N20 数据)，32K 上下文下 KV_Cache 总量 ≈ 1GB，总读取量 ≈ 55GB。

## Corrected Claim

Decode 阶段的显存读取总量 R_decode = Weight_Size_bytes + KV_Cache_bytes_per_token * (seq_len - 1)。对于 Qwen3-27B BF16，Weight_Size ≈ 54GB，KV_Cache 每 token 增量 ≈ 32KB (基于 N20 数据)，32K 上下文下 KV_Cache 总量 ≈ 1GB，总读取量 ≈ 55GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB（27B*2bytes），KV Cache每token 32KB符合常见架构配置（如GQA），32K上下文下KV Cache约1GB，总读取量55GB量级合理且计算自洽。

## Search Query

Qwen3-27B decode memory read size calculation
