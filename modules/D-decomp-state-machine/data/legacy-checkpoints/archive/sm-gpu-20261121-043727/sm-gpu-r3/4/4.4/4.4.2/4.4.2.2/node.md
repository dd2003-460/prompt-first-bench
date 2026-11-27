# N188: RTX 4090 在 W4 量化下运行 Qwen3-27B 时的最大并发 Batch Size 计算：假设固定上下文长度 32K Tokens，每 Batch 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N72

## Claim

RTX 4090 在 W4 量化下运行 Qwen3-27B 时的最大并发 Batch Size 计算：假设固定上下文长度 32K Tokens，每 Batch KV Cache 占用 = 32,000 * 128 KB = 4 GB (FP16) 或 2 GB (FP8)，则最大 Batch Size = 8 GB / 4 GB = 2 (FP16) 或 8 GB / 2 GB = 4 (FP8)，考虑激活值开销后实际 Batch Size 可能降至 1-2

## Corrected Claim

RTX 4090 在 W4 量化下运行 Qwen3-27B 时，若假设每 Token KV Cache 占用约 128 KB 且可用显存为 8 GB，则理论最大 Batch Size 约为 2 (FP16) 或 4 (FP8)，实际受激活值等开销影响可能降至 1-2。

## Evidence

[质询]KV Cache 占用量的计算依据（128 KB/token）缺乏模型具体架构参数（如层数、头数、头维度）的支持，属于经验估算而非精确推导；且未明确 8GB 是显存剩余量还是总显存扣除模型权重后的可用量，存在口径模糊。 | 先验知识/题面给定，逻辑校验通过：算术运算正确（32000*128KB=4GB, 8/4=2），量级符合大模型推理常识，但具体 KV 大小依赖模型结构，属经验事实，降级为定性表述。
