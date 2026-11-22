# N44: Qwen3-27B 嵌入层参数量计算：Input_Embedding = vocab_size * hidden_size = 152,064 * 4096 ≈

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Qwen3-27B 嵌入层参数量计算：Input_Embedding = vocab_size * hidden_size = 152,064 * 4096 ≈ 622.8e6；Output_Head = vocab_size * hidden_size ≈ 622.8e6 (因为 tie_word_embeddings=False)；总 Embedding 参数 ≈ 1.246e9。

## Corrected Claim

Qwen3-27B 嵌入层参数量计算：Input_Embedding = vocab_size * hidden_size = 152,064 * 4096 ≈ 622.8e6；Output_Head = vocab_size * hidden_size ≈ 622.8e6 (因为 tie_word_embeddings=False)；总 Embedding 参数 ≈ 1.246e9。

## Evidence

先验知识/题面给定，逻辑校验通过：152,064 * 4,096 = 622,854,144 ≈ 622.8e6，两倍即为 1.246e9，计算无误且符合 Qwen3-27B 架构参数设定。
