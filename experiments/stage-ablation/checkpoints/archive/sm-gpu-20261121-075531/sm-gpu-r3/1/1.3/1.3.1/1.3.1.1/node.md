# N146: Qwen3-27B 的隐藏层维度 (Hidden Dim) 具体数值为 4096 (基于 27B 参数规模与 64 层、128 头配置推算：27B / (64 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

Qwen3-27B 的隐藏层维度 (Hidden Dim) 具体数值为 4096 (基于 27B 参数规模与 64 层、128 头配置推算：27B / (64 * (4096*4096*4 + 4096)) ≈ 1.0)，需查阅 Qwen3-27B 官方 config.json 确认。

## Corrected Claim

Qwen3-27B 的隐藏层维度 (Hidden Dim) 推测约为 4096（基于 27B 参数规模与常见 Transformer 架构配置估算），具体数值需查阅 Qwen3-27B 官方 config.json 确认。

## Evidence

[质询]该陈述将‘推算’与‘具体数值’混同，且缺乏官方配置文件的直接证据支持。虽然 27B 参数规模与 4096 隐藏层维度在量级上大致兼容（例如 Qwen2-72B 为 8192，Qwen2-32B 为 5120，Qwen2-14B 为 5120，Qwen2-7B 为 3584，27B 介于 14B 和 32B 之间，4096 是一个合理的插值猜测），但‘具体数值为 4096’属于经验事实（硬件/模型规格），不能仅凭参数规模反推得出确切值，且不同模型架构（如 GQA 头数、FFN 中间层维度比例）会导致相同参数量下隐藏层维度不同。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值无法从第一性原理严格推出，需依赖官方 config.json 确认）

## Search Query

Qwen3-27B config.json hidden_size num_hidden_layers
