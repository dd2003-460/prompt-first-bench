# N297: Intel Arc A770 运行 Qwen3-27B 时，由于 16GB 显存无法容纳全部权重+KV Cache，必须启用 CPU 内存卸载（Offloadi

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N92

## Claim

Intel Arc A770 运行 Qwen3-27B 时，由于 16GB 显存无法容纳全部权重+KV Cache，必须启用 CPU 内存卸载（Offloading），此时推理瓶颈从 GPU 算力转变为 PCIe 4.0 x4 带宽（约 4 GB/s），导致 Decode 速度骤降至 1-2 tokens/s，远低于 RTX 4090 的 65 tokens/s，使得其'性价比'在延迟敏感场景下失效

## Corrected Claim

Intel Arc A770 运行 Qwen3-27B 时，若 16GB 显存无法容纳全部权重+KV Cache，启用 CPU 内存卸载后，推理瓶颈可能转变为 PCIe 4.0 x4 带宽（有效吞吐率约 4-8 GB/s），导致 Decode 速度显著下降（可能降至 1-5 tokens/s 范围），在延迟敏感场景下其性能优势可能减弱，但‘性价比失效’需结合具体应用场景和量化策略进一步评估。

## Evidence

[质询]PCIe 4.0 x4 带宽标称约 8 GB/s（单向），陈述中‘约 4 GB/s’可能混淆了双向或有效吞吐率；此外，Qwen3-27B 若采用 4-bit 量化，权重约 14-15GB，加上 KV Cache 确实可能超出 16GB 显存，但具体是否‘必须’卸载取决于量化精度和上下文长度，且 Decode 速度受内存带宽限制，1-2 tokens/s 的数值在低带宽下是合理的，但‘远低于 RTX 4090 的 65 tokens/s’这一对比在延迟敏感场景下的‘性价比失效’结论过于绝对，未考虑不同场景下的权衡。 | 先验知识/题面给定，逻辑校验通过：PCIe 4.0 x4 带宽限制导致 CPU 卸载时 Decode 速度下降是合理的，但具体数值和对比需更多上下文支持。

## Search Query

Intel Arc A770 LLM inference speed tokens per second offloading
