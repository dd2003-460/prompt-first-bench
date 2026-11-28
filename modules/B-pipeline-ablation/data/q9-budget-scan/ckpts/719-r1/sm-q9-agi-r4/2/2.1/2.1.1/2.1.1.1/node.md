# N142: 测试集构建参数：从 Nature/Science 子刊近 2 年摘要中随机抽样 100 篇，每篇摘要平均长度 150-200 tokens，构建倒排索引时使用的

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

测试集构建参数：从 Nature/Science 子刊近 2 年摘要中随机抽样 100 篇，每篇摘要平均长度 150-200 tokens，构建倒排索引时使用的分词器需与 Qwen3.8-27B 训练分词器兼容（如使用 SentencePiece BPE 或 jieba），否则 BM25 匹配率将因 Token 不一致而下降 10%-20%

## Corrected Claim

测试集构建参数：从 Nature/Science 子刊近 2 年摘要中随机抽样 100 篇，每篇摘要平均长度 150-200 tokens。构建倒排索引时，建议直接使用 Qwen3.8-27B 的原生分词器（如 SentencePiece BPE）以确保 Token 一致性；若使用其他分词器（如 jieba），需评估其对 BM25 匹配率的具体影响，避免 Token 不一致导致的性能下降。

## Evidence

父节点级核验未通过：不完备（子节点之间存在轻微的内容重叠（子节点2在提出解决方案时隐含了子节点1的问题背景），但核心关注点不同（一个侧重影响量化/纠错，一个侧重操作策略），可视为正交。然而，完备性不足：父节点明确包含‘从 Nature/Science 子刊近 2 年摘要中随机抽样 100 篇’以及‘每篇摘要平均长度 150-200 tokens’这两个具体的数据集构建参数，但两个子节点均完全未涉及数据源、时间范围、样本量或长度分布等关键信息，仅聚焦于分词器问题。）
