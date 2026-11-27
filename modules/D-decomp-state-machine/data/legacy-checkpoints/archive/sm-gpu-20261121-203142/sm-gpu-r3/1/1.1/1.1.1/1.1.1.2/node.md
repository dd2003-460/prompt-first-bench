# N127: BF16 权重显存占用计算需包含 Embedding 层和 LM Head 层的参数，若 config 中 tie_word_embeddings=true，则

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

BF16 权重显存占用计算需包含 Embedding 层和 LM Head 层的参数，若 config 中 tie_word_embeddings=true，则 Embedding 与 LM Head 共享权重，需从总参数量中扣除重复部分以避免高估显存占用约 1-2GB

## Corrected Claim

BF16 权重显存占用计算需包含 Embedding 层和 LM Head 层的参数，若 config 中 tie_word_embeddings=true，则 Embedding 与 LM Head 共享权重，需从总参数量中扣除重复部分以避免高估显存占用约 1-2GB

## Evidence

先验知识/题面给定，逻辑校验通过：BF16下参数量与显存占用线性相关，tie_word_embeddings机制确实导致Embedding与LM Head共享权重，扣除重复部分符合内存计算逻辑，1-2GB量级对于常见LLM词表规模（如32k-128k）合理。
