# N193: L40S 48GB 运行 Qwen3-27B INT8 (AWQ/GPTQ) 在 32K 上下文下的 Decode 阶段单卡吞吐量基准值：基于 GDDR6 带宽

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42, N43, N44

## Claim

L40S 48GB 运行 Qwen3-27B INT8 (AWQ/GPTQ) 在 32K 上下文下的 Decode 阶段单卡吞吐量基准值：基于 GDDR6 带宽 864 GB/s 与 INT8 权重加载特性，理论上限约为 864GB/s / 27GB * 1000ms ≈ 32 tokens/s，实测受 PCIe 4.0 及算子效率限制通常在 20-30 tokens/s 区间（来源：vLLM benchmark 或 L40S 官方白皮书实测数据）

## Corrected Claim

L40S 48GB 运行 Qwen3-27B INT8 在 32K 上下文下的 Decode 阶段，受限于 GDDR6 带宽（约 864 GB/s），理论吞吐量上限约为 32 tokens/s；实际吞吐量通常低于此理论值，具体数值取决于量化实现及算子优化效率。

## Evidence

[质询]该陈述包含具体的硬件规格（L40S 48GB, GDDR6 864GB/s）和特定的性能基准数据（20-30 tokens/s），属于经验事实。虽然理论计算逻辑自洽，但缺乏外部来源直接支持具体的实测区间，且不同量化方案（AWQ/GPTQ）及框架（vLLM）下的实际性能可能因实现细节差异而波动，单一理论推导不足以确证具体实测区间。 | 经验事实，逻辑自洽但缺来源支持。理论上限计算（864/27≈32）符合内存带宽瓶颈下的Decode阶段基本物理直觉，但具体实测值20-30 tokens/s缺乏检索来源直接验证。

## Search Query

L40S 48GB Qwen3-27B INT8 vLLM benchmark tokens per second 32k context
