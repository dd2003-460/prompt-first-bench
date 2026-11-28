# N453: Cross-Encoder 重排序模型的推理延迟基准：BGE-reranker-base（110M 参数）在 V100 上处理 Top-50 候选（平均序列长度

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N157

## Claim

Cross-Encoder 重排序模型的推理延迟基准：BGE-reranker-base（110M 参数）在 V100 上处理 Top-50 候选（平均序列长度 512 tokens）的 P50 延迟为 15-25ms（Batch Size=1），P99 延迟 <50ms；若使用 Qwen3.8-27B 作为重排器，延迟将飙升至 2-5s（需生成完整评分），不可用于 <200ms 总延迟目标

## Corrected Claim

Cross-Encoder 重排序模型（如 BGE-reranker-base）在 V100 上处理 Top-50 候选的 P50 延迟通常在几十毫秒级别（约 10-50ms），可满足低延迟需求；而使用大语言模型（如 27B 参数规模）进行生成式重排序，由于需要自回归生成，延迟通常达到秒级（>1s），难以满足 <200ms 的严格实时性要求。

## Evidence

[质询]具体延迟数值（15-25ms, <50ms, 2-5s）属于高度依赖硬件驱动版本、CUDA配置及具体实现细节的经验数据，缺乏通用标准，且Qwen3.8-27B作为重排器的具体延迟范围缺乏公开基准支持，存在数值夸大或特定环境偏差的风险。 | 经验事实，逻辑自洽（Cross-Encoder计算复杂度高于Bi-Encoder，LLM生成式评分远高于判别式打分），但检索无可用来源，无法验证具体数值量级，故降级。

## Search Query

BGE reranker base inference latency V100 top50 candidates ms
