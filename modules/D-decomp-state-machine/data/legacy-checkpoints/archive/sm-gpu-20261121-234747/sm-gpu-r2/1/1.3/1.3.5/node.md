# N49: Apple Silicon M2/M3 Max 64GB+ 在运行 Qwen3-27B INT8 量化版本时的实测吞吐量（单用户，32K 上下文）：约为 5-1

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

Apple Silicon M2/M3 Max 64GB+ 在运行 Qwen3-27B INT8 量化版本时的实测吞吐量（单用户，32K 上下文）：约为 5-10 tokens/s（来源：vLLM 官方 benchmark 报告 2024-11 或第三方独立评测如 Benchmarks.gg 2025-01），需标注具体测试日志和模型版本。

## Corrected Claim

Apple Silicon M2/M3 Max 64GB+ 在运行 Qwen3-27B INT8 量化版本时，受限于内存带宽，单用户 32K 上下文下的吞吐量预计处于个位数至低双位数 tokens/s 量级（具体数值需依据特定测试日志确认）。

## Evidence

[质询]该陈述包含具体的硬件规格（M2/M3 Max 64GB+）、模型版本（Qwen3-27B）、量化方式（INT8）及具体性能数值（5-10 tokens/s），属于典型的经验事实。检索无可用来源，无法验证具体数值是否准确，且不同测试环境（如内存带宽限制、上下文长度对KV Cache的影响）可能导致数值波动，存在口径混淆或数值偏差的风险。 | 经验事实，逻辑自洽但缺来源支持。M2/M3 Max 内存带宽（~400GB/s）在运行 27B INT8 模型（~27GB 权重 + KV Cache）时，理论极限吞吐量受限于内存带宽，5-10 tokens/s 的量级在物理上合理，但具体数值缺乏外部证据直接支持。

## Search Query

Apple Silicon M2 M3 Max Qwen3-27B INT8 inference benchmark tokens per second 32K context
