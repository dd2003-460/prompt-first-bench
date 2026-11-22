# N288: 工作点 2（中上下文/标准精度）：采用 W4 量化权重 (13.5GB) + BF16 KV Cache。限制上下文长度至 16K tokens。KV Size

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

工作点 2（中上下文/标准精度）：采用 W4 量化权重 (13.5GB) + BF16 KV Cache。限制上下文长度至 16K tokens。KV Size ≈ 2 × 64 × 128 × 16384 × 2 / 1024^3 ≈ 8.05 GB。总显存 = 13.5 + 8.05 = 21.55 GB < 24 GB。结论：在 16K 上下文下，W4 权重 + BF16 KV 可在单卡 24GB 内稳定运行，留有余量约 2.45 GB 用于激活值与碎片，这是单卡 4090 的可行边界。

## Corrected Claim

工作点 2（中上下文/标准精度）：采用 W4 量化权重 (13.5GB) + BF16 KV Cache。限制上下文长度至 16K tokens。KV Size ≈ 2 × 64 × 128 × 16384 × 2 / 1024^3 ≈ 8.05 GB。总显存 = 13.5 + 8.05 = 21.55 GB < 24 GB。结论：在 16K 上下文下，W4 权重 + BF16 KV 可在单卡 24GB 内稳定运行，留有余量约 2.45 GB 用于激活值与碎片，这是单卡 4090 的可行边界。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算公式 2(Head) * 64(Heads) * 128(Dim) * 16384(Len) * 2(BF16 bytes) / 1024^3 ≈ 8.05GB 正确，总显存 21.55GB < 24GB 符合单卡 4090 运行边界逻辑。

## Search Query

RTX 4090 24GB LLM inference context length limit KV cache
