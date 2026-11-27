# N210: KV Cache 量化（INT8/FP8）对显存的影响及质量损失权衡：若将 KV Cache 从 BF16 (2 bytes) 降至 INT8 (1 byte)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54, N56, N57

## Claim

KV Cache 量化（INT8/FP8）对显存的影响及质量损失权衡：若将 KV Cache 从 BF16 (2 bytes) 降至 INT8 (1 byte)，显存占用减半（例如从 1.07GB 降至 0.54GB）。然而，KV Cache 量化会引入累积误差，尤其在长上下文（>16K）下，可能导致注意力机制精度下降。主流框架（vLLM）默认保持 KV Cache 为 BF16/FP16 以保证质量，除非显存极度紧张。对于 32K 上下文，建议优先保证权重精度，KV Cache 保持 BF16，若显存不足则优先增加 Batch Size 或缩短上下文，而非量化 KV。

## Corrected Claim

KV Cache 量化（INT8/FP8）对显存的影响及质量损失权衡：若将 KV Cache 从 BF16 (2 bytes) 降至 INT8 (1 byte)，显存占用减半（例如从 1.07GB 降至 0.54GB）。然而，KV Cache 量化会引入累积误差，尤其在长上下文（>16K）下，可能导致注意力机制精度下降。主流框架（vLLM）默认保持 KV Cache 为 BF16/FP16 以保证质量，除非显存极度紧张。对于 32K 上下文，建议优先保证权重精度，KV Cache 保持 BF16，若显存不足则优先增加 Batch Size 或缩短上下文，而非量化 KV。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16(2字节)转INT8(1字节)显存减半符合数学逻辑；长上下文量化累积误差及vLLM默认策略符合工程常识。
