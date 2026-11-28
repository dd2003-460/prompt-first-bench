# N280: BM25 在 150M terms (10k docs * 15k tokens) 规模下的查询延迟分解：倒排索引查找 (Inverted Index Look

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N89

## Claim

BM25 在 150M terms (10k docs * 15k tokens) 规模下的查询延迟分解：倒排索引查找 (Inverted Index Lookup) 耗时约 5ms，TF-IDF 评分计算 (Scoring) 耗时约 45ms，合计 50ms；该延迟与 CPU 单核主频及内存带宽强相关，需监控 CPU 频率是否降至基频以下

## Corrected Claim

BM25 在 150M terms 规模下的查询延迟通常由倒排索引查找和评分计算组成，其中评分计算往往占主要耗时；具体延迟数值（如总计50ms）强烈依赖于CPU主频、内存带宽及具体实现优化，需根据实际硬件环境监控。

## Evidence

[质询]具体延迟数值（5ms/45ms）高度依赖硬件配置、文档长度分布及实现细节，属于特定环境下的经验观测值，无法从第一性原理推导，且缺乏通用基准数据支持其作为固定事实。 | source=knowledge，逻辑自洽（BM25计算复杂度与内存访问模式符合描述），但具体毫秒级延迟为经验事实，无外部来源直接支持，依据经验事实排除条款降级。

## Search Query

BM25 query latency breakdown inverted index lookup scoring cost 150 million terms
