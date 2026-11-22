# N41: Qwen3-27B 的总参数量分解：Total_Params = n_layers * (Attention_Params + FFN_Params) + Em

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Qwen3-27B 的总参数量分解：Total_Params = n_layers * (Attention_Params + FFN_Params) + Embedding_Params，其中 Attention_Params = 4 * hidden_size^2 (QKV投影+输出投影)，FFN_Params = 3 * hidden_size * intermediate_size (Gate, Up, Down)，Embedding_Params = vocab_size * hidden_size (若 tie_word_embeddings=False，则需额外加上 Output Head 的 vocab_size * hidden_size)。

## Corrected Claim

Qwen3-27B 的总参数量分解：Total_Params = n_layers * (Attention_Params + FFN_Params) + Embedding_Params，其中 Attention_Params = 4 * hidden_size^2 (QKV投影+输出投影)，FFN_Params = 3 * hidden_size * intermediate_size (Gate, Up, Down)，Embedding_Params = vocab_size * hidden_size (若 tie_word_embeddings=False，则需额外加上 Output Head 的 vocab_size * hidden_size)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3 27B architecture parameters breakdown attention ffn embedding
