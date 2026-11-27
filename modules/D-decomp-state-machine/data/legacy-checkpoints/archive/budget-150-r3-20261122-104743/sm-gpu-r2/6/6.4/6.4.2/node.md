# N178: 量化质量损失数据的模型特异性偏差：学术文献中关于 Qwen 系列模型的量化评测较少，多数数据基于 LLaMA 或 Mistral 系列。由于 Qwen3-27B

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

量化质量损失数据的模型特异性偏差：学术文献中关于 Qwen 系列模型的量化评测较少，多数数据基于 LLaMA 或 Mistral 系列。由于 Qwen3-27B 采用了特定的注意力机制（如 GQA），其量化敏感度可能与 LLaMA 不同。经验法则表明，若缺乏特定模型的评测，应将文献中的困惑度增加阈值放宽 20%（例如从 5% 放宽到 6%）作为保守估计，或必须自行运行小规模校准测试 [待核验：需查 Qwen3 官方技术报告或第三方评测]

## Corrected Claim

学术文献中关于 Qwen 系列模型的量化评测较少，多数数据基于 LLaMA 或 Mistral 系列。由于 Qwen 系列模型可能采用特定的注意力机制（如 GQA），其量化敏感度可能与 LLaMA 不同。在缺乏特定模型评测数据时，建议参考 LLaMA/Mistral 的量化敏感度作为保守估计，或必须自行运行小规模校准测试以获取准确数据。

## Evidence

[质询]「将困惑度增加阈值放宽 20%」这一具体经验法则缺乏普遍公认的学术或工程依据，属于高度特定的经验性建议，且 Qwen3-27B 是否采用 GQA 等具体架构细节需以官方技术报告为准，不能仅凭系列名称推断。 | 先验知识/题面给定，逻辑校验通过；但具体量化阈值调整比例（20%）为经验性参数，缺乏直接来源支持，故降级。

## Search Query

Qwen3 quantization sensitivity GQA perplexity increase benchmark
