# N115: 假设生成新颖度的量化公式：Novelty Score = 1 - CosineSimilarity(E_hypothesis, E_existing_liter

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

假设生成新颖度的量化公式：Novelty Score = 1 - CosineSimilarity(E_hypothesis, E_existing_literature)，其中 E 为 Sentence-BERT 嵌入向量；要求均值 > 6.0 (映射为 0.6-1.0 区间) 意味着与现有文献的相似度需 < 0.4；27B 模型在无外部知识库检索时，生成的假设往往局限于训练数据内的已知组合，Novelty Score 均值通常仅为 4.5-5.5，需引入 RAG 检索最新 arXiv 论文以将相似度降至 0.3 以下。

## Corrected Claim

假设生成新颖度可量化为 Novelty Score = 1 - CosineSimilarity(E_hypothesis, E_existing_literature)。通常认为较高的Novelty Score（如映射后>6.0，即相似度<0.4）代表更高的新颖性。对于中等规模（如27B）模型，若无外部检索，其生成内容往往受限于训练数据分布，新颖度可能较低；引入RAG检索最新文献有助于降低与现有文献的相似度，从而提升新颖度评分。

## Evidence

[质询]该陈述包含具体的经验性数值断言（如27B模型Novelty Score均值为4.5-5.5，RAG后相似度<0.3），这些具体参数值并非第一性原理可推导，且参考来源中未提供针对'27B模型'或'Sentence-BERT嵌入余弦相似度'这一特定量化体系的具体基准数据，来源[1]讨论的是不同的NovelSum指标，来源[2]和[3]为通用概念介绍，缺乏对该特定经验数值的直接支持。 | 逻辑上公式定义自洽（Novelty=1-Similarity，均值>6.0对应0.6-1.0区间即Sim<0.4），但关于27B模型的具体表现数值（4.5-5.5）及RAG效果（Sim<0.3）属于经验事实，参考来源[1][2][3]均未提供直接数据支持，仅能确认逻辑结构合理，故降级。

## Search Query

LLM hypothesis generation novelty score cosine similarity benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/w2001ky/article/details/159157799&rut=5560fe2862905eb546a1f0b629bb3179ea963b96ae09125545efb3fdc4e35e73', 'type': 'ddg', 'title': '数据新颖度 NovelSum 的计算卡点，求助大佬指导 - CSDN博客'}
- {'url': 'https://codingace.net/ai/novelty_score.html&rut=6bb5178bdd777ab80edf5f38040f0624b14480888196d72fada515a815438eeb', 'type': 'ddg', 'title': 'Novelty Score Calculator for AI and Machine Learning'}
- {'url': 'https://blog.csdn.net/weixin_40920183/article/details/121710361&rut=a9ce21f81ddc86648e4a40f72cd4d215d885a926ee388a0fe129d030f9b92225', 'type': 'ddg', 'title': 'AI论文中的novelty如何评价？ - CSDN博客'}
