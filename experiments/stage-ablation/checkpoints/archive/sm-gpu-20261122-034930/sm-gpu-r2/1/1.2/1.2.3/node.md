# N50: 32K 上下文 (seq_len=32768) 下 KV Cache 总显存占用 (Batch=1, FP16)：0.25 MB/token * 32,768 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

32K 上下文 (seq_len=32768) 下 KV Cache 总显存占用 (Batch=1, FP16)：0.25 MB/token * 32,768 tokens = 8,192 MB = 8 GB。若 KV Cache 使用 FP8 量化 (如 vLLM 支持)，则减半为 4 GB；若使用 INT8 则同样为 4 GB。N8 中提到的 10.7GB 可能基于不同的 head_dim 或包含 Padding 的保守估计，需以实际架构参数 (N45) 修正。

## Corrected Claim

在假设 KV Cache 占用率为 0.25 MB/token (FP16) 的前提下，32K 上下文 (Batch=1) 的总显存占用为 8 GB；若使用 FP8 或 INT8 量化，则减半为 4 GB。注意：0.25 MB/token 为特定模型架构下的估算值，实际占用需依据具体模型的层数、头数及 head_dim 计算。

## Evidence

[质询]0.25 MB/token 的 KV Cache 占用率是一个高度依赖具体模型架构（层数、头数、head_dim）的经验参数，并非通用常数。对于常见的 Llama-2-7B 或 Llama-3-8B 模型，该数值通常接近 0.125 MB/token (FP16)，0.25 MB/token 可能对应更大参数量的模型（如 13B/14B）或特定配置。若未明确指定模型，直接使用该数值计算 8GB 存在口径混淆风险。 | 先验知识/题面给定，逻辑校验通过。数学计算 (0.25 * 32768 = 8192) 正确，FP8/INT8 减半逻辑正确。但 0.25 MB/token 为经验事实，缺乏特定模型上下文支持，故降级。
