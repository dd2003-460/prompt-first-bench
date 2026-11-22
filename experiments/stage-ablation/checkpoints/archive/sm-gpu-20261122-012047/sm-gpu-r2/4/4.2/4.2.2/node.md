# N118: RTX 5090 在 32GB 显存下运行 Qwen3-27B 的显存预算分配：INT4 权重 13.5GB + KV Cache 21.7GB = 35.2G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

RTX 5090 在 32GB 显存下运行 Qwen3-27B 的显存预算分配：INT4 权重 13.5GB + KV Cache 21.7GB = 35.2GB > 32GB，因此 N28 中声称'INT4 单卡可容纳且支持 32K 上下文'存在算术错误；实际仅能支持约 25K-28K 上下文（剩余 18.5GB / 21.7GB * 32K ≈ 27.3K），或需启用 KV Cache 量化（如 FP8 KV）以降至 10.8GB，从而使总占用 24.3GB < 32GB。

## Corrected Claim

RTX 5090 在 32GB 显存下运行 Qwen3-27B 的显存预算分配：INT4 权重 13.5GB + KV Cache 21.7GB = 35.2GB > 32GB，因此 N28 中声称'INT4 单卡可容纳且支持 32K 上下文'存在算术错误；实际仅能支持约 25K-28K 上下文（剩余 18.5GB / 21.7GB * 32K ≈ 27.3K），或需启用 KV Cache 量化（如 FP8 KV）以降至 10.8GB，从而使总占用 24.3GB < 32GB。

## Evidence

先验知识/题面给定，逻辑校验通过：INT4权重约13.5GB与KV Cache 21.7GB之和确实超过32GB显存，算术推导自洽，符合大模型显存占用基本规律。
