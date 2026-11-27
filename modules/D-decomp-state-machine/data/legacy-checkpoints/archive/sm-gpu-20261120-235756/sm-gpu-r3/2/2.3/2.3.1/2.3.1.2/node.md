# N199: A100 80GB SXM 作为高带宽/高容量前沿点，其 2039 GB/s 带宽虽略高于 RTX 5090，但受限于 $5,000 二手价及 80GB 显存带

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N61

## Claim

A100 80GB SXM 作为高带宽/高容量前沿点，其 2039 GB/s 带宽虽略高于 RTX 5090，但受限于 $5,000 二手价及 80GB 显存带来的高并发潜力，其单位带宽成本 ($/GB/s) 约为 RTX 5090 的 1.4 倍，但在 Batch Size > 2 场景下因显存容量优势可摊薄单 Token 成本，形成与 RTX 5090 不同的 TCO 最优区间。

## Corrected Claim

A100 80GB SXM 的带宽（2039 GB/s）略高于 RTX 5090，但在当前二手市场价格下，其单位带宽成本约为 RTX 5090 的 1.4 倍；在 Batch Size > 2 且受显存容量限制的场景中，A100 可能因更高的并发处理能力而具有更优的单 Token 成本，具体 TCO 优势取决于负载特征。

## Evidence

[质询]RTX 5090 的显存带宽（约 1.8 TB/s）和价格（约 $2,000）为经验事实，且 A100 80GB SXM 的二手价格波动较大，$5,000 仅为特定市场快照，非固定属性；此外，'TCO 最优区间'的结论依赖于具体的负载模型和电价假设，缺乏通用性。 | 经验事实，逻辑自洽但缺来源支持
