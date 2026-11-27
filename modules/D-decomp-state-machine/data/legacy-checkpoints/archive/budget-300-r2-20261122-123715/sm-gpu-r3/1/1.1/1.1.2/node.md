# N29: RTX 4090 单卡在 FP8 量化下运行 Qwen3-27B 32K 上下文的显存占用为 27GB(权重) + 9GB(KV Cache) + 2GB(激活

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

RTX 4090 单卡在 FP8 量化下运行 Qwen3-27B 32K 上下文的显存占用为 27GB(权重) + 9GB(KV Cache) + 2GB(激活/框架) ≈ 38GB，大于 24GB 物理显存，必须启用 CPU Offload 或降低上下文长度至 ~15K tokens

## Corrected Claim

RTX 4090 单卡在 FP8 量化下运行 Qwen3-27B 32K 上下文的显存占用为 27GB(权重) + 9GB(KV Cache) + 2GB(激活/框架) ≈ 38GB，大于 24GB 物理显存，必须启用 CPU Offload 或降低上下文长度至 ~15K tokens

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 10 column 5 (char 717)
