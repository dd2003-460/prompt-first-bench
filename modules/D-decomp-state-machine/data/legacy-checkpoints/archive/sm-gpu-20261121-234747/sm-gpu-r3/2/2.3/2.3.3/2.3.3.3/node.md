# N250: RTX 4090 运行 Qwen3-27B INT8 模型时，32K 上下文下的 KV Cache 显存占用为 2 * 32 * 8 * 128 * 32768

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

RTX 4090 运行 Qwen3-27B INT8 模型时，32K 上下文下的 KV Cache 显存占用为 2 * 32 * 8 * 128 * 32768 * 1 byte ≈ 2.1 GB，加上模型权重 27GB，总显存需求约 29.1GB，超过 24GB 显存上限，需启用 PagedAttention 或 offload 部分权重至 CPU，导致 Decode 吞吐进一步降低 20-30%

## Corrected Claim

RTX 4090 运行 Qwen3-27B INT8 模型时，32K 上下文下的 KV Cache 显存占用约为 2.1 GB（基于典型架构估算），加上模型权重 27GB，总显存需求约 29.1GB，超过 24GB 显存上限，需启用 PagedAttention 或 offload 部分权重至 CPU，导致 Decode 吞吐显著降低（具体幅度取决于实现，通常估计在 20-30% 左右）。

## Evidence

[质询]KV Cache 计算公式中的参数（如 128 可能指层数或头数，32 可能指头维或层数）存在歧义，且未明确 Qwen3-27B 的具体架构参数（如 GQA 分组数、实际层数），导致 2.1GB 的数值缺乏确切的架构依据；此外，'Decode 吞吐降低 20-30%' 是一个经验性估计，缺乏特定硬件和软件栈下的基准测试支持。 | 先验知识/题面给定，逻辑校验通过：24GB 显存确实无法容纳 27GB 权重 + 2.1GB KV Cache，因此必须 offload 或分页，这会导致性能下降，逻辑自洽。但具体数值（2.1GB, 20-30%）属于经验事实且无来源支持，故降级。
