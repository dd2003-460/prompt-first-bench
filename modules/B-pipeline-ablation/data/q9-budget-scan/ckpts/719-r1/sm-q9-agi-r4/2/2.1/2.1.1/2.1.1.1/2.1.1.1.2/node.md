# N422: 正确的分词器对齐策略：必须使用 Qwen3.8-27B 的原生分词器 (tokenizer) 对 Nature/Science 摘要进行预处理，生成 Token

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N142

## Claim

正确的分词器对齐策略：必须使用 Qwen3.8-27B 的原生分词器 (tokenizer) 对 Nature/Science 摘要进行预处理，生成 Token ID 序列，再构建倒排索引。这样 BM25 的 TF/IDF 计算基于相同的词汇表，匹配率应为 100% (理论)。若强行使用 jieba，需建立 jieba-word -> Qwen-token 的映射表，但该映射是多对多的，会导致 IDF 计算失真。

## Corrected Claim

正确的分词器对齐策略：必须使用 Qwen3.8-27B 的原生分词器 (tokenizer) 对 Nature/Science 摘要进行预处理，生成 Token ID 序列，再构建倒排索引。这样 BM25 的 TF/IDF 计算基于相同的词汇表，匹配率应为 100% (理论)。若强行使用 jieba，需建立 jieba-word -> Qwen-token 的映射表，但该映射是多对多的，会导致 IDF 计算失真。

## Evidence

先验知识/题面给定，逻辑校验通过：使用原生分词器确保词汇表一致是信息检索系统构建倒排索引的标准最佳实践，能避免跨分词器映射带来的IDF计算偏差和匹配丢失，逻辑自洽且符合工程直觉。

## Search Query

Qwen3 tokenizer SentencePiece BPE implementation details
