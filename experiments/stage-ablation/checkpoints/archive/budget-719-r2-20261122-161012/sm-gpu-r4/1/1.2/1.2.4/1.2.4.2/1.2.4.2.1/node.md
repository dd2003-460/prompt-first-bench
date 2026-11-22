# N360: FP8 KV Cache 量化对 32K 长文本检索 (RAG) 任务的影响量化：在 32K 上下文中，KV Cache 误差累积主要影响 Attention 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N150

## Claim

FP8 KV Cache 量化对 32K 长文本检索 (RAG) 任务的影响量化：在 32K 上下文中，KV Cache 误差累积主要影响 Attention Score 的精度；经验法则显示，FP8 KV Cache 在长文本检索任务中的 Recall@1 下降通常 < 1-2%，但若任务涉及极细微的数值比较或长距离依赖，误差可能放大，需通过 RAG 基准测试 (如 RAGAS) 实测验证。

## Corrected Claim

FP8 KV Cache 量化在 32K 长文本检索任务中通常对 Recall@1 影响较小，但具体下降幅度取决于模型架构、量化方案及任务特性，建议通过 RAGAS 等基准测试实测验证。

## Evidence

[质询]该陈述包含具体的经验性能指标（Recall@1 下降 < 1-2%），属于经验事实而非第一性原理可推导结论，且缺乏具体模型、硬件及量化算法（如 E4M3/E5M2）的限定，不同实现下误差可能显著不同。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

FP8 KV cache quantization impact long context RAG retrieval accuracy perplexity
