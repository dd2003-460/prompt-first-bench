# N83: RTX 5090 在 LLM 推理负载下的平均功耗 P_avg_5090 预计为 350-450W，保守估计取 400W 用于 TCO 计算 [待核验]。

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N21

## Claim

RTX 5090 在 LLM 推理负载下的平均功耗 P_avg_5090 预计为 350-450W，保守估计取 400W 用于 TCO 计算 [待核验]。

## Corrected Claim

RTX 5090 在 LLM 推理负载下的平均功耗 P_avg_5090 预计为 350-450W，保守估计取 400W 用于 TCO 计算（注：该数值为基于典型高负载场景的估算，实际功耗随负载波动，建议以实测或官方 TDP 上限为参考进行敏感性分析）。

## Evidence

[质询]RTX 5090 的 TDP 官方规格尚未完全公开或存在不同版本（如 575W vs 其他），且 LLM 推理负载下的实际平均功耗受模型大小、Batch Size、量化方式影响极大，350-450W 的范围可能偏窄或偏宽，缺乏具体负载场景的实测数据支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且属于硬件功耗经验参数，不适用第一性原理推导）

## Search Query

RTX 5090 average power consumption LLM inference load watts
