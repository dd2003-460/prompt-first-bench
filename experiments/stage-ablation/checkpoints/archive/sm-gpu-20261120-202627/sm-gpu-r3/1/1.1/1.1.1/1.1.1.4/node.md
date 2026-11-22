# N158: Output Head (LM Head) 参数量公式：Params_Output = vocab_size * hidden_dim。若与 Embedding

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

Output Head (LM Head) 参数量公式：Params_Output = vocab_size * hidden_dim。若与 Embedding 共享权重 (tie_word_embeddings=true)，则额外显存占用为 0；若不共享，则额外占用 = vocab_size * hidden_dim * bytes_per_element。

## Corrected Claim

Output Head (LM Head) 参数量公式：Params_Output = vocab_size * hidden_dim。若与 Embedding 共享权重 (tie_word_embeddings=true)，则额外显存占用为 0；若不共享，则额外占用 = vocab_size * hidden_dim * bytes_per_element。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3 tie_word_embeddings config
