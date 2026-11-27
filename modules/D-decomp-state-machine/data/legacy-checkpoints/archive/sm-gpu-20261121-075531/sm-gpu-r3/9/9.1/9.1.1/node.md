# N349: RTX 4090 (24GB) 运行 Qwen3-27B INT8 (W8A8) 时，Prefill 阶段 (处理 32K context) 的实测吞吐量 (T

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N117

## Claim

RTX 4090 (24GB) 运行 Qwen3-27B INT8 (W8A8) 时，Prefill 阶段 (处理 32K context) 的实测吞吐量 (Tokens/s)，受限于 SM 计算密度和 Tensor Core INT8 峰值算力 (约 330 TOPS)，典型值在 1000-3000 Tokens/s 区间 [待核验]。

## Corrected Claim

RTX 4090 (24GB) 运行 Qwen3-27B INT8 (W8A8) 时，Prefill 阶段 (处理 32K context) 的实测吞吐量受限于 SM 计算密度和 Tensor Core INT8 峰值算力，具体数值取决于推理框架优化程度，通常在千级 Tokens/s 量级。

## Evidence

[质询]该陈述包含具体的硬件性能实测数据（1000-3000 Tokens/s），属于经验事实。虽然RTX 4090的INT8峰值算力约为330 TOPS（或更高，取决于具体计算方式，通常标称更高，但量级正确）是合理的，但Prefill阶段的吞吐量受内存带宽、SM利用率、Kernel优化等多种因素影响，且Qwen3-27B的具体模型架构细节（如MoE或Dense）会显著影响实际吞吐。在没有具体基准测试数据支持的情况下，直接给出一个具体的数值区间（1000-3000）缺乏严谨性，且不同推理框架（如vLLM, TensorRT-LLM）的结果可能差异巨大。 | 经验事实，逻辑自洽但缺来源支持。RTX 4090的算力量级与Prefill阶段计算密集型特征相符，但具体吞吐量数值需依赖特定软件栈和模型实现的基准测试，当前无可用外部证据直接支持该具体区间。

## Search Query

RTX 4090 Qwen3-27B INT8 vLLM prefill throughput tokens per second benchmark
