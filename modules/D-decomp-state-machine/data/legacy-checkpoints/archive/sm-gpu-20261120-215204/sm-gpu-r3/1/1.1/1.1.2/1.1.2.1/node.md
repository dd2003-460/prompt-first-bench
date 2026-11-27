# N159: 基于修正后的 KV Cache 大小 (8 GB for BF16)，Qwen3-27B 在 BF16 精度下的总硬性显存需求修正为：54 GB (权重) + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

基于修正后的 KV Cache 大小 (8 GB for BF16)，Qwen3-27B 在 BF16 精度下的总硬性显存需求修正为：54 GB (权重) + 8 GB (KV Cache) + 2-3 GB (激活值/框架开销) ≈ 64-65 GB。这意味着 1x A100 40GB 不可行，但 1x A100 80GB 可行，且 1x RTX 4090 24GB 绝对不可行，2x RTX 4090 (48GB) 在 BF16 下仍不可行（需 65GB），必须使用量化权重 (W8/W4) 或降低上下文长度。

## Corrected Claim

基于修正后的 KV Cache 大小 (8 GB for BF16)，Qwen3-27B 在 BF16 精度下的总硬性显存需求修正为：54 GB (权重) + 8 GB (KV Cache) + 2-3 GB (激活值/框架开销) ≈ 64-65 GB。这意味着 1x A100 40GB 不可行，但 1x A100 80GB 可行，且 1x RTX 4090 24GB 绝对不可行，2x RTX 4090 (48GB) 在 BF16 下仍不可行（需 65GB），必须使用量化权重 (W8/W4) 或降低上下文长度。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB，加上8GB KV Cache及2-3GB开销，总需求约64-65GB，符合显存计算逻辑。

## Search Query

Qwen3-27B total VRAM requirement BF16 32k context
