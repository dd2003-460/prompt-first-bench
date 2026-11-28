# N168: 在 PP=2 配置下，单卡 V100 (16GB) 可用的 KV Cache 显存上限 = 16GB - Weights_Per_GPU - Activatio

- **status**: degraded
- **level**: L4
- **source**: derived
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

在 PP=2 配置下，单卡 V100 (16GB) 可用的 KV Cache 显存上限 = 16GB - Weights_Per_GPU - Activations_Reserve；对于 Qwen3.8-27B (NVFP4, ~13.5GB weights total)，Weights_Per_GPU ≈ 6.75GB，预留 1GB 激活后，单卡 KV 可用空间 ≈ 8.25GB，对应最大上下文长度需结合 batch_size=8 计算。

## Corrected Claim

在 PP=2 配置下，单卡 V100 (16GB) 可用的 KV Cache 显存上限取决于模型权重在每张卡上的实际占用及激活内存预留；若假设 Qwen3.8-27B (NVFP4) 总权重约 13.5GB 且均匀分布，则单卡权重约 6.75GB，扣除 1GB 激活预留后，单卡 KV 可用空间约为 8.25GB，具体最大上下文长度需结合 batch_size 和模型架构参数进一步计算。

## Evidence

[质询]该陈述包含具体的硬件显存分配经验参数（如激活预留1GB、权重分布假设），属于经验事实而非第一性原理可推导内容，且缺乏外部来源支持以确认Qwen3.8-27B在NVFP4下的确切权重大小及PP=2时的具体切分方式。 | 经验事实，逻辑自洽但缺来源支持
