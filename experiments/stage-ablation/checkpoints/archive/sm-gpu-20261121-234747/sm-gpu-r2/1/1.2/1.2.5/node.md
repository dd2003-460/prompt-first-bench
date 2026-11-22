# N41: NVIDIA A100 40GB/80GB 在运行 Qwen3-27B INT8 量化版本时的实测吞吐量（单用户，32K 上下文）：约为 30-50 token

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

NVIDIA A100 40GB/80GB 在运行 Qwen3-27B INT8 量化版本时的实测吞吐量（单用户，32K 上下文）：约为 30-50 tokens/s（来源：vLLM 官方 benchmark 报告 2024-11 或第三方独立评测如 Benchmarks.gg 2025-01），需标注具体测试日志和模型版本。

## Corrected Claim

NVIDIA A100 40GB/80GB 在运行 Qwen3-27B INT8 量化版本时的实测吞吐量（单用户，32K 上下文）预计处于数十 tokens/s 量级，具体数值需参考 vLLM 官方 benchmark 或第三方独立评测报告。

## Evidence

[质询]该陈述包含具体的经验性性能数据（吞吐量数值）和特定的测试条件（vLLM benchmark, 32K上下文），属于硬件/软件性能指标，无法从第一性原理推导。且来源标记为search但实际无可用来源，缺乏直接证据支持具体数值范围。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值30-50 tokens/s的准确性）

## Search Query

NVIDIA A100 Qwen3-27B INT8 inference benchmark tokens per second 32K context
