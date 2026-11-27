# N407: 修正 N134 中的带宽假设：RTX 4090 的显存带宽为 1008 GB/s (GDDR6X)，而非 N134 可能隐含的更低值；在 INT4 量化（权重 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N134

## Claim

修正 N134 中的带宽假设：RTX 4090 的显存带宽为 1008 GB/s (GDDR6X)，而非 N134 可能隐含的更低值；在 INT4 量化（权重 13.5GB）且 32K 上下文 KV Cache 为 8GB (N370 修正值，基于 BF16 KV) 时，理论 Decode 吞吐上限为 1008 / (13.5 + 8.0) ≈ 46.9 tokens/s，修正后数值略高于 N134 的 45.5 tokens/s（因 N134 使用了未修正的 8.59GB KV 值）。

## Corrected Claim

修正 N134 中的带宽假设：RTX 4090 的显存带宽为 1008 GB/s (GDDR6X)，而非 N134 可能隐含的更低值；在 INT4 量化（权重 13.5GB）且 32K 上下文 KV Cache 为 8GB (N370 修正值，基于 BF16 KV) 时，理论 Decode 吞吐上限为 1008 / (13.5 + 8.0) ≈ 46.9 tokens/s，修正后数值略高于 N134 的 45.5 tokens/s（因 N134 使用了未修正的 8.59GB KV 值）。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽 1008 GB/s 为公认规格；算术运算 1008 / (13.5 + 8.0) = 1008 / 21.5 ≈ 46.88，四舍五入为 46.9 tokens/s，与陈述一致；且 46.9 > 45.5 符合因分母减小（8.0 < 8.59）导致结果增大的逻辑。

## Search Query

RTX 4090 memory bandwidth 1008 GB/s spec
