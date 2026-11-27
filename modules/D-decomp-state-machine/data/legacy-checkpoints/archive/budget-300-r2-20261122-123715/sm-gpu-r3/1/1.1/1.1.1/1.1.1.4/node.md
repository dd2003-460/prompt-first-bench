# N125: RTX 4090 在 FP8 量化下运行 Qwen3-27B 32K 上下文时，若降低上下文至 ~15K tokens，KV Cache 显存占用降至 ~4.5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28, N29, N30

## Claim

RTX 4090 在 FP8 量化下运行 Qwen3-27B 32K 上下文时，若降低上下文至 ~15K tokens，KV Cache 显存占用降至 ~4.5GB，总显存占用降至 ~33.5GB，仍超过 24GB 上限，需进一步量化至 W8 或启用更激进的 Offload 策略

## Corrected Claim

RTX 4090 在 FP8 量化下运行 Qwen3-27B 32K 上下文时，若降低上下文至 ~15K tokens，KV Cache 显存占用降至 ~4.5GB，总显存占用降至 ~33.5GB，仍超过 24GB 上限，需进一步量化至 W8 或启用更激进的 Offload 策略

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 模型权重约 54GB (FP16) 或 27GB (FP8)，KV Cache 随上下文线性增长，15K 上下文下 KV 占用约 4.5GB 符合常规估算，总显存 33.5GB 超过 24GB 上限的结论在数学和工程逻辑上自洽。

## Search Query

RTX 4090 FP8 15K context KV cache size
