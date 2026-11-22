# N240: 单卡 RTX 4090 在 W4A16 权重 + INT8 KV Cache + 32K 上下文下的实际推理性能瓶颈分析：权重读取带宽 1008 GB/s，每 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82, N83, N84

## Claim

单卡 RTX 4090 在 W4A16 权重 + INT8 KV Cache + 32K 上下文下的实际推理性能瓶颈分析：权重读取带宽 1008 GB/s，每 Token 生成需读取 13.5GB 权重 + 4.0GB KV Cache = 17.5GB 数据。理论最大吞吐 = 1008 / 17.5 ≈ 57.6 Tokens/s。考虑内存控制器效率 (85%) 和计算开销，实际预期吞吐约为 49 Tokens/s。此性能显著高于 N143 中仅计权重的 37-40 Tokens/s，表明 KV 量化不仅解决显存问题，还因减少内存读取量而提升速度。

## Corrected Claim

单卡 RTX 4090 在 W4A16 权重 + INT8 KV Cache + 32K 上下文下，若模型权重为 13.5GB（约 27B 参数），每 Token 生成需读取 17.5GB 数据，理论最大吞吐约 57.6 Tokens/s，实际预期约 49 Tokens/s。此性能高于仅计权重的 37-40 Tokens/s，表明 KV 量化在解决显存问题的同时，因减少内存读取量而提升速度。

## Evidence

[质询]数值量级与模型规模假设存在潜在矛盾：13.5GB 的 W4A16 权重仅对应约 27B 参数的模型（如 Llama-3-70B 的 W4 权重约为 35-40GB，Llama-3-8B 约为 4-5GB）。若该节点隐含指代主流大模型（如 70B+），则 13.5GB 权重数据严重偏低，导致吞吐计算错误；若指代 27B 模型，则需明确模型规模，否则‘显著高于 N143’的对比缺乏统一基准。此外，4.0GB KV Cache 在 32K 上下文下对于 27B 模型（假设 GQA 8:1）是合理的，但对于 70B 模型则偏低，进一步暗示模型规模假设模糊。 | 先验知识/题面给定，逻辑校验通过（带宽/数据量/吞吐公式自洽），但经验事实（具体模型权重大小与 KV 大小）缺乏来源支持且存在模型规模歧义，故降级。

## Search Query

RTX 4090 LLM inference throughput memory bandwidth bottleneck W4A16 INT8 KV
