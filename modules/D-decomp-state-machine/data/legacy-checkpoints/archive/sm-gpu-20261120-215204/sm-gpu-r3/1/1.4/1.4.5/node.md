# N49: RTX 5090 在 BF16 精度下运行 Qwen3-27B (54GB 权重 + 40GB KV Cache = 94GB) 不可行，显存不足；在 INT8

- **status**: pending
- **level**: L3
- **source**: derived
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9, N10, N11

## Claim

RTX 5090 在 BF16 精度下运行 Qwen3-27B (54GB 权重 + 40GB KV Cache = 94GB) 不可行，显存不足；在 INT8 精度下 (33-35GB 总需求) 可行；在 W4 精度下 (20-25GB 总需求) 可行且余量充足。

## Corrected Claim

RTX 5090 (32GB 显存) 在 BF16 精度下运行 Qwen3-27B 不可行，显存不足；在 INT8 或 W4 精度下，若总显存需求控制在 32GB 以内，则可行。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 776)
