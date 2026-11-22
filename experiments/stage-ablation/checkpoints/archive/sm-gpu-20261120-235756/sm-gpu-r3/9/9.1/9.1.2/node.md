# N338: Qwen3-27B 的 MoE 路由开销（Routing Overhead）导致实际有效利用率因子（Utilization Factor）低于纯 Dense 模

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N127

## Claim

Qwen3-27B 的 MoE 路由开销（Routing Overhead）导致实际有效利用率因子（Utilization Factor）低于纯 Dense 模型的典型值（0.5-0.7），在 Blackwell 架构上，由于路由逻辑的额外访存和计算，预计有效利用率因子降至 0.35-0.55，需结合 vLLM 对 MoE 算子的具体优化程度进行校准。

## Corrected Claim

Qwen3-27B 的 MoE 路由开销预计会导致实际有效利用率因子低于纯 Dense 模型的典型值（0.5-0.7），在 Blackwell 架构上可能降至 0.35-0.55 区间，具体数值需结合 vLLM 对 MoE 算子的优化程度进行校准。

## Evidence

[质询]该陈述包含具体的经验性数值预测（0.35-0.55），属于硬件/模型性能经验事实，无法从第一性原理严格推导，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

MoE routing overhead impact on GPU inference throughput utilization factor
