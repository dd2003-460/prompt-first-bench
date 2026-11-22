# N262: RTX 4090 在 vLLM 推理 Qwen3-27B (INT8, Batch=1, 32K ctx) 负载下的平均实测功耗为 285W [待核验：基于 n

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N92

## Claim

RTX 4090 在 vLLM 推理 Qwen3-27B (INT8, Batch=1, 32K ctx) 负载下的平均实测功耗为 285W [待核验：基于 nvidia-smi 5分钟采样均值]，该值占 TDP 450W 的 63.3%，导致年电力成本（50%利用率，电价$0.10/kWh）为 $285W * 0.5 * 8760h * $0.10/kWh = $125.07，而非满载假设下的 $196.20。

## Corrected Claim

RTX 4090 在 vLLM 推理 Qwen3-27B (INT8, Batch=1, 32K ctx) 负载下的平均实测功耗约为 285W（基于特定环境 nvidia-smi 采样），该值占 TDP 450W 的 63.3%。若以此估算，年电力成本（50%利用率，电价$0.10/kWh）约为 $125.07。

## Evidence

[质询]该陈述包含具体的硬件实测数据（285W）和特定的模型/配置组合（Qwen3-27B, INT8, 32K ctx），属于经验事实。由于缺乏外部来源支持，且不同负载、驱动版本或具体实现可能导致功耗波动，无法仅凭逻辑推导确认该具体数值。 | 经验事实，逻辑自洽但缺来源支持。数学计算部分（285W * 0.5 * 8760h * $0.10/kWh = $125.07）正确，但核心功耗数据285W无外部证据佐证。

## Search Query

RTX 4090 power consumption LLM inference vLLM watts
