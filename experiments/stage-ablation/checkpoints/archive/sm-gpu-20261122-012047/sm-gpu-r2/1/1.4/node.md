# N9: FP8 精度下 Qwen3-27B 的静态权重显存占用降至 27 GB (27B params × 1 byte)，KV Cache 若保持 BF16 则总显存

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

FP8 精度下 Qwen3-27B 的静态权重显存占用降至 27 GB (27B params × 1 byte)，KV Cache 若保持 BF16 则总显存需求为 48.7 GB，若 KV Cache 也降至 FP8 则总需求为 37.3 GB。

## Corrected Claim

FP8 精度下 Qwen3-27B 的静态权重显存占用降至 27 GB (27B params × 1 byte)，KV Cache 若保持 BF16 则总显存需求为 48.7 GB，若 KV Cache 也降至 FP8 则总需求为 37.3 GB。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 7 column 5 (char 583)
