# N82: RTX 4090 运行 Qwen3-27B W4A16 (AWQ/GPTQ) 时，因 KV Cache 为 BF16 且权重反量化至 FP16 计算，实际显存占

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

RTX 4090 运行 Qwen3-27B W4A16 (AWQ/GPTQ) 时，因 KV Cache 为 BF16 且权重反量化至 FP16 计算，实际显存占用约为 17GB (权重) + 40GB (32K KV Cache, 基于N25修正) + 2GB (激活/开销) = 59GB，远超 24GB 显存上限，故该配置在 32K 上下文下不可行，必须采用 KV Cache 量化 (INT8/FP8) 或降低上下文长度。

## Corrected Claim

RTX 4090 运行 Qwen3-27B W4A16 (AWQ/GPTQ) 时，因 KV Cache 为 BF16 且权重反量化至 FP16 计算，实际显存占用约为 17GB (权重) + 40GB (32K KV Cache, 基于N25修正) + 2GB (激活/开销) = 59GB，远超 24GB 显存上限，故该配置在 32K 上下文下不可行，必须采用 KV Cache 量化 (INT8/FP8) 或降低上下文长度。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存为 24GB，而计算得出的 59GB 显存需求（17GB 权重 + 40GB KV Cache + 2GB 开销）远超此上限，结论在逻辑和物理限制上自洽。

## Search Query

RTX 4090 Qwen3 27B 32k context memory usage KV cache quantization
