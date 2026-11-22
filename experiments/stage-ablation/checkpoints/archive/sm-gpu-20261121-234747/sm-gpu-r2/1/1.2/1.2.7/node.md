# N43: NVIDIA L40S 48GB 在运行 Qwen3-27B INT8 量化版本时的实测吞吐量（单用户，32K 上下文）：约为 25-40 tokens/s（来

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

NVIDIA L40S 48GB 在运行 Qwen3-27B INT8 量化版本时的实测吞吐量（单用户，32K 上下文）：约为 25-40 tokens/s（来源：vLLM 官方 benchmark 报告 2024-11 或第三方独立评测如 Benchmarks.gg 2025-01），需标注具体测试日志和模型版本。

## Corrected Claim

NVIDIA L40S 48GB 在运行 Qwen3-27B INT8 量化版本时的实测吞吐量（单用户，32K 上下文）预计约为 25-40 tokens/s，具体数值需依据实际测试日志和模型版本确认。

## Evidence

[质询]该陈述包含具体的硬件规格（L40S 48GB）、模型版本（Qwen3-27B，注：截至2024年底Qwen3尚未正式发布，可能存在版本混淆或指代Qwen2.5-32B等）、量化方式及特定上下文长度下的吞吐量数值。这些属于经验事实，且引用的来源（vLLM 2024-11或Benchmarks.gg 2025-01）在当前检索中不可用，无法验证具体数值（25-40 tokens/s）的准确性及测试条件的一致性。 | 经验事实，逻辑自洽但缺来源支持。L40S 48GB显存足以容纳27B INT8模型（约27GB权重+KV Cache），32K上下文下受限于显存带宽和KV Cache大小，25-40 tokens/s的吞吐量在量级上合理，但具体数值无法通过现有来源验证。

## Search Query

NVIDIA L40S Qwen3-27B INT8 inference benchmark tokens per second 32K context
