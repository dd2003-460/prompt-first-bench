# N45: Qwen3-27B 在 INT4/W4 精度下的权重显存占用为 13.5 GB，加上 32K 上下文 KV Cache (约 1.07 GB，假设 KV 保持 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

Qwen3-27B 在 INT4/W4 精度下的权重显存占用为 13.5 GB，加上 32K 上下文 KV Cache (约 1.07 GB，假设 KV 保持 BF16/FP16) 及 15% 开销，总需求约 17.2 GB，低于 RTX 4090 的 24 GB 显存上限，单卡 INT4 方案可行且余量约 6.8 GB

## Corrected Claim

Qwen3-27B 在 INT4/W4 精度下的权重显存占用为 13.5 GB，加上 32K 上下文 KV Cache (约 1.07 GB，假设 KV 保持 BF16/FP16) 及 15% 开销，总需求约 17.2 GB，低于 RTX 4090 的 24 GB 显存上限，单卡 INT4 方案可行且余量约 6.8 GB

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 749)
