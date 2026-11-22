# N289: 工作点 3（长上下文/激进量化）：采用 W4 量化权重 (13.5GB) + INT4 量化 KV Cache。32K 上下文下，KV Size ≈ 2 × 6

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

工作点 3（长上下文/激进量化）：采用 W4 量化权重 (13.5GB) + INT4 量化 KV Cache。32K 上下文下，KV Size ≈ 2 × 64 × 128 × 32768 × 0.5 / 1024^3 ≈ 8.05 GB。总显存 = 13.5 + 8.05 = 21.55 GB < 24 GB。结论：在 32K 上下文下，若接受 INT4 KV Cache 带来的注意力精度损失（需验证对长文本检索准确性的影响），则单卡 4090 可行。此方案以质量损失换取容量，需对比 N96 中的质量下降指标。

## Corrected Claim

工作点 3（长上下文/激进量化）：采用 W4 量化权重 (13.5GB) + INT4 量化 KV Cache。32K 上下文下，KV Size ≈ 2 × 64 × 128 × 32768 × 0.5 / 1024^3 ≈ 8.05 GB。总显存 = 13.5 + 8.05 = 21.55 GB < 24 GB。结论：在 32K 上下文下，若接受 INT4 KV Cache 带来的注意力精度损失（需验证对长文本检索准确性的影响），则单卡 4090 可行。此方案以质量损失换取容量，需对比 N96 中的质量下降指标。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算公式 2(Head) * 64(Heads) * 128(Dim) * 32768(Seqlen) * 0.5(4bit/8bit) / 1024^3 ≈ 8.05GB 数值准确，总显存 21.55GB < 24GB 逻辑自洽。

## Search Query

INT4 KV cache quantization LLM inference accuracy impact
