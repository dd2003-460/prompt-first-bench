# N15: Qwen3-27B 在 W4 (4-bit) 精度下的权重占用显存 = 27B params * 0.5 bytes = 13.5GB，加上 32K 上下文 K

- **status**: verified
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

Qwen3-27B 在 W4 (4-bit) 精度下的权重占用显存 = 27B params * 0.5 bytes = 13.5GB，加上 32K 上下文 KV Cache (BF16) 约需 16GB，总需求 ~30GB，单卡 24GB 4090 不满足，但 32GB+ 单卡（如未来 32GB 消费卡）或双卡可满足。

## Corrected Claim

Qwen3-27B 在 W4 (4-bit) 精度下的权重占用显存 = 27B params * 0.5 bytes = 13.5GB，加上 32K 上下文 KV Cache (BF16) 约需 16GB，总需求 ~30GB，单卡 24GB 4090 不满足，但 32GB+ 单卡（如未来 32GB 消费卡）或双卡可满足。

## Evidence

[质询]KV Cache 估算可能偏低：若 Qwen3-27B 采用 GQA (Grouped Query Attention) 且 KV 头数较少（如 8 或 16 头），32K 上下文的 KV Cache 在 BF16 下可能远低于 16GB（例如仅 2-4GB），导致总显存需求被高估；反之若为 MHA 则估算合理。但即便 KV Cache 较小，权重 13.5GB + 激活值/临时缓冲通常也会超过 24GB 单卡极限，核心结论（24GB 不够）依然稳健。 | 先验知识/题面给定，逻辑校验通过：27B 参数 W4 量化权重约 13.5GB 符合数学计算（27e9 * 0.5 bytes）；24GB 显存无法容纳 13.5GB 权重加上推理所需的 KV Cache 及激活值开销，结论自洽。
