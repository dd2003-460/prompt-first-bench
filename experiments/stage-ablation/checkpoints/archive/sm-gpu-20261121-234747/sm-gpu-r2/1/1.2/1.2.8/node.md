# N44: AMD MI300X 192GB 在运行 Qwen3-27B INT8 量化版本时的实测吞吐量（单用户，32K 上下文）：约为 60-100 tokens/s（

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

AMD MI300X 192GB 在运行 Qwen3-27B INT8 量化版本时的实测吞吐量（单用户，32K 上下文）：约为 60-100 tokens/s（来源：vLLM 官方 benchmark 报告 2024-11 或第三方独立评测如 Benchmarks.gg 2025-01），需标注具体测试日志和模型版本。

## Corrected Claim

AMD MI300X 192GB 在运行 Qwen3-27B INT8 量化版本时，单用户 32K 上下文下的实测吞吐量预计处于数十 tokens/s 量级（具体数值需参考 vLLM 官方 benchmark 或第三方独立评测日志，当前缺乏确切来源支持）。

## Evidence

[质询]该陈述包含具体的经验性性能数据（吞吐量数值范围）和特定的测试条件（单用户、32K上下文、INT8量化），属于硬件/软件性能基准测试范畴，无法从第一性原理推导。且引用的来源（vLLM 2024-11 或 Benchmarks.gg 2025-01）在参考来源中缺失，无法验证其真实性和具体数值。 | 经验事实，逻辑自洽但缺来源支持。MI300X 192GB 显存足以容纳 Qwen3-27B INT8 模型，60-100 tokens/s 在单用户长上下文场景下符合大模型推理的一般量级直觉，但因无外部来源直接支持具体数值，依据经验事实排除条款降级。

## Search Query

AMD MI300X Qwen3-27B INT8 inference benchmark tokens per second 32K context
