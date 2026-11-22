# N178: Qwen3-27B 在 AWQ (W4A16) 量化下的 GSM8K 具体实测得分（需引用特定量化库的 benchmark 结果，以验证 84.0% 这一假设值

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

Qwen3-27B 在 AWQ (W4A16) 量化下的 GSM8K 具体实测得分（需引用特定量化库的 benchmark 结果，以验证 84.0% 这一假设值，并计算实际 Δ）

## Corrected Claim

Qwen3-27B 在 AWQ (W4A16) 量化下的 GSM8K 得分约为 84.0%（基于假设值，需特定量化库 benchmark 验证），实际 Δ 需根据具体实测数据计算。

## Evidence

[质询]该陈述包含具体的经验性数值（84.0%）和特定量化配置（AWQ W4A16）下的实测得分，属于经验事实。由于缺乏外部来源支持，无法验证该具体数值的准确性，且不同量化库（如 GPTQModel, AutoGPTQ, bitsandbytes）的实现差异可能导致结果波动，直接断言具体得分存在风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。Qwen3-27B 在 GSM8K 上通常表现优异，84.0% 在合理量级范围内，但具体数值需依赖特定 benchmark 数据，无法从第一性原理推出。

## Search Query

Qwen3-27B AWQ W4A16 GSM8K score benchmark
