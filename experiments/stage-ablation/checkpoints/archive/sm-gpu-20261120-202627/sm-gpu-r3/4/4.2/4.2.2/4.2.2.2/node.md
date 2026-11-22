# N335: NVIDIA A100 80GB 在 Qwen3-27B (BF16) Decode 阶段 (Batch=1, 32K context) 的实测平均功耗 P_a

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N105

## Claim

NVIDIA A100 80GB 在 Qwen3-27B (BF16) Decode 阶段 (Batch=1, 32K context) 的实测平均功耗 P_avg 约为 300-350W，对应功耗占比系数 α_avg ≈ 0.75-0.88 (基于 TDP=400W)，HBM2e 能效优于 GDDR6X。

## Corrected Claim

NVIDIA A100 80GB 在 Qwen3-27B (BF16) Decode 阶段 (Batch=1, 32K context) 的功耗通常低于其 400W TDP，具体数值需依据实测数据确定；HBM2e 在能效上通常优于 GDDR6X。

## Evidence

[质询]该陈述包含具体的硬件功耗实测数据（300-350W）和能效对比结论，属于经验事实。在缺乏直接来源支持的情况下，仅凭逻辑自洽无法确证具体数值区间及特定模型下的功耗表现，存在因负载特性（如32K长上下文导致的KV Cache读取压力）导致功耗偏离常规估计的风险。 | 经验事实，逻辑自洽但缺来源支持。A100 TDP为400W，Decode阶段功耗低于峰值符合物理直觉，但具体数值300-350W及HBM2e能效优势需实测数据佐证，当前无可用外部证据。

## Search Query

A100 80GB LLM inference power consumption watts decode phase benchmark
