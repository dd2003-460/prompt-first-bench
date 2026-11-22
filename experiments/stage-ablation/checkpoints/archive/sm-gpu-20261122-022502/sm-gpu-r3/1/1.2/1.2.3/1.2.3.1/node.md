# N121: B200 192GB 在 BF16 下运行 Qwen3-27B 128K 上下文的显存占用计算：权重 54GB + 128K * 0.002GB (KV Cac

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N38

## Claim

B200 192GB 在 BF16 下运行 Qwen3-27B 128K 上下文的显存占用计算：权重 54GB + 128K * 0.002GB (KV Cache/32K) + 2GB 缓冲 = 56.6GB，显存利用率仅 29.48%，剩余 135.4GB 可支持 batch size > 20 或更长上下文 (如 256K tokens)。

## Corrected Claim

B200 192GB 在 BF16 下运行 Qwen3-27B 128K 上下文的显存占用估算：权重约 54GB，加上 KV Cache 及缓冲后总占用约 56.6GB，显存利用率约 29.5%。剩余约 135GB 显存可用于支持更大的 Batch Size 或更长的上下文，具体容量取决于 KV Cache 的实际大小及调度策略。

## Evidence

[质询]KV Cache 的估算系数（0.002GB/32K tokens）缺乏模型具体架构参数（如层数、头数、头维度）的支持，属于经验估算而非精确计算；此外，'batch size > 20' 的结论依赖于具体的并发请求数和序列长度分布，仅凭剩余显存无法直接推导出确切的 batch size 上限，存在逻辑跳跃。 | 先验知识/题面给定，逻辑校验通过。权重 54GB (27B * 2 bytes) 计算正确；总显存 192GB 下 56.6GB 占用率约 29.5% 计算无误。但 KV Cache 系数和 Batch Size 推导为经验估算，非严格第一性原理推导，且无外部来源支持具体系数，故降级。
