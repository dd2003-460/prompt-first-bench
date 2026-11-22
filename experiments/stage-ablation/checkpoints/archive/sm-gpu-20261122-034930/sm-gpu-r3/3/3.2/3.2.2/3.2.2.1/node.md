# N265: A100 40GB SXM/PCIe 在 Qwen3-27B INT8 推理负载下的实测平均功耗分布：P50 约为 260W，P95 约为 320W，基于 Se

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N93

## Claim

A100 40GB SXM/PCIe 在 Qwen3-27B INT8 推理负载下的实测平均功耗分布：P50 约为 260W，P95 约为 320W，基于 ServeTheHome 或 NVIDIA 官方能效白皮书的负载曲线数据（非 TDP 估算），用于修正 N93 中 240-280W 的宽泛区间。

## Corrected Claim

A100 40GB SXM/PCIe 在 Qwen3-27B INT8 推理负载下的实测平均功耗通常低于 TDP（400W），具体 P50/P95 数值需依据特定测试环境数据，建议保留为定性描述或标注为待验证的估算值。

## Evidence

[质询]具体数值（P50 260W, P95 320W）属于特定硬件在特定模型负载下的经验测量数据，无法从第一性原理推导，且缺乏来源支持其精确性；此外，Qwen3-27B 的具体版本及 INT8 量化实现细节可能影响功耗，单一来源或无来源情况下难以确证该精确分布。 | 经验事实，逻辑自洽（A100 TDP 400W，INT8 推理功耗低于 TDP 合理），但缺来源支持（本轮检索无可用来源）。

## Search Query

A100 40GB average power consumption LLM inference benchmark watts
