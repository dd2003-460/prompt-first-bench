# N48: RTX 4090 在 BF16 精度下运行 Qwen3-27B (54GB 权重) 不可行，因为显存不足；在 INT8 精度下 (33-35GB 总需求) 不可

- **status**: pending
- **level**: L3
- **source**: derived
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9, N10, N11

## Claim

RTX 4090 在 BF16 精度下运行 Qwen3-27B (54GB 权重) 不可行，因为显存不足；在 INT8 精度下 (33-35GB 总需求) 不可行，显存不足；仅在 W4 精度下 (20-25GB 总需求) 可行，但需验证 KV Cache 是否溢出。

## Corrected Claim

RTX 4090 在 BF16 精度下运行 Qwen3-27B 不可行（显存不足）；在 INT8 精度下通常不可行（总需求接近或超过 24GB 显存上限）；在 W4 精度下理论上可能可行，但需严格验证 KV Cache 及激活值开销是否导致显存溢出。

## Evidence

父节点级核验失败（LLM 错误）：Expecting ',' delimiter: line 12 column 4 (char 833)
