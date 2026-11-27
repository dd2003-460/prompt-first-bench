# N160: 激活值 (Activations) 显存开销的量化估算：在 LLM 推理中，激活值主要取决于 Batch Size 和 Sequence Length。对于单序

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

激活值 (Activations) 显存开销的量化估算：在 LLM 推理中，激活值主要取决于 Batch Size 和 Sequence Length。对于单序列 (Batch=1) 32K 上下文，激活值开销通常较小，约 1-2 GB。但在 Prefill 阶段，若使用 FlashAttention，激活值会被分块处理，峰值显存可能增加 5-10%。因此，在 65 GB 基线之上，需预留 5-8 GB 的安全边际，总需求上限约为 70-73 GB。

## Corrected Claim

激活值 (Activations) 显存开销的量化估算：在 LLM 推理中，激活值主要取决于 Batch Size 和 Sequence Length。对于单序列 (Batch=1) 32K 上下文，激活值开销通常较小，约 1-2 GB。但在 Prefill 阶段，若使用 FlashAttention，激活值会被分块处理，峰值显存可能增加 5-10%。因此，在 65 GB 基线之上，需预留 5-8 GB 的安全边际，总需求上限约为 70-73 GB。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference activation memory overhead flash attention prefill
