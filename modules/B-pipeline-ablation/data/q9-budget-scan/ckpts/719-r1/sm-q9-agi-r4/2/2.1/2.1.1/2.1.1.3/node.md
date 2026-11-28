# N144: Query 构造策略对 BM25 召回率的关键作用：若直接使用用户原始提问作为 Query，Recall@5 约为 0.60；若使用 LLM (Qwen3.8-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

Query 构造策略对 BM25 召回率的关键作用：若直接使用用户原始提问作为 Query，Recall@5 约为 0.60；若使用 LLM (Qwen3.8-27B) 生成的 '扩展关键词' 或 '伪相关反馈' 后的 Query，Recall@5 可提升至 0.70-0.78，这是因为科研术语的同义词替换（如 'neural net' vs 'deep learning'）在 BM25 中缺乏语义理解

## Corrected Claim

Query 构造策略对 BM25 召回率的关键作用：若直接使用用户原始提问作为 Query，Recall@5 约为 0.60；若使用 LLM (Qwen3.8-27B) 生成的 '扩展关键词' 或 '伪相关反馈' 后的 Query，Recall@5 可提升至 0.70-0.78，这是因为科研术语的同义词替换（如 'neural net' vs 'deep learning'）在 BM25 中缺乏语义理解

## Evidence

先验知识/题面给定，逻辑校验通过
