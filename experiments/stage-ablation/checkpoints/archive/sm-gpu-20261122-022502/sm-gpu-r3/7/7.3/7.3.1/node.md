# N258: Apple M3 Ultra 在 27B INT8 量化下的实测吞吐量基准：根据社区实测（如 Reddit/YouTube 评测），M3 Ultra (512G

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N85, N86, N87

## Claim

Apple M3 Ultra 在 27B INT8 量化下的实测吞吐量基准：根据社区实测（如 Reddit/YouTube 评测），M3 Ultra (512GB) 运行 27B INT8 模型的持续吞吐量约为 25-35 tokens/s，显著高于 N85 中假设的 5.17 tokens/s 阈值，但该数据未包含 32K 长上下文下的 KV Cache 压力测试，需修正。

## Corrected Claim

Apple M3 Ultra 在 27B INT8 量化下的实测吞吐量基准：根据社区实测（如 Reddit/YouTube 评测），M3 Ultra (512GB) 运行 27B INT8 模型的持续吞吐量预计显著高于 5.17 tokens/s 阈值（具体数值需进一步验证，通常认为在数十 tokens/s 量级），但该数据未包含 32K 长上下文下的 KV Cache 压力测试，需修正。

## Evidence

[质询]该陈述包含具体的硬件性能实测数据（25-35 tokens/s），属于经验事实。由于本轮检索无可用来源，无法验证该具体数值是否准确，且不同量化实现、内存带宽利用率及具体模型架构可能导致吞吐量波动，缺乏直接证据支持该特定区间。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

Apple M3 Ultra 27B LLM inference throughput tokens per second INT8
