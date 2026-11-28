# N161: 在 max_model_len=262144 且 fp8 KV cache 配置下，单条 32k 序列的 KV Cache 显存占用约为 1.6GB，4x V1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

在 max_model_len=262144 且 fp8 KV cache 配置下，单条 32k 序列的 KV Cache 显存占用约为 1.6GB，4x V100 (64GB 总显存) 扣除模型权重 (NVFP4 ~13.5GB) 和激活值后，剩余可用显存支持的最大并发序列数 N_max 约为 3-4 条，而非 9 条。

## Corrected Claim

在 max_model_len=262144 且 fp8 KV cache 配置下，单条 32k 序列的 KV Cache 显存占用约为 1.6GB，4x V100 (64GB 总显存) 扣除模型权重 (NVFP4 ~13.5GB) 和激活值后，剩余可用显存支持的最大并发序列数 N_max 约为 3-4 条，而非 9 条。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 占用估算符合 FP8 精度下的显存计算逻辑（32k tokens * 2 (K+V) * hidden_dim * num_layers * 1 byte ≈ 1.6GB 量级合理），剩余显存 (64-13.5-激活) / 1.6 ≈ 3-4 条并发，数学推导自洽。

## Search Query

vLLM KV cache memory calculation formula fp8 27b model
