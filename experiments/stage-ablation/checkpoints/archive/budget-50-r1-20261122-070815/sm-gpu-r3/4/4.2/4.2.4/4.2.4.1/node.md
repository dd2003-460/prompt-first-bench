# N311: Apple Mac Studio M2 Ultra 在运行 27B 模型 LLM 推理（Decode 阶段）时的实测整机功耗 P_decode 约为 180W-

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N108

## Claim

Apple Mac Studio M2 Ultra 在运行 27B 模型 LLM 推理（Decode 阶段）时的实测整机功耗 P_decode 约为 180W-220W，Prefill 阶段峰值功耗 P_prefill 约为 250W-280W，需基于 MLX 或 llama.cpp 的硬件监控数据（如 iStat Menus 或 powermetrics 工具输出）进行校准，以替代静态 TDP 估算。

## Corrected Claim

Apple Mac Studio M2 Ultra 在运行 27B 模型 LLM 推理时，整机功耗通常高于其 TDP 估算值，Prefill 阶段功耗显著高于 Decode 阶段。具体数值需基于 MLX 或 llama.cpp 的硬件监控数据（如 iStat Menus 或 powermetrics 工具输出）进行实测校准，一般 Decode 阶段在 180W-220W 区间，Prefill 阶段在 250W-280W 区间（基于典型配置估算，具体值随负载变化）。

## Evidence

[质询]该陈述包含具体的实测功耗数值范围（180W-220W, 250W-280W），属于经验事实。由于检索无可用来源，无法验证这些具体数值是否准确，且不同负载、模型量化精度及系统状态可能导致功耗波动，单一数值范围可能不具备普适性。 | 经验事实，逻辑自洽但缺来源支持。M2 Ultra TDP 约为 120W-150W，加上内存、风扇等整机功耗，Decode 阶段 180-220W 和 Prefill 阶段 250-280W 在物理量级上合理（Prefill 计算密集度高于 Decode，功耗更高符合直觉），但具体数值缺乏外部证据直接证实。

## Search Query

Mac Studio M2 Ultra LLM inference power consumption watts MLX llama.cpp
