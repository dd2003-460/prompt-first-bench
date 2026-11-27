# N302: 32K 上下文下单请求的总 KV Cache 显存占用量化：Total_KV_per_request = KV_bytes_per_token * 32,768

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N97

## Claim

32K 上下文下单请求的总 KV Cache 显存占用量化：Total_KV_per_request = KV_bytes_per_token * 32,768；BF16 下为 4 GB，FP8 下为 2 GB，INT8 下为 2 GB。

## Corrected Claim

在特定模型架构（如 Llama-3-70B 级别，KV Cache 每 token 约 128KB @BF16）下，32K 上下文单请求 KV Cache 显存占用约为：BF16 4 GB，FP8/INT8 2 GB。

## Evidence

[质询]该陈述隐含了特定的模型架构参数（如层数、头数、头维度），但未在陈述中明确给出。例如，若假设 KV_bytes_per_token 为 128KB（对应 Llama-3-70B 等特定配置），则 32K 上下文下 BF16 占用约为 4GB，但 FP8 和 INT8 通常均为 2GB 的前提是量化后字节数减半。然而，不同模型（如 Llama-2-7B vs Llama-3-70B）的 KV Cache 大小差异巨大，直接给出固定数值（4GB/2GB）而缺乏模型规格限定，存在以偏概全或参数假设不透明的风险。 | 先验知识/题面给定，逻辑校验通过。公式 Total_KV = KV_per_token * Context_Length 逻辑自洽。数值量级（BF16 4GB, FP8/INT8 2GB）符合常见大模型（如 70B 级别）在 32K 上下文下的工程估算惯例（假设 KV_per_token ~ 128KB for BF16）。虽无外部来源直接覆盖具体数值，但作为 knowledge 节点，逻辑与量级合理，故保留但降级以提示参数依赖性。
