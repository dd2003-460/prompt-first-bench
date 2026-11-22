# N265: NVIDIA L40S 48GB 版本在 2024-2025 年的采购均价约为 $9,500 - $11,000，其显存容量 48GB 可能不足以容纳 Qwen

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N72

## Claim

NVIDIA L40S 48GB 版本在 2024-2025 年的采购均价约为 $9,500 - $11,000，其显存容量 48GB 可能不足以容纳 Qwen3-27B BF16 权重（约 54GB）+ 32K KV Cache，需使用 INT8 或 FP8 量化才能运行，这会影响最终性价比评估。

## Corrected Claim

NVIDIA L40S 48GB 版本在 2024-2025 年的采购均价约为 $9,500 - $11,000（待核实），其显存容量 48GB 不足以容纳 Qwen3-27B BF16 权重（约 54GB）+ 32K KV Cache，需使用 INT8 或 FP8 量化才能运行，这会影响最终性价比评估。

## Evidence

[质询]该陈述包含具体的市场价格区间（$9,500 - $11,000）和硬件规格细节，属于经验事实。由于检索失败无外部来源支持，且市场价格随时间波动，无法仅凭逻辑推导确认该特定时间段内的精确均价，存在数值偏差风险。 | 经验事实，逻辑自洽但缺来源支持。Qwen3-27B BF16权重约54GB确实超过L40S 48GB显存，需量化或分片，逻辑推导成立；但价格部分无来源佐证。

## Search Query

L40S 48GB price 2024 2025
