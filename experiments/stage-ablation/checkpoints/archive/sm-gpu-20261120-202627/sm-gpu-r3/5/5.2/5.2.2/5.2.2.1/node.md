# N379: A100 80GB SXM 在运行 Qwen3-27B (BF16, 32K ctx, Batch=1) 持续解码负载下的平均功耗 P_avg 约为 320W 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N120, N121, N122

## Claim

A100 80GB SXM 在运行 Qwen3-27B (BF16, 32K ctx, Batch=1) 持续解码负载下的平均功耗 P_avg 约为 320W (基于 TDP 400W × 负载因子 0.8 估算，需实测校准)，用于替换 N120 中的 0.7 系数以精确计算 OpEx。

## Corrected Claim

A100 80GB SXM 在运行 Qwen3-27B (BF16, 32K ctx, Batch=1) 持续解码负载下的平均功耗 P_avg 估算约为 320W (基于 TDP 400W × 负载因子 0.8)，该值为理论估算，实际 OpEx 计算建议采用实测功耗数据或保守区间。

## Evidence

[质询]该数值为基于 TDP 的估算值（400W * 0.8），而非实测数据。不同模型（Qwen3-27B）在特定上下文长度（32K）和批处理大小（Batch=1）下的实际功耗可能显著偏离 0.8 的负载因子，且 SXM 版本的功耗受散热和频率调节影响，直接将其作为精确 OpEx 计算的固定系数存在不确定性。 | 先验知识/题面给定，逻辑校验通过。A100 SXM TDP 为 400W，推理负载下功耗低于 TDP 符合物理直觉，但具体数值 320W 为估算值，缺乏实测来源支持，故降级为定性/估算表述。

## Search Query

A100 80GB SXM average power consumption LLM inference 32k context benchmark
