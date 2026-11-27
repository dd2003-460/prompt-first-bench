# N168: Embedding 层额外显存开销量化：若 tie_word_embeddings=false，额外开销 = (vocab_size * hidden_dim 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

Embedding 层额外显存开销量化：若 tie_word_embeddings=false，额外开销 = (vocab_size * hidden_dim * 2) bytes。假设 vocab_size=152k, hidden_dim=4096，则额外开销 ≈ 152000 * 4096 * 2 / 1024^3 ≈ 1.18 GB。

## Corrected Claim

Embedding 层额外显存开销量化：若 tie_word_embeddings=false，额外开销 = (vocab_size * hidden_dim * 2) bytes。假设 vocab_size=152k, hidden_dim=4096，则额外开销 ≈ 152000 * 4096 * 2 / 1024^3 ≈ 1.18 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 vocab_size * hidden_dim * 2 bytes 符合 FP16 参数存储标准，数值计算 152000 * 4096 * 2 / 1024^3 ≈ 1.179 GB 与陈述一致。
